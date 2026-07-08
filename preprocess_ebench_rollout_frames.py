#!/usr/bin/env python3
"""Preprocess ebench rollout videos into synchronized multi-camera frame grids."""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from score_rollouts import DEFAULT_CAMERAS, sample_synced_camera_frames


DEFAULT_TASKS = [
    "apple_to_fruit_bowl",
    "bookmark_on_book",
    "collect_coffee_beans",
    "detergent",
    "put_glass_in_glassbox",
    "utensils_to_holder",
]


@dataclass(frozen=True)
class EbenchEpisode:
    task_id: str
    task_dir: str
    episode_id: str
    rollout_dir: Path


def task_id_from_dir_name(name: str) -> str:
    return name.removesuffix("_test_mini")


def camera_key(cameras: list[str]) -> str:
    return "single_" + cameras[0].replace(".mp4", "") if len(cameras) == 1 else "four_camera"


def discover_episodes(input_root: Path, task_ids: set[str]) -> list[EbenchEpisode]:
    episodes = []
    for result_path in sorted(input_root.glob("**/*_test_mini/*/result_info.json")):
        rollout_dir = result_path.parent
        task_dir = rollout_dir.parent.name
        task_id = task_id_from_dir_name(task_dir)
        if task_id not in task_ids:
            continue
        episodes.append(
            EbenchEpisode(
                task_id=task_id,
                task_dir=task_dir,
                episode_id=rollout_dir.name,
                rollout_dir=rollout_dir,
            )
        )
    return episodes


def output_frame_dir(output_root: Path, run_name: str, episode: EbenchEpisode, cameras: list[str]) -> Path:
    return output_root / run_name / episode.task_id / episode.episode_id / camera_key(cameras)


def load_result_info(rollout_dir: Path) -> dict[str, Any]:
    result_path = rollout_dir / "result_info.json"
    if not result_path.exists():
        return {}
    return json.loads(result_path.read_text(encoding="utf-8"))


