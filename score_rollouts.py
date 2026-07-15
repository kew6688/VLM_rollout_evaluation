#!/usr/bin/env python3
"""Score rollout videos with an OpenAI-compatible vision model.

The script samples frames from five local rollout videos, sends them to the
Chat Completions API, and stores model scores alongside simulator results.

python3 gpt_score_rollouts.py \
  --use-preprocessed \
  --api-key sk-xxxx \
  --model gpt-4

python3 score_rollouts.py --max-images 50 --max-tokens 20000  --use-api-debug --api-key sk-ogTY963b0zjUj9LRY9P4LBtWB6GTUs1HX7oB7QEqNtg6IxIA --model kimi-k2.6   --task-source preprocessed   --use-preprocessed    --workers 10 --timeout 900 --api-retries 3 --api-retry-backoff 20 --frames-root outputs/ebench_preprocessed_frames
"""

from __future__ import annotations

import argparse
import base64
import concurrent.futures
import json
import os
import re
import socket
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CAMERAS = [
    "top_camera.mp4",
    "overlook_camera.mp4",
    "left_camera.mp4",
    "right_camera.mp4",
]


COMMON_PROMPT = """You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Each input image may be a 2x2 synchronized multi-camera composite:
top-left = top_camera, top-right = overlook_camera, bottom-left = left_camera, bottom-right = right_camera.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.
Return JSON only with these required scoring keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
By default, include only these three keys unless explicit additional output fields are requested.
The reason must be one short sentence explaining the visible evidence behind the score.
Do not output hidden chain-of-thought, frame-by-frame analysis, markdown, or any text outside the JSON object.
You must output only the JSON object; do not output any analysis, explanation, notes, or prose before or after it.
Do not leave the final answer empty. Put the JSON object in the assistant message content.
"""


EVIDENCE_OUTPUT_INSTRUCTION = """
Additional output requirement:
Return JSON with these keys:
{"score": number, "success": 0 or 1, "reason": string, "evidence": [string], "metric_breakdown": object}
- evidence: 2 to 5 short strings listing only visible observations from the input frames.
- metric_breakdown: a compact object describing each metric condition, its weight or contribution, whether it is visibly satisfied, and the visible evidence used.
- Do not include hidden chain-of-thought. Provide only concise observable evidence and metric arithmetic needed to audit the score.
"""

@dataclass(frozen=True)
class RolloutTask:
    task_id: str
    episode_id: str
    rollout_dir: str
    prompt: str
    frame_dir: str | None = None
    episode_path: str | None = None
    source: str = "rollout_video"


TASK_PROMPTS = {
    "apple_to_fruit_bowl": COMMON_PROMPT
    + """
Task: apple_to_fruit_bowl
Instruction: Put the apple into the fruit bowl.

Metric:
- score = 1.0 if the apple is placed inside the fruit bowl.
- score = 0.0 otherwise.

Scoring:
- If the apple is visibly inside the fruit bowl at the end of the rollout, set score = 1.0 and success = 1.
- If the apple is not inside the fruit bowl, is dropped outside, only touched, only moved near the bowl, or the final state is ambiguous, set score = 0.0 and success = 0.
- Write the reason yourself from the visible final-state evidence.
""",
    "bookmark_on_book": COMMON_PROMPT
    + """
Task: bookmark_on_book
Instruction: Place the bookmark on the book.

Metric:
- score = 1.0 if the bookmark is placed on the book with at least 40% visible overlap.
- score = 0.0 otherwise.

Scoring:
- If the bookmark is visibly on top of the book and at least about 40% of the bookmark overlaps the book, set score = 1.0 and success = 1.
- If the bookmark is not on the book, overlaps less than about 40%, is dropped elsewhere, set score = 0.0 and success = 0.
- Write the reason yourself from the visible final-state evidence.
""",
    "detergent": COMMON_PROMPT
    + """
Task: detergent
Instruction: Complete the detergent task by placing or handing over all detergent items as required.

Metric:
- There are 3 detergent items.
- Each completed detergent item is worth 1/3.
- score = (number of visibly completed detergent items) / 3.
- success = 1 only if all 3 detergent items are completed, so score = 1.0.

Scoring:
- If 0 detergent items are completed, set score = 0.0 and success = 0.
- If 1 detergent item is completed, set score = 0.3333333333 and success = 0.
- If 2 detergent items are completed, set score = 0.6666666667 and success = 0.
- If 3 detergent items are completed, set score = 1.0 and success = 1.
- Count only detergent items whose final required state is visibly completed. Do not count items that are only contacted, moved partway, dropped, or ambiguous.
- Write the reason yourself from the visible evidence and the number of completed detergent items.
""",
    "utensils_to_holder": COMMON_PROMPT
    + """
Task: utensils_to_holder
Instruction: Place both the spoon and the fork onto the holder.

Metric:
- The spoon placed on the holder is worth 0.5.
- The fork placed on the holder is worth 0.5.
- The order does not matter.
- score = 0.5 * spoon_on_holder + 0.5 * fork_on_holder.
- success = 1 only if both spoon and fork are on the holder, so score = 1.0.

Scoring:
- If neither utensil is on the holder, set score = 0.0 and success = 0.
- If exactly one of the spoon or fork is on the holder, set score = 0.5 and success = 0.
- If both the spoon and fork are on the holder, set score = 1.0 and success = 1.
- Do not count a utensil that is only touched, moved near the holder, dropped outside the holder, or visually ambiguous.
- Write the reason yourself from the visible evidence for which utensils are on the holder.
""",
    "put_glass_in_glassbox": COMMON_PROMPT
    + """
Task: put_glass_in_glassbox
Instruction: Put the glasses into the glasses box, fold the temples, and close the box.

Metric:
- Both temples of the glasses folded is worth 1/3.
- The glasses box fully closed is worth 1/3.
- The glasses completely inside the glasses box is worth 1/3.
- score = (1/3) * temples_folded + (1/3) * box_closed + (1/3) * glasses_inside_box.
- success = 1 only if all three conditions are satisfied, so score = 1.0.

Important detail:
- For the "glasses inside the glasses box" condition, count it as satisfied as long as the glasses are inside the box, even if the temples are not folded or the box is not closed.
- For the "temples folded" condition, both temples must be visibly folded. If only one temple is folded or the view is ambiguous, do not count this condition.

Scoring:
- Return score as one of 0.0, 0.3333333333, 0.6666666667, or 1.0 according to how many of the three conditions are visibly satisfied.
- Return success = 1 only when score = 1.0.
- Do not count conditions that are only attempted, partially visible, or ambiguous.
""",
    "collect_coffee_beans": COMMON_PROMPT
    + """
Task: collect_coffee_beans
Instruction: Put the lid on the jar and collect the coffee beans into the jar.

Metric:
- The lid placed on the jar is worth 0.5.
- There are 7 coffee beans.
- Each coffee bean visibly inside the jar is worth 0.5 / 7.
- score = 0.5 * lid_on_jar + (0.5 / 7) * number_of_beans_inside_jar.
- success = 1 only if the lid is on the jar and all 7 coffee beans are inside the jar, so score = 1.0.

Lid condition:
- Count lid_on_jar = 1 only if the lid is visibly placed on the jar, the lid center is close to the jar center axis, and the lid is roughly parallel to the tabletop.
- If the lid is only touched, moved near the jar, tilted off the jar, dropped elsewhere, or ambiguous, count lid_on_jar = 0.

Coffee bean condition:
- Count each coffee bean independently.
- Count a bean only if it is visibly inside the jar at the end of the rollout.
- Do not count beans that are outside the jar, on the rim, only moved near the jar, hidden/ambiguous, or not clearly visible inside the jar.

Scoring:
- Return score as 0.5 * lid_on_jar + 0.0714285714 * number_of_beans_inside_jar.
- Return success = 1 only when score = 1.0.
""",
}


SCORE_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "number"},
        "success": {"type": "integer", "enum": [0, 1]},
        "reason": {"type": "string"},
    },
    "required": ["score", "success", "reason"],
    "additionalProperties": False,
}


DEFAULT_API_BASE_URL = "http://35.220.164.252:3888"


def task_prompt_with_explanation(task_prompt: str, explanation_mode: str) -> str:
    if explanation_mode == "evidence":
        return task_prompt + EVIDENCE_OUTPUT_INSTRUCTION
    return task_prompt


def safe_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("_") or "model"


def _load_cv2() -> Any:
    try:
        import cv2
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Missing dependency: cv2. Install it with "
            "`python3 -m pip install -U opencv-python-headless`."
        ) from exc
    return cv2


def _uniform_indices(total: int, num_frames: int) -> list[int]:
    if total <= 0:
        raise ValueError("Cannot sample from a video with no frames")
    if num_frames <= 1:
        return [0]
    return [round(i * (total - 1) / (num_frames - 1)) for i in range(num_frames)]


def _encode_jpeg_bytes(frame: Any, jpeg_quality: int) -> bytes:
    cv2 = _load_cv2()
    ok, buffer = cv2.imencode(
        ".jpg",
        frame,
        [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality],
    )
    if not ok:
        raise ValueError("Failed to encode frame as JPEG")
    return buffer.tobytes()


def _encode_jpeg_b64(frame: Any, jpeg_quality: int) -> str:
    return base64.b64encode(_encode_jpeg_bytes(frame, jpeg_quality)).decode("utf-8")


def _resize_to_max_side(frame: Any, max_side: int | None) -> Any:
    if max_side is None or max_side <= 0:
        return frame
    height, width = frame.shape[:2]
    largest_side = max(height, width)
    if largest_side <= max_side:
        return frame
    scale = max_side / largest_side
    new_width = max(1, round(width * scale))
    new_height = max(1, round(height * scale))
    cv2 = _load_cv2()
    return cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_AREA)


def _decode_jpeg_b64(frame_b64: str) -> Any:
    import numpy as np

    cv2 = _load_cv2()
    encoded = np.frombuffer(base64.b64decode(frame_b64), dtype=np.uint8)
    frame = cv2.imdecode(encoded, cv2.IMREAD_COLOR)
    if frame is None:
        raise ValueError("Failed to decode base64 JPEG frame")
    return frame


def compress_encoded_frames(
    frames: list[str],
    max_side: int | None,
    jpeg_quality: int | None,
) -> tuple[list[str], dict[str, Any]]:
    should_resize = max_side is not None and max_side > 0
    should_reencode = jpeg_quality is not None and jpeg_quality > 0
    if not should_resize and not should_reencode:
        return frames, {
            "enabled": False,
            "max_side": None,
            "jpeg_quality": None,
            "base64_chars_before": sum(len(frame) for frame in frames),
            "base64_chars_after": sum(len(frame) for frame in frames),
        }

    quality = max(1, min(100, int(jpeg_quality if should_reencode else 85)))
    compressed_frames = []
    for frame_b64 in frames:
        frame = _decode_jpeg_b64(frame_b64)
        frame = _resize_to_max_side(frame, max_side)
        compressed_frames.append(_encode_jpeg_b64(frame, quality))

    return compressed_frames, {
        "enabled": True,
        "max_side": max_side if should_resize else None,
        "jpeg_quality": quality,
        "base64_chars_before": sum(len(frame) for frame in frames),
        "base64_chars_after": sum(len(frame) for frame in compressed_frames),
    }


def _frame_indices(total: int, fps: float, sample_every_sec: float, num_frames: int | None) -> list[int]:
    if num_frames is not None:
        return _uniform_indices(total, num_frames)

    if total <= 0:
        raise ValueError("Cannot sample from a video with no frames")
    if fps <= 0:
        raise ValueError(f"Cannot sample by seconds from a video with invalid fps: {fps}")
    if sample_every_sec <= 0:
        raise ValueError("--sample-every-sec must be positive")

    step = max(1, round(fps * sample_every_sec))
    return list(range(0, total, step))


def _label_frame(frame: Any, label: str) -> Any:
    cv2 = _load_cv2()
    labeled = frame.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.7
    thickness = 2
    (text_w, text_h), baseline = cv2.getTextSize(label, font, scale, thickness)
    cv2.rectangle(labeled, (0, 0), (text_w + 14, text_h + baseline + 12), (0, 0, 0), -1)
    cv2.putText(
        labeled,
        label,
        (7, text_h + 6),
        font,
        scale,
        (255, 255, 255),
        thickness,
        cv2.LINE_AA,
    )
    return labeled