def preprocess_episode(
    episode: EbenchEpisode,
    input_root: Path,
    output_root: Path,
    run_name: str,
    cameras: list[str],
    num_frames: int,
    sample_every_sec: float,
    jpeg_quality: int,
    output_image_max_side: int | None,
    overwrite: bool,
) -> dict[str, Any]:
    frame_dir = output_frame_dir(output_root, run_name, episode, cameras)
    if frame_dir.exists() and overwrite:
        shutil.rmtree(frame_dir)
    if frame_dir.exists() and list(frame_dir.glob("frame_*.jpg")):
        metadata_path = frame_dir / "metadata.json"
        if metadata_path.exists():
            return json.loads(metadata_path.read_text(encoding="utf-8")) | {"skipped_existing": True}
        return {
            "task_id": episode.task_id,
            "episode_id": episode.episode_id,
            "frames_dir": str(frame_dir),
            "num_frames": len(list(frame_dir.glob("frame_*.jpg"))),
            "skipped_existing": True,
        }

    encoded_frames, frame_metadata = sample_synced_camera_frames(
        rollout_dir=episode.rollout_dir,
        cameras=cameras,
        sample_every_sec=sample_every_sec,
        num_frames=num_frames,
        jpeg_quality=jpeg_quality,
        output_dir=frame_dir,
        max_side=output_image_max_side,
    )
    result_info = load_result_info(episode.rollout_dir)
    metadata = {
        "source_format": "ebench_rollout",
        "input_root": str(input_root),
        "run_name": run_name,
        "task_id": episode.task_id,
        "task_dir": episode.task_dir,
        "episode_id": episode.episode_id,
        "rollout_dir": str(episode.rollout_dir),
        "frames_dir": str(frame_dir),
        "cameras": cameras,
        "num_frames": len(encoded_frames),
        "requested_num_frames": num_frames,
        "jpeg_quality": jpeg_quality,
        "output_image_max_side": output_image_max_side,
        "result_info": result_info,
        **frame_metadata,
    }
    (frame_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return metadata


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-root",
        default="ebench-test_step_h30",
        help="Ebench result root containing ebench/**/<task>_test_mini/<episode>.",
    )
    parser.add_argument(
        "--output-root",
        default="outputs/ebench_preprocessed_frames",
        help="Directory to write sampled composite images.",
    )
    parser.add_argument(
        "--run-name",
        default=None,
        help="Output run name. Defaults to the input root directory name.",
    )
    parser.add_argument(
        "--task",
        action="append",
        dest="tasks",
        help="Task id to preprocess. Can be passed multiple times. Defaults to the six VLM eval tasks.",
    )
    parser.add_argument(
        "--episode",
        action="append",
        dest="episodes",
        help="Episode id to preprocess, for example 000. Can be passed multiple times.",
    )
    parser.add_argument(
        "--num-frames",
        type=int,
        default=50,
        help="Uniformly sample this many synchronized composite frames per episode.",
    )
    parser.add_argument(
        "--sample-every-sec",
        type=float,
        default=1.0,
        help="Used only if --num-frames <= 0. Sample one frame every N seconds.",
    )
    parser.add_argument("--jpeg-quality", type=int, default=85)
    parser.add_argument(
        "--output-image-max-side",
        type=int,
        default=0,
        help="Resize written frame_*.jpg files so their longest side is at most this many pixels. Use 0 to keep original composite size.",
    )
    parser.add_argument(
        "--cameras",
        nargs="+",
        default=DEFAULT_CAMERAS,
        help="Camera files to synchronize and stitch.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing frame directories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only list discovered episodes; do not write images.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_root = Path(args.input_root).resolve()
    output_root = Path(args.output_root).resolve()
    run_name = args.run_name or input_root.name
    task_ids = set(args.tasks or DEFAULT_TASKS)
    episode_ids = set(args.episodes or [])
    num_frames = args.num_frames if args.num_frames > 0 else None

    episodes = discover_episodes(input_root, task_ids)
    if episode_ids:
        episodes = [episode for episode in episodes if episode.episode_id in episode_ids]
    if not episodes:
        raise ValueError(
            f"No episodes found under {input_root} for tasks={sorted(task_ids)} "
            f"episodes={sorted(episode_ids) if episode_ids else 'ALL'}"
        )

    print(f"Found {len(episodes)} episodes in {input_root}")
    if args.dry_run:
        for episode in episodes:
            print(f"{episode.task_id}/{episode.episode_id}: {episode.rollout_dir}")
        return

    output_root.mkdir(parents=True, exist_ok=True)
    summaries = []
    for idx, episode in enumerate(episodes, 1):
        print(f"[{idx}/{len(episodes)}] preprocessing {episode.task_id}/{episode.episode_id}...")
        metadata = preprocess_episode(
            episode=episode,
            input_root=input_root,
            output_root=output_root,
            run_name=run_name,
            cameras=args.cameras,
            num_frames=num_frames,
            sample_every_sec=args.sample_every_sec,
            jpeg_quality=args.jpeg_quality,
            output_image_max_side=args.output_image_max_side
            if args.output_image_max_side > 0
            else None,
            overwrite=args.overwrite,
        )
        summaries.append(metadata)
        suffix = " skipped existing" if metadata.get("skipped_existing") else ""
        print(f"  wrote {metadata.get('num_frames')} frames to {metadata.get('frames_dir')}{suffix}")

    summary_path = output_root / run_name / "metadata.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(
        json.dumps(
            {
                "input_root": str(input_root),
                "output_root": str(output_root),
                "run_name": run_name,
                "tasks": sorted(task_ids),
                "episodes": len(summaries),
                "num_frames": num_frames,
                "output_image_max_side": args.output_image_max_side
                if args.output_image_max_side > 0
                else None,
                "cameras": args.cameras,
                "items": summaries,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote summary metadata to {summary_path}")


if __name__ == "__main__":
    main()