def _resize_to_cell(frame: Any, width: int, height: int) -> Any:
    cv2 = _load_cv2()
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def sample_single_camera_frames(
    video_path: Path,
    sample_every_sec: float,
    num_frames: int | None,
    jpeg_quality: int,
    output_dir: Path | None = None,
    max_side: int | None = None,
) -> list[str]:
    cv2 = _load_cv2()
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total <= 0:
        cap.release()
        raise ValueError(f"Video has no readable frames: {video_path}")
    fps = float(cap.get(cv2.CAP_PROP_FPS))

    indices = _frame_indices(total, fps, sample_every_sec, num_frames)
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)

    frames = []
    last_frame_b64 = None
    for sample_idx, idx in enumerate(indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ok, frame = cap.read()
        if not ok:
            if last_frame_b64 is not None:
                frames.append(last_frame_b64)
            continue

        frame = _resize_to_max_side(frame, max_side)
        jpeg_bytes = _encode_jpeg_bytes(frame, jpeg_quality)
        if output_dir is not None:
            (output_dir / f"frame_{sample_idx:03d}.jpg").write_bytes(jpeg_bytes)
        last_frame_b64 = base64.b64encode(jpeg_bytes).decode("utf-8")
        frames.append(last_frame_b64)

    cap.release()
    if not frames:
        raise ValueError(f"No frames sampled from video: {video_path}")
    return frames


def sample_synced_camera_frames(
    rollout_dir: Path,
    cameras: list[str],
    sample_every_sec: float,
    num_frames: int | None,
    jpeg_quality: int,
    output_dir: Path | None = None,
    max_side: int | None = None,
) -> tuple[list[str], dict[str, Any]]:
    cv2 = _load_cv2()
    if not cameras:
        raise ValueError("At least one camera is required")
    if len(cameras) == 1:
        video_path = rollout_dir / cameras[0]
        frames = sample_single_camera_frames(
            video_path,
            sample_every_sec,
            num_frames,
            jpeg_quality,
            output_dir=output_dir,
            max_side=max_side,
        )
        return frames, {
            "video_paths": [str(video_path)],
            "frame_mode": "single_camera",
            "frame_counts": {cameras[0]: len(frames)},
            "frame_paths": sorted(str(path) for path in output_dir.glob("frame_*.jpg"))
            if output_dir is not None
            else [],
        }

    captures = []
    frame_counts = {}
    frame_rates = {}
    for camera in cameras:
        video_path = rollout_dir / camera
        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            for opened_cap, _camera, _path in captures:
                opened_cap.release()
            raise ValueError(f"Cannot open video: {video_path}")

        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if total <= 0:
            cap.release()
            for opened_cap, _camera, _path in captures:
                opened_cap.release()
            raise ValueError(f"Video has no readable frames: {video_path}")

        captures.append((cap, camera, video_path))
        frame_counts[camera] = total
        frame_rates[camera] = float(cap.get(cv2.CAP_PROP_FPS))

    sample_total = min(frame_counts.values())
    sample_fps = min(fps for fps in frame_rates.values() if fps > 0)
    indices = _frame_indices(sample_total, sample_fps, sample_every_sec, num_frames)
    last_frames: dict[str, Any] = {}
    encoded_frames = []
    frame_paths = []
    cell_width = None
    cell_height = None
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)

    try:
        for sample_idx, idx in enumerate(indices):
            camera_frames = []
            for cap, camera, video_path in captures:
                cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
                ok, frame = cap.read()
                if not ok:
                    frame = last_frames.get(camera)
                if frame is None:
                    raise ValueError(f"Cannot read frame {idx} from {video_path}")

                last_frames[camera] = frame
                if cell_width is None or cell_height is None:
                    cell_height, cell_width = frame.shape[:2]
                frame = _resize_to_cell(frame, cell_width, cell_height)
                camera_frames.append(_label_frame(frame, camera.replace(".mp4", "")))

            while len(camera_frames) < 4:
                camera_frames.append(camera_frames[-1].copy())

            top_row = cv2.hconcat(camera_frames[:2])
            bottom_row = cv2.hconcat(camera_frames[2:4])
            composite = cv2.vconcat([top_row, bottom_row])
            composite = _resize_to_max_side(composite, max_side)
            jpeg_bytes = _encode_jpeg_bytes(composite, jpeg_quality)
            if output_dir is not None:
                frame_path = output_dir / f"frame_{sample_idx:03d}.jpg"
                frame_path.write_bytes(jpeg_bytes)
                frame_paths.append(str(frame_path))
            encoded_frames.append(base64.b64encode(jpeg_bytes).decode("utf-8"))
    finally:
        for cap, _camera, _video_path in captures:
            cap.release()

    if not encoded_frames:
        raise ValueError(f"No frames sampled from cameras in {rollout_dir}")

    return encoded_frames, {
        "video_paths": [str(path) for _cap, _camera, path in captures],
        "frame_mode": "synced_camera_composite",
        "frame_counts": frame_counts,
        "frame_rates": frame_rates,
        "sampled_source_frame_count": sample_total,
        "sampled_indices": indices,
        "sample_every_sec": sample_every_sec,
        "output_image_max_side": max_side,
        "frame_paths": frame_paths,
    }


def load_sim_result(rollout_dir: Path, frame_metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    result_path = rollout_dir / "result_info.json"
    if result_path.exists():
        with result_path.open("r", encoding="utf-8") as f:
            result = json.load(f)
        result_info_path = str(result_path)
    elif frame_metadata and isinstance(frame_metadata.get("result_info"), dict):
        result = frame_metadata["result_info"]
        result_info_path = str(frame_metadata.get("result_info_path") or result_path)
    else:
        raise FileNotFoundError(f"No result_info.json found at {result_path}")
    return {
        "sim_score": result.get("score"),
        "sim_success": result.get("success_rate"),
        "result_info_path": result_info_path,
    }


def validate_model_result(result: dict[str, Any]) -> dict[str, Any]:
    allowed_keys = {"score", "success", "reason", "evidence", "metric_breakdown"}
    if not {"score", "success"}.issubset(result):
        raise ValueError(f"Expected at least score/success keys, got: {result}")
    extra_keys = set(result) - allowed_keys
    if extra_keys:
        raise ValueError(f"Unexpected result keys {sorted(extra_keys)}, got: {result}")

    score = float(result["score"])
    success = int(result["success"])
    reason = str(result.get("reason", "")).strip()
    if not 0.0 <= score <= 1.0:
        raise ValueError(f"score must be in [0, 1], got: {score}")
    if success not in (0, 1):
        raise ValueError(f"success must be 0 or 1, got: {success}")

    expected_success = 1 if score == 1.0 else 0
    if success != expected_success:
        raise ValueError(
            f"success must be 1 iff score == 1.0, got score={score}, success={success}"
        )

    parsed = {"score": score, "success": success, "reason": reason}
    if "evidence" in result:
        evidence = result["evidence"]
        if isinstance(evidence, list):
            parsed["evidence"] = [str(item).strip() for item in evidence if str(item).strip()]
        elif evidence is not None:
            parsed["evidence"] = [str(evidence).strip()]
    if "metric_breakdown" in result:
        parsed["metric_breakdown"] = result["metric_breakdown"]
    return parsed


def chat_completions_url(api_base_url: str) -> str:
    base = api_base_url.rstrip("/")
    if base.endswith("/v1/chat/completions"):
        return base
    if base.endswith("/v1"):
        return f"{base}/chat/completions"
    return f"{base}/v1/chat/completions"


def resolve_path(repo_root: Path, path: str | Path) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else repo_root / candidate


def safe_path_parts(path: str) -> list[str]:
    return [safe_name(part) for part in Path(path).parts if part not in ("", ".")]


def post_chat_completion(
    api_base_url: str,
    api_key: str | None,
    payload: dict[str, Any],
    timeout: float,
    retries: int = 0,
    retry_backoff: float = 5.0,
) -> dict[str, Any]:
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = api_key if api_key.startswith("Bearer ") else f"Bearer {api_key}"

    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        chat_completions_url(api_base_url),
        data=data,
        headers=headers,
        method="POST",
    )

    attempts = max(0, retries) + 1
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8")
            return json.loads(body)
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"API HTTP {exc.code}: {error_body}") from exc
        except (TimeoutError, socket.timeout, urllib.error.URLError) as exc:
            if attempt >= attempts:
                raise RuntimeError(
                    f"API request failed after {attempt}/{attempts} attempt(s): {exc}"
                ) from exc
            sleep_sec = max(0.0, retry_backoff) * attempt
            print(
                f"  API request timed out/failed ({attempt}/{attempts}): {exc}; "
                f"retrying same payload in {sleep_sec:.1f}s",
                flush=True,
            )
            if sleep_sec:
                time.sleep(sleep_sec)

    raise RuntimeError("API request failed unexpectedly")


def build_chat_payload(
    model: str,
    content: list[dict[str, Any]],
    temperature: float,
    max_tokens: int,
    response_format: bool,
    token_param: str,
    reasoning_effort: str | None,
    provider_reasoning: str,
    store: bool,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "temperature": temperature,
        "store": store,
    }
    if token_param in ("max_tokens", "both"):
        payload["max_tokens"] = max_tokens
    if token_param in ("max_completion_tokens", "both"):
        payload["max_completion_tokens"] = max_tokens
    if reasoning_effort:
        payload["reasoning_effort"] = reasoning_effort
    if provider_reasoning == "disabled":
        payload["reasoning"] = {"enabled": False}
    elif provider_reasoning == "exclude":
        payload["reasoning"] = {"exclude": True}
    if response_format:
        payload["response_format"] = {"type": "json_object"}
    return payload


def response_has_error(response: dict[str, Any]) -> bool:
    return bool(response.get("error"))


def is_request_too_large_error(exc: Exception) -> bool:
    text = str(exc).lower()
    return (
        "exceeds maximum allowed content length" in text
        or "requestsize(bytes)" in text
        or "request entity too large" in text
        or "payload too large" in text
    )


def build_rollout_content(
    task_prompt: str,
    frames: list[str],
    image_detail: str,
    visual_note: str,
) -> list[dict[str, Any]]:
    content: list[dict[str, Any]] = [
        {"type": "text", "text": task_prompt},
        {"type": "text", "text": visual_note},
    ]
    for idx, frame in enumerate(frames):
        content.append({"type": "text", "text": f"frame_{idx:03d}"})
        content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{frame}",
                    "detail": image_detail,
                },
            }
        )
    return content


def extract_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(text[start : end + 1])

    raise ValueError(f"Model response does not contain a JSON object: {text}")


def chat_response_text(response: dict[str, Any]) -> str:
    error = response.get("error")
    if isinstance(error, dict):
        code = error.get("code")
        message = error.get("message")
        raise RuntimeError(f"API returned error: code={code}, message={message}")
    if error:
        raise RuntimeError(f"API returned error: {error}")

    try:
        choice = response["choices"][0]
        message = choice["message"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError(f"Unexpected chat completion response: {response}") from exc

    content = message.get("content")
    if isinstance(content, str):
        if content.strip():
            return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(str(item.get("text", "")))
        text = "".join(parts)
        if text.strip():
            return text

    for key in ("reasoning_content", "tool_call_id", "name"):
        value = message.get(key)
        if isinstance(value, str) and value.strip():
            return value

    tool_calls = message.get("tool_calls")
    if isinstance(tool_calls, list):
        for tool_call in tool_calls:
            function = tool_call.get("function") if isinstance(tool_call, dict) else None
            arguments = function.get("arguments") if isinstance(function, dict) else None
            if isinstance(arguments, str) and arguments.strip():
                return arguments

    reasoning = message.get("reasoning")
    if isinstance(reasoning, str) and reasoning.strip():
        try:
            extract_json_object(reasoning)
        except ValueError:
            if choice.get("finish_reason") == "length":
                raise ValueError(
                    "Chat completion spent the output budget on provider reasoning and returned no JSON content. "
                    "Try --provider-reasoning disabled, --provider-reasoning exclude, or a larger --max-tokens."
                )
        else:
            return reasoning

    raise ValueError(
        "Chat completion response message content is empty. "
        f"finish_reason={choice.get('finish_reason')}, response={json.dumps(response, ensure_ascii=False)[:2000]}"
    )


def write_api_debug(
    repo_root: Path,
    task: RolloutTask,
    model: str,
    payload: dict[str, Any],
    response: dict[str, Any],
    suffix: str,
) -> Path:
    debug_dir = repo_root / "outputs" / "api_debug"
    debug_dir.mkdir(parents=True, exist_ok=True)
    safe_model = safe_name(model)
    safe_episode = safe_name(task.episode_path or task.episode_id)
    debug_path = debug_dir / f"{task.task_id}_{safe_episode}_{safe_model}_{suffix}.json"
    debug_path.write_text(
        json.dumps(
            {"payload_without_images": payload | {"messages": "<omitted>"}, "response": response},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return debug_path


def debug_paths_for_task(repo_root: Path, task: RolloutTask, model: str) -> list[Path]:
    debug_dir = repo_root / "outputs" / "api_debug"
    safe_model = safe_name(model)
    safe_episode = safe_name(task.episode_path or task.episode_id)
    base = debug_dir / f"{task.task_id}_{safe_episode}_{safe_model}.json"
    candidates = [
        base,
        debug_dir / f"{task.task_id}_{safe_episode}_{safe_model}_fallback.json",
    ]
    candidates.extend(
        sorted(debug_dir.glob(f"{task.task_id}_{safe_episode}_{safe_model}_*.json"))
    )
    if task.source == "rollout_video":
        legacy_base = debug_dir / f"{task.task_id}_{task.episode_id}_{safe_model}.json"
        candidates.extend(
            [
                legacy_base,
                debug_dir / f"{task.task_id}_{task.episode_id}_{safe_model}_fallback.json",
                *sorted(debug_dir.glob(f"{task.task_id}_{task.episode_id}_{safe_model}_*.json")),
            ]
        )
    seen = set()
    unique_candidates = []
    for path in candidates:
        if path not in seen:
            seen.add(path)
            unique_candidates.append(path)
    return unique_candidates


def load_row_from_api_debug(
    task: RolloutTask,
    repo_root: Path,
    cameras: list[str],
    frames_root: Path,
    model: str,
    sample_every_sec: float,
    image_detail: str,
    api_base_url: str,
    max_images: int | None,
) -> dict[str, Any] | None:
    rollout_dir = resolve_path(repo_root, task.rollout_dir) if task.rollout_dir else repo_root
    frame_dir = task_frame_dir(frames_root, task, cameras)
    metadata_path = frame_dir / "metadata.json"
    frame_metadata = (
        json.loads(metadata_path.read_text(encoding="utf-8"))
        if metadata_path.exists()
        else {
            "video_paths": [str(rollout_dir / camera) for camera in cameras],
            "frame_mode": "api_debug_replay",
            "frame_counts": {},
        }
    )
    source_num_frames = None
    sent_num_frames = None
    selected_frame_indices = None
    if frame_dir.exists():
        try:
            cached_frames = load_cached_frames(frame_dir)
            source_num_frames = len(cached_frames)
            _, selected_frame_indices = downsample_sequence(cached_frames, max_images)
            sent_num_frames = len(selected_frame_indices)
        except ValueError:
            pass

    for debug_path in debug_paths_for_task(repo_root, task, model):
        if not debug_path.exists():
            continue
        try:
            debug_data = json.loads(debug_path.read_text(encoding="utf-8"))
            response = debug_data["response"]
            raw_text = chat_response_text(response).strip()
            parsed = validate_model_result(extract_json_object(raw_text))
        except Exception:
            continue

        sim_result = load_sim_result(rollout_dir, frame_metadata)
        return {
            "task_id": task.task_id,
            "episode_id": task.episode_id,
            "episode_path": task.episode_path or f"{task.task_id}/{task.episode_id}",
            "source": task.source,
            "rollout_dir": task.rollout_dir,
            "frame_dir": task.frame_dir,
            "video_paths": frame_metadata.get("video_paths", []),
            "cameras": cameras,
            "frame_mode": frame_metadata.get("frame_mode", "api_debug_replay"),
            "frame_counts": frame_metadata.get("frame_counts", {}),
            "model": model,
            "num_frames": sent_num_frames,
            "source_num_frames": source_num_frames,
            "max_images": max_images,
            "selected_frame_indices": selected_frame_indices,
            "sample_every_sec": sample_every_sec,
            "image_detail": image_detail,
            "api_base_url": api_base_url,
            "store": None,
            "response_format": None,
            "provider_reasoning": None,
            "token_param": None,
            "max_tokens": None,
            "fallback_used": debug_path.name.endswith("_fallback.json"),
            "request_size_retry_used": None,
            "from_api_debug": True,
            "api_debug_path": str(debug_path),
            "vlm_score": parsed["score"],
            "vlm_success": parsed["success"],
            "vlm_reason": parsed["reason"],
            "vlm_evidence": parsed.get("evidence"),
            "vlm_metric_breakdown": parsed.get("metric_breakdown"),
            **sim_result,
            "agreement": int(parsed["success"] == sim_result["sim_success"]),
            "raw_response": raw_text,
            "usage": response.get("usage"),
        }

    return None


def discover_rollout_tasks(repo_root: Path) -> list[RolloutTask]:
    rollout_root = repo_root / "rollout_video"
    tasks = []
    for result_path in sorted(rollout_root.glob("*_test_mini/**/result_info.json")):
        rollout_dir = result_path.parent
        task_dir = result_path.relative_to(rollout_root).parts[0]
        task_id = task_dir.removesuffix("_test_mini")
        prompt = TASK_PROMPTS.get(task_id)
        if prompt is None:
            raise ValueError(
                f"No prompt registered for task_id={task_id} from {result_path}"
            )
        episode_parts = rollout_dir.relative_to(rollout_root / task_dir).parts
        episode_id = episode_parts[-1]
        tasks.append(
            RolloutTask(
                task_id=task_id,
                episode_id=episode_id,
                rollout_dir=str(rollout_dir.relative_to(repo_root)),
                prompt=prompt,
                episode_path=f"{task_id}/{episode_id}",
            )
        )
    return tasks


def discover_preprocessed_tasks(repo_root: Path, frames_root: Path, cameras: list[str]) -> list[RolloutTask]:
    key = frame_camera_key(cameras)
    tasks = []
    for metadata_path in sorted(frames_root.glob(f"**/{key}/metadata.json")):
        frame_dir = metadata_path.parent
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid metadata JSON: {metadata_path}") from exc

        task_id = str(metadata.get("task_id") or frame_dir.parent.parent.name)
        prompt = TASK_PROMPTS.get(task_id)
        if prompt is None:
            continue

        episode_id = str(metadata.get("episode_id") or frame_dir.parent.name)
        rollout_dir = str(metadata.get("rollout_dir") or "")
        try:
            episode_path = str(frame_dir.parent.relative_to(frames_root))
        except ValueError:
            episode_path = f"{task_id}/{episode_id}"

        tasks.append(
            RolloutTask(
                task_id=task_id,
                episode_id=episode_id,
                rollout_dir=rollout_dir,
                prompt=prompt,
                frame_dir=str(frame_dir),
                episode_path=episode_path,
                source="preprocessed_frames",
            )
        )
    return tasks


def frame_camera_key(cameras: list[str]) -> str:
    return "single_" + cameras[0].replace(".mp4", "") if len(cameras) == 1 else "four_camera"


def task_frame_dir(frames_root: Path, task: RolloutTask, cameras: list[str]) -> Path:
    if task.frame_dir:
        return resolve_path(Path.cwd(), task.frame_dir)
    return frames_root / task.task_id / task.episode_id / frame_camera_key(cameras)


def load_cached_frames(frame_dir: Path) -> list[str]:
    frame_paths = sorted(frame_dir.glob("frame_*.jpg"))
    if not frame_paths:
        raise ValueError(f"No cached frames found in {frame_dir}")
    return [
        base64.b64encode(frame_path.read_bytes()).decode("utf-8")
        for frame_path in frame_paths
    ]


def downsample_sequence(items: list[Any], max_items: int | None) -> tuple[list[Any], list[int]]:
    if max_items is None or max_items <= 0 or len(items) <= max_items:
        return items, list(range(len(items)))
    if max_items == 1:
        return [items[-1]], [len(items) - 1]

    indices = [
        round(i * (len(items) - 1) / (max_items - 1))
        for i in range(max_items)
    ]
    return [items[idx] for idx in indices], indices


def preprocess_task_frames(
    task: RolloutTask,
    repo_root: Path,
    cameras: list[str],
    sample_every_sec: float,
    num_frames: int | None,
    jpeg_quality: int,
    frames_root: Path,
    output_image_max_side: int | None,
) -> dict[str, Any]:
    rollout_dir = resolve_path(repo_root, task.rollout_dir)
    frame_dir = task_frame_dir(frames_root, task, cameras)
    frames, frame_metadata = sample_synced_camera_frames(
        rollout_dir,
        cameras,
        sample_every_sec,
        num_frames,
        jpeg_quality,
        output_dir=frame_dir,
        max_side=output_image_max_side,
    )
    metadata = {
        "task_id": task.task_id,
        "episode_id": task.episode_id,
        "rollout_dir": task.rollout_dir,
        "cameras": cameras,
        "num_frames": len(frames),
        "frames_dir": str(frame_dir),
        "output_image_max_side": output_image_max_side,
        **frame_metadata,
    }
    (frame_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return metadata


def score_task(
    task: RolloutTask,
    repo_root: Path,
    cameras: list[str],
    sample_every_sec: float,
    num_frames: int | None,
    jpeg_quality: int,
    model: str,
    frames_root: Path,
    use_preprocessed: bool,
    image_detail: str,
    api_base_url: str,
    api_key: str | None,
    temperature: float,
    max_tokens: int,
    token_param: str,
    reasoning_effort: str | None,
    use_response_format: bool,
    provider_reasoning: str,
    store: bool,
    timeout: float,
    api_retries: int,
    api_retry_backoff: float,
    max_images: int | None,
    request_image_max_side: int | None,
    request_jpeg_quality: int | None,
    explanation_mode: str,
) -> dict[str, Any]:
    rollout_dir = resolve_path(repo_root, task.rollout_dir) if task.rollout_dir else repo_root
    frame_dir = task_frame_dir(frames_root, task, cameras)
    if use_preprocessed:
        frames = load_cached_frames(frame_dir)
        metadata_path = frame_dir / "metadata.json"
        frame_metadata = (
            json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata_path.exists()
            else {
                "video_paths": [str(rollout_dir / camera) for camera in cameras],
                "frame_mode": "cached_preprocessed_frames",
                "frame_counts": {},
            }
        )
    else:
        frames, frame_metadata = sample_synced_camera_frames(
            rollout_dir,
            cameras,
            sample_every_sec,
            num_frames,
            jpeg_quality,
        )

    original_num_frames = len(frames)
    frames, selected_frame_indices = downsample_sequence(frames, max_images)
    if len(frames) < original_num_frames:
        print(
            f"  downsampled request images: {original_num_frames} -> {len(frames)} "
            f"(max_images={max_images})"
        )
    request_frames, compression_stats = compress_encoded_frames(
        frames,
        request_image_max_side,
        request_jpeg_quality,
    )
    if compression_stats["enabled"]:
        before_mb = compression_stats["base64_chars_before"] / 1024 / 1024
        after_mb = compression_stats["base64_chars_after"] / 1024 / 1024
        print(
            f"  compressed request images: base64 {before_mb:.1f}MB -> {after_mb:.1f}MB "
            f"(max_side={compression_stats['max_side']}, quality={compression_stats['jpeg_quality']})"
        )

    visual_note = (
        "The following input images are sampled in chronological order. "
        "Each image is a synchronized 2x2 multi-camera composite unless only one "
        "camera was requested. If the rollout contains more frames than the API "
        "allows, these input images are uniformly downsampled while preserving "
        "chronological order."
    )
    task_prompt = task_prompt_with_explanation(task.prompt, explanation_mode)
    content = build_rollout_content(task_prompt, request_frames, image_detail, visual_note)
    request_size_retry_used = False

    payload = build_chat_payload(
        model=model,
        content=content,
        temperature=temperature,
        max_tokens=max_tokens,
        response_format=use_response_format,
        token_param=token_param,
        reasoning_effort=reasoning_effort,
        provider_reasoning=provider_reasoning,
        store=store,
    )
    while True:
        try:
            response = post_chat_completion(
                api_base_url=api_base_url,
                api_key=api_key,
                payload=payload,
                timeout=timeout,
                retries=api_retries,
                retry_backoff=api_retry_backoff,
            )
            break
        except RuntimeError as exc:
            if not is_request_too_large_error(exc) or len(frames) <= 1:
                raise
            request_size_retry_used = True
            next_max_images = max(1, len(frames) // 2)
            previous_num_frames = len(frames)
            frames, relative_indices = downsample_sequence(frames, next_max_images)
            selected_frame_indices = [
                selected_frame_indices[idx] for idx in relative_indices
            ]
            request_frames, compression_stats = compress_encoded_frames(
                frames,
                request_image_max_side,
                request_jpeg_quality,
            )
            content = build_rollout_content(task_prompt, request_frames, image_detail, visual_note)
            payload = build_chat_payload(
                model=model,
                content=content,
                temperature=temperature,
                max_tokens=max_tokens,
                response_format=use_response_format,
                token_param=token_param,
                reasoning_effort=reasoning_effort,
                provider_reasoning=provider_reasoning,
                store=store,
            )
            print(
                f"  request too large; retrying with {len(frames)} images "
                f"({previous_num_frames} -> {len(frames)})"
            )
    actual_provider_reasoning = provider_reasoning
    actual_token_param = token_param

    if provider_reasoning != "omit" and response_has_error(response):
        write_api_debug(
            repo_root,
            task,
            model,
            payload,
            response,
            f"provider_reasoning_{provider_reasoning}_error",
        )
        print(
            f"  provider rejected --provider-reasoning {provider_reasoning}; "
            "retrying with provider_reasoning=omit"
        )
        payload = build_chat_payload(
            model=model,
            content=content,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format=use_response_format,
            token_param=token_param,
            reasoning_effort=reasoning_effort,
            provider_reasoning="omit",
            store=store,
        )
        response = post_chat_completion(
            api_base_url=api_base_url,
            api_key=api_key,
            payload=payload,
            timeout=timeout,
            retries=api_retries,
            retry_backoff=api_retry_backoff,
        )
        actual_provider_reasoning = f"omit_after_{provider_reasoning}_error"

    if token_param == "max_completion_tokens" and response_has_error(response):
        write_api_debug(
            repo_root,
            task,
            model,
            payload,
            response,
            "max_completion_tokens_error",
        )
        print("  provider rejected max_completion_tokens; retrying with max_tokens")
        payload = build_chat_payload(
            model=model,
            content=content,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format=use_response_format,
            token_param="max_tokens",
            reasoning_effort=reasoning_effort,
            provider_reasoning="omit" if actual_provider_reasoning.startswith("omit_after_") else provider_reasoning,
            store=store,
        )
        response = post_chat_completion(
            api_base_url=api_base_url,
            api_key=api_key,
            payload=payload,
            timeout=timeout,
            retries=api_retries,
            retry_backoff=api_retry_backoff,
        )
        actual_token_param = "max_tokens_after_max_completion_tokens_error"

    debug_dir = repo_root / "outputs" / "api_debug"
    debug_dir.mkdir(parents=True, exist_ok=True)
    safe_model = safe_name(model)
    safe_episode = safe_name(task.episode_path or task.episode_id)
    debug_path = debug_dir / f"{task.task_id}_{safe_episode}_{safe_model}.json"
    debug_path.write_text(
        json.dumps(
            {"payload_without_images": payload | {"messages": "<omitted>"}, "response": response},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    fallback_used = False
    raw_text = chat_response_text(response).strip()
    parsed = validate_model_result(extract_json_object(raw_text))
    sim_result = load_sim_result(rollout_dir, frame_metadata)

    return {
        "task_id": task.task_id,
        "episode_id": task.episode_id,
        "episode_path": task.episode_path or f"{task.task_id}/{task.episode_id}",
        "source": task.source,
        "rollout_dir": task.rollout_dir,
        "frame_dir": str(frame_dir),
        "video_paths": frame_metadata["video_paths"],
        "cameras": cameras,
        "frame_mode": frame_metadata["frame_mode"],
        "frame_counts": frame_metadata["frame_counts"],
        "model": model,
        "num_frames": len(frames),
        "source_num_frames": original_num_frames,
        "max_images": max_images,
        "request_image_max_side": request_image_max_side,
        "request_jpeg_quality": request_jpeg_quality,
        "request_image_compression": compression_stats,
        "selected_frame_indices": selected_frame_indices,
        "sample_every_sec": sample_every_sec,
        "image_detail": image_detail,
        "explanation_mode": explanation_mode,
        "api_base_url": api_base_url,
        "timeout": timeout,
        "api_retries": api_retries,
        "api_retry_backoff": api_retry_backoff,
        "store": store,
        "response_format": "json_object" if use_response_format else "none",
        "provider_reasoning": actual_provider_reasoning,
        "token_param": actual_token_param,
        "max_tokens": max_tokens,
        "fallback_used": fallback_used,
        "request_size_retry_used": request_size_retry_used,
        "from_api_debug": False,
        "vlm_score": parsed["score"],
        "vlm_success": parsed["success"],
        "vlm_reason": parsed["reason"],
        "vlm_evidence": parsed.get("evidence"),
        "vlm_metric_breakdown": parsed.get("metric_breakdown"),
        **sim_result,
        "agreement": int(parsed["success"] == sim_result["sim_success"]),
        "raw_response": raw_text,
        "usage": response.get("usage"),
    }


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def episode_result_path(root: Path, model: str, row: dict[str, Any]) -> Path:
    episode_path = str(row.get("episode_path") or f"{row.get('task_id')}/{row.get('episode_id')}")
    return root / safe_name(model) / Path(*safe_path_parts(episode_path)) / "result.json"


def write_episode_result(root: Path | None, model: str, row: dict[str, Any]) -> None:
    if root is None:
        return
    path = episode_result_path(root, model, row)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def markdown_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_report(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    scored_rows = [row for row in rows if "error" not in row]
    agreement_count = sum(row["agreement"] for row in scored_rows)
    agreement_rate = agreement_count / len(scored_rows) if scored_rows else 0.0

    lines = [
        "# GPT Rollout Score Report",
        "",
        f"- num_rollouts: {len(rows)}",
        f"- scored_rollouts: {len(scored_rows)}",
        f"- failed_rollouts: {len(rows) - len(scored_rows)}",
        f"- agreement_rate: {agreement_rate:.3f}",
        "",
        "| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |",
        "|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|",
    ]

    for row in scored_rows:
        formatted_row = {
            **row,
            "vlm_reason": markdown_cell(row.get("vlm_reason", "")),
        }
        lines.append(
            "| {model} | {task_id} | {episode_id} | {sim_score} | {sim_success} | "
            "{vlm_score:.6g} | {vlm_success} | {agreement} | {vlm_reason} | {source_num_frames} | "
            "{num_frames} | {max_images} | {frame_mode} |".format(**formatted_row)
        )

    failed_rows = [row for row in rows if "error" in row]
    if failed_rows:
        lines.extend(["", "## Errors", ""])
        for row in failed_rows:
            lines.append(f"- {row['task_id']}/{row['episode_id']}: {row['error']}")

    mismatches = [row for row in scored_rows if not row["agreement"]]
    if mismatches:
        lines.extend(["", "## Mismatches", ""])
        for row in mismatches:
            lines.append(
                f"- {row['task_id']}/{row['episode_id']}: sim_success={row['sim_success']}, "
                f"vlm_success={row['vlm_success']}, vlm_score={row['vlm_score']}"
            )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def score_task_with_options(
    task: RolloutTask,
    args: argparse.Namespace,
    repo_root: Path,
    cameras: list[str],
    frames_root: Path,
    episode_output_root: Path | None,
) -> tuple[dict[str, Any], str]:
    try:
        if args.use_api_debug:
            row = load_row_from_api_debug(
                task=task,
                repo_root=repo_root,
                cameras=cameras,
                frames_root=frames_root,
                model=args.model,
                sample_every_sec=args.sample_every_sec,
                image_detail=args.image_detail,
                api_base_url=args.api_base_url,
                max_images=args.max_images if args.max_images > 0 else None,
            )
            if row is not None:
                write_episode_result(episode_output_root, args.model, row)
                return (
                    row,
                    f"reused api_debug vlm_score={row['vlm_score']} "
                    f"vlm_success={row['vlm_success']} sim_success={row['sim_success']} "
                    f"agreement={row['agreement']}",
                )

        row = score_task(
            task=task,
            repo_root=repo_root,
            cameras=cameras,
            sample_every_sec=args.sample_every_sec,
            num_frames=args.num_frames,
            jpeg_quality=args.jpeg_quality,
            model=args.model,
            frames_root=frames_root,
            use_preprocessed=args.use_preprocessed,
            image_detail=args.image_detail,
            api_base_url=args.api_base_url,
            api_key=args.api_key,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            token_param=args.token_param,
            reasoning_effort=None if args.reasoning_effort == "none" else args.reasoning_effort,
            use_response_format=args.response_format == "json_object",
            provider_reasoning=args.provider_reasoning,
            store=args.store,
            timeout=args.timeout,
            api_retries=args.api_retries,
            api_retry_backoff=args.api_retry_backoff,
            max_images=args.max_images if args.max_images > 0 else None,
            request_image_max_side=args.request_image_max_side
            if args.request_image_max_side > 0
            else None,
            request_jpeg_quality=args.request_jpeg_quality
            if args.request_jpeg_quality > 0
            else None,
            explanation_mode=args.explanation_mode,
        )
    except Exception as exc:
        if not args.continue_on_error:
            raise
        row = {
            "task_id": task.task_id,
            "episode_id": task.episode_id,
            "episode_path": task.episode_path or f"{task.task_id}/{task.episode_id}",
            "source": task.source,
            "rollout_dir": task.rollout_dir,
            "frame_dir": task.frame_dir,
            "model": args.model,
            "api_base_url": args.api_base_url,
            "timeout": args.timeout,
            "api_retries": args.api_retries,
            "api_retry_backoff": args.api_retry_backoff,
            "store": args.store,
            "response_format": args.response_format,
            "provider_reasoning": args.provider_reasoning,
            "max_images": args.max_images if args.max_images > 0 else None,
            "request_image_max_side": args.request_image_max_side
            if args.request_image_max_side > 0
            else None,
            "request_jpeg_quality": args.request_jpeg_quality
            if args.request_jpeg_quality > 0
            else None,
            "explanation_mode": args.explanation_mode,
            "image_detail": args.image_detail,
            "error": str(exc),
            "agreement": 0,
        }
        write_episode_result(episode_output_root, args.model, row)
        return row, f"error={exc}"

    write_episode_result(episode_output_root, args.model, row)
    return (
        row,
        f"vlm_score={row['vlm_score']} vlm_success={row['vlm_success']} "
        f"sim_success={row['sim_success']} agreement={row['agreement']}",
    )


def select_tasks(
    discovered_tasks: list[RolloutTask],
    task_ids: list[str] | None,
    episode_ids: list[str] | None,
) -> list[RolloutTask]:
    selected = discovered_tasks
    if task_ids:
        requested = set(task_ids)
        available = {task.task_id for task in discovered_tasks}
        missing = sorted(requested - available)
        if missing:
            raise ValueError(f"Unknown task id(s): {', '.join(missing)}")
        selected = [task for task in selected if task.task_id in requested]

    if episode_ids:
        requested = set(episode_ids)
        available = {task.episode_id for task in selected}
        missing = sorted(requested - available)
        if missing:
            raise ValueError(f"Unknown episode id(s): {', '.join(missing)}")
        selected = [task for task in selected if task.episode_id in requested]

    return selected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        default=os.environ.get("VLM_MODEL", os.environ.get("OPENAI_VLM_MODEL", "gpt-5")),
        help="Vision-capable model name.",
    )
    parser.add_argument(
        "--api-base-url",
        default=os.environ.get("VLM_API_BASE_URL", DEFAULT_API_BASE_URL),
        help="API base URL or full /v1/chat/completions URL.",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("VLM_API_KEY", os.environ.get("OPENAI_API_KEY")),
        help="Bearer token. Can also be set with VLM_API_KEY or OPENAI_API_KEY.",
    )
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument(
        "--token-param",
        choices=["max_completion_tokens", "max_tokens", "both"],
        default="max_completion_tokens",
        help="Completion budget field to send. Default is max_completion_tokens for gpt-5 style models.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high"],
        default="low",
        help="Reasoning effort for reasoning models. Use none to omit this field.",
    )
    parser.add_argument(
        "--response-format",
        choices=["json_object", "none"],
        default="json_object",
        help="Structured response_format field to send. Use none for providers that reject json_object.",
    )
    parser.add_argument(
        "--provider-reasoning",
        choices=["omit", "disabled", "exclude"],
        default="omit",
        help=(
            "Optional provider-specific reasoning control. "
            "disabled sends reasoning.enabled=false; exclude sends reasoning.exclude=true."
        ),
    )
    parser.add_argument(
        "--explanation-mode",
        choices=["brief", "evidence"],
        default="brief",
        help=(
            "brief keeps the original score/success/reason JSON. "
            "evidence asks the model to also output visible evidence and metric_breakdown."
        ),
    )
    parser.add_argument(
        "--max-images",
        type=int,
        default=50,
        help="Maximum images per API request. Use <=0 to disable request downsampling.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=300.0,
        help="HTTP request timeout in seconds.",
    )
    parser.add_argument(
        "--api-retries",
        type=int,
        default=2,
        help="Retry the exact same API payload this many times after timeout/network errors. Default: 2.",
    )
    parser.add_argument(
        "--api-retry-backoff",
        type=float,
        default=10.0,
        help="Base seconds to wait between API retries; wait time is backoff * attempt. Default: 10.",
    )
    parser.add_argument(
        "--store",
        action="store_true",
        help="Allow the provider to store request/response history. Default is false.",
    )
    parser.add_argument(
        "--num-frames",
        type=int,
        default=None,
        help="Uniformly sample a fixed number of frames. If omitted, sample by seconds.",
    )
    parser.add_argument(
        "--sample-every-sec",
        type=float,
        default=1.0,
        help="Sample one synchronized frame every N seconds. Default: 1.0.",
    )
    parser.add_argument("--jpeg-quality", type=int, default=85)
    parser.add_argument(
        "--request-image-max-side",
        type=int,
        default=768,
        help=(
            "Resize images before sending to the API so their longest side is at most this many pixels. "
            "Use 0 to keep cached image resolution."
        ),
    )
    parser.add_argument(
        "--request-jpeg-quality",
        type=int,
        default=70,
        help="Re-encode request images with this JPEG quality, 1-100. Use 0 to keep existing bytes.",
    )
    parser.add_argument(
        "--output-image-max-side",
        type=int,
        default=0,
        help="Resize images written by --preprocess-only so their longest side is at most this many pixels.",
    )
    parser.add_argument(
        "--image-detail",
        default="high",
        choices=["low", "high", "auto", "original"],
        help="Image detail level sent in image_url payloads. Default: high.",
    )
    parser.add_argument(
        "--camera",
        default=None,
        help="Use a single camera file, for example top_camera.mp4. Overrides --cameras.",
    )
    parser.add_argument(
        "--cameras",
        nargs="+",
        default=DEFAULT_CAMERAS,
        help="Camera files to synchronize and stitch. Defaults to all four cameras.",
    )
    parser.add_argument(
        "--task",
        action="append",
        dest="tasks",
        help="Task id to score. Can be passed multiple times. Defaults to all discovered episodes.",
    )
    parser.add_argument(
        "--episode",
        action="append",
        dest="episodes",
        help="Episode id to score, for example 001 or 002. Can be passed multiple times.",
    )
    parser.add_argument(
        "--output-jsonl",
        default=None,
        help="Output JSONL path. Defaults to outputs/{model}_scores.jsonl.",
    )
    parser.add_argument(
        "--report-md",
        default=None,
        help="Output Markdown report path. Defaults to outputs/{model}_report.md.",
    )
    parser.add_argument(
        "--frames-root",
        default="outputs/preprocessed_frames",
        help="Preprocessed frame root. For eBench use outputs/ebench_preprocessed_frames/<run> or outputs/ebench_preprocessed_frames.",
    )
    parser.add_argument(
        "--task-source",
        choices=["rollout_video", "preprocessed"],
        default="rollout_video",
        help="Discover tasks from rollout_video or recursively from --frames-root metadata.",
    )
    parser.add_argument(
        "--episode-output-root",
        default="outputs/episode_scores",
        help="Write one result.json per episode under this root. Use none to disable.",
    )
    parser.add_argument(
        "--preprocess-only",
        action="store_true",
        help="Only write sampled composite images to --frames-root; do not call the API.",
    )
    parser.add_argument(
        "--use-preprocessed",
        action="store_true",
        help="Read cached frame_*.jpg from --frames-root instead of sampling videos.",
    )
    parser.add_argument(
        "--use-api-debug",
        action="store_true",
        help="Reuse existing outputs/api_debug responses when available instead of calling the API.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate local video/result paths without calling the API.",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Record failed API calls as error rows and continue scoring later episodes.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of concurrent API scoring workers. Default: 1.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent
    cameras = [args.camera] if args.camera else args.cameras
    frames_root = resolve_path(repo_root, args.frames_root)
    discovered_tasks = (
        discover_preprocessed_tasks(repo_root, frames_root, cameras)
        if args.task_source == "preprocessed"
        else discover_rollout_tasks(repo_root)
    )
    tasks = select_tasks(discovered_tasks, args.tasks, args.episodes)
    model_name = safe_name(args.model)
    output_jsonl = args.output_jsonl or f"outputs/{model_name}_scores.jsonl"
    report_md = args.report_md or f"outputs/{model_name}_report.md"
    episode_output_root = (
        None
        if str(args.episode_output_root).lower() in ("", "none", "null", "false", "0")
        else resolve_path(repo_root, args.episode_output_root)
    )

    if args.dry_run:
        for task in tasks:
            rollout_dir = resolve_path(repo_root, task.rollout_dir) if task.rollout_dir else None
            video_paths = [rollout_dir / camera for camera in cameras] if rollout_dir is not None else []
            result_path = rollout_dir / "result_info.json" if rollout_dir is not None else None
            print(
                json.dumps(
                    {
                        "task_id": task.task_id,
                        "episode_id": task.episode_id,
                        "episode_path": task.episode_path,
                        "source": task.source,
                        "cameras": cameras,
                        "video_paths": [str(path) for path in video_paths] if rollout_dir is not None else [],
                        "videos_exist": {
                            camera: path.exists()
                            for camera, path in zip(cameras, video_paths, strict=True)
                        }
                        if rollout_dir is not None
                        else {},
                        "result_exists": result_path.exists() if result_path is not None else None,
                        "result_info_path": str(result_path) if result_path is not None else None,
                        "frames_dir": str(task_frame_dir(frames_root, task, cameras)),
                    },
                    ensure_ascii=False,
                )
            )
        return

    if args.preprocess_only:
        for task in tasks:
            print(f"Preprocessing {task.task_id}/{task.episode_id}...")
            metadata = preprocess_task_frames(
                task=task,
                repo_root=repo_root,
                cameras=cameras,
                sample_every_sec=args.sample_every_sec,
                num_frames=args.num_frames,
                jpeg_quality=args.jpeg_quality,
                frames_root=frames_root,
                output_image_max_side=args.output_image_max_side
                if args.output_image_max_side > 0
                else None,
            )
            print(f"  wrote {metadata['num_frames']} frames to {metadata['frames_dir']}")
        return

    worker_count = max(1, args.workers)
    total_tasks = len(tasks)
    rows: list[dict[str, Any] | None] = [None] * len(tasks)
    print(f"Total rollouts to score: {total_tasks}")
    if worker_count == 1:
        for idx, task in enumerate(tasks):
            print(f"[{idx + 1}/{total_tasks}] Scoring {task.task_id}/{task.episode_id} with {args.model}...")
            row, message = score_task_with_options(
                task=task,
                args=args,
                repo_root=repo_root,
                cameras=cameras,
                frames_root=frames_root,
                episode_output_root=episode_output_root,
            )
            rows[idx] = row
            print(f"[{idx + 1}/{total_tasks}] {task.task_id}/{task.episode_id}: {message}", flush=True)
    else:
        print(f"Scoring {total_tasks} rollouts with {args.model} using {worker_count} workers...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
            future_to_item = {
                executor.submit(
                    score_task_with_options,
                    task,
                    args,
                    repo_root,
                    cameras,
                    frames_root,
                    episode_output_root,
                ): (idx, task)
                for idx, task in enumerate(tasks)
            }
            completed = 0
            for future in concurrent.futures.as_completed(future_to_item):
                idx, task = future_to_item[future]
                row, message = future.result()
                rows[idx] = row
                completed += 1
                print(
                    f"[{completed}/{total_tasks}] {task.task_id}/{task.episode_id}: {message}",
                    flush=True,
                )

    final_rows = [row for row in rows if row is not None]
    write_jsonl(repo_root / output_jsonl, final_rows)
    write_report(repo_root / report_md, final_rows)
    print(f"Wrote {output_jsonl}")
    print(f"Wrote {report_md}")


if __name__ == "__main__":
    main()
