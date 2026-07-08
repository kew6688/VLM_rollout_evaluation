#!/usr/bin/env python3
"""Summarize rollout VLM score JSONL files into one comparison report."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    source_mtime = path.stat().st_mtime
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path}:{line_no}: {exc}") from exc
            row["_source_file"] = str(path)
            row["_source_mtime"] = source_mtime
            rows.append(row)
    return rows


def rollout_key(row: dict[str, Any]) -> str:
    episode_path = str(row.get("episode_path") or "").strip()
    if episode_path:
        return episode_path
    return f"{row.get('task_id', '')}/{row.get('episode_id', '')}"


def run_id(row: dict[str, Any]) -> str:
    parts = Path(rollout_key(row)).parts
    if len(parts) >= 4 and parts[0] == parts[1]:
        return parts[0]
    if len(parts) >= 3:
        return parts[0]
    return str(row.get("source", "unknown"))


def deduplicate_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[tuple[str, str, list[str]]]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (
            str(row.get("model", "unknown")),
            rollout_key(row),
        )
        grouped[key].append(row)

    deduped = []
    duplicates = []
    for key, group in grouped.items():
        if len(group) > 1:
            duplicates.append((key[0], key[1], sorted(str(row.get("_source_file")) for row in group)))
        chosen = max(
            group,
            key=lambda row: (
                1 if "error" not in row else 0,
                float(row.get("_source_mtime", 0)),
                1 if not row.get("from_api_debug") else 0,
            ),
        )
        deduped.append(chosen)

    return sorted(
        deduped,
        key=lambda row: (str(row.get("model")), rollout_key(row)),
    ), duplicates


def fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "N/A"
    if isinstance(value, float):
        if math.isnan(value):
            return "N/A"
        return f"{value:.{digits}f}"
    return str(value)


def markdown_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2 or len(xs) != len(ys):
        return None
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys, strict=True))
    var_x = sum((x - mean_x) ** 2 for x in xs)
    var_y = sum((y - mean_y) ** 2 for y in ys)
    denom = math.sqrt(var_x * var_y)
    if denom == 0:
        return None
    return cov / denom


def ranks(values: list[float]) -> list[float]:
    indexed = sorted(enumerate(values), key=lambda item: item[1])
    result = [0.0] * len(values)
    i = 0
    while i < len(indexed):
        j = i + 1
        while j < len(indexed) and indexed[j][1] == indexed[i][1]:
            j += 1
        avg_rank = (i + 1 + j) / 2.0
        for k in range(i, j):
            result[indexed[k][0]] = avg_rank
        i = j
    return result


def spearman(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2 or len(xs) != len(ys):
        return None
    return pearson(ranks(xs), ranks(ys))


def metric_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    scored_rows = [row for row in rows if "error" not in row]
    sim_scores = [float(row["sim_score"]) for row in scored_rows]
    vlm_scores = [float(row["vlm_score"]) for row in scored_rows]
    sim_successes = [int(row["sim_success"]) for row in scored_rows]
    vlm_successes = [int(row["vlm_success"]) for row in scored_rows]

    errors = [v - s for s, v in zip(sim_scores, vlm_scores, strict=True)]
    abs_errors = [abs(error) for error in errors]
    sq_errors = [error * error for error in errors]

    tp = sum(1 for s, v in zip(sim_successes, vlm_successes, strict=True) if s == 1 and v == 1)
    tn = sum(1 for s, v in zip(sim_successes, vlm_successes, strict=True) if s == 0 and v == 0)
    fp = sum(1 for s, v in zip(sim_successes, vlm_successes, strict=True) if s == 0 and v == 1)
    fn = sum(1 for s, v in zip(sim_successes, vlm_successes, strict=True) if s == 1 and v == 0)
    precision = tp / (tp + fp) if tp + fp else None
    recall = tp / (tp + fn) if tp + fn else None
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision is not None and recall is not None and precision + recall
        else None
    )

    no_visual_keywords = (
        "no image",
        "no visible evidence",
        "frames are not accessible",
        "cannot visually",
        "not provided",
    )
    no_visual_count = sum(
        1
        for row in scored_rows
        if any(keyword in str(row.get("vlm_reason", "")).lower() for keyword in no_visual_keywords)
    )

    return {
        "n": len(rows),
        "scored": len(scored_rows),
        "failed": len(rows) - len(scored_rows),
        "score_pearson": pearson(sim_scores, vlm_scores),
        "score_spearman": spearman(sim_scores, vlm_scores),
        "score_mae": sum(abs_errors) / len(abs_errors) if abs_errors else None,
        "score_rmse": math.sqrt(sum(sq_errors) / len(sq_errors)) if sq_errors else None,
        "success_accuracy": (tp + tn) / len(scored_rows) if scored_rows else None,
        "success_precision": precision,
        "success_recall": recall,
        "success_f1": f1,
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "no_visual_count": no_visual_count,
    }


def compact_score(row: dict[str, Any] | None) -> str:
    if row is None:
        return "-"
    if "error" in row:
        return "ERR"
    return f"{fmt(float(row['vlm_score']), 3)} / {int(row['vlm_success'])}"


def model_metric_table(
    lines: list[str],
    title: str,
    grouped_rows: dict[str, list[dict[str, Any]]],
) -> None:
    lines.extend(["", f"## {title}", ""])
    metric_header = [
        "group",
        "scored/total",
        "pearson_score",
        "spearman_score",
        "MAE",
        "RMSE",
        "success_acc",
        "precision",
        "recall",
        "F1",
        "TP/TN/FP/FN",
        "avg_sim_score",
        "avg_vlm_score",
        "vlm_success_rate",
        "no_visual_reason",
    ]
    lines.append("| " + " | ".join(metric_header) + " |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|")
    for group_name in sorted(grouped_rows):
        rows = grouped_rows[group_name]
        summary = metric_summary(rows)
        scored_rows = [row for row in rows if "error" not in row]
        avg_sim_score = (
            sum(float(row["sim_score"]) for row in scored_rows) / len(scored_rows)
            if scored_rows
            else None
        )
        avg_vlm_score = (
            sum(float(row["vlm_score"]) for row in scored_rows) / len(scored_rows)
            if scored_rows
            else None
        )
        vlm_success_rate = (
            sum(int(row["vlm_success"]) for row in scored_rows) / len(scored_rows)
            if scored_rows
            else None
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_cell(group_name),
                    f"{summary['scored']}/{summary['n']}",
                    fmt(summary["score_pearson"]),
                    fmt(summary["score_spearman"]),
                    fmt(summary["score_mae"]),
                    fmt(summary["score_rmse"]),
                    fmt(summary["success_accuracy"]),
                    fmt(summary["success_precision"]),
                    fmt(summary["success_recall"]),
                    fmt(summary["success_f1"]),
                    f"{summary['tp']}/{summary['tn']}/{summary['fp']}/{summary['fn']}",
                    fmt(avg_sim_score),
                    fmt(avg_vlm_score),
                    fmt(vlm_success_rate),
                    str(summary["no_visual_count"]),
                ]
            )
            + " |"
        )


def build_report(
    rows: list[dict[str, Any]],
    raw_row_count: int | None = None,
    duplicates: list[tuple[str, str, list[str]]] | None = None,
) -> str:
    raw_row_count = len(rows) if raw_row_count is None else raw_row_count
    duplicates = [] if duplicates is None else duplicates
    by_model: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_model_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_model_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_rollout: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    rollout_meta: dict[str, tuple[str, str, str, float, int]] = {}

    for row in rows:
        model = str(row.get("model", "unknown"))
        key = rollout_key(row)
        by_model[model].append(row)
        by_model_run[f"{model} | {run_id(row)}"].append(row)
        by_model_task[f"{model} | {row.get('task_id', '')}"].append(row)
        by_rollout[key][model] = row
        if "error" not in row:
            rollout_meta[key] = (
                run_id(row),
                str(row.get("task_id", "")),
                str(row.get("episode_id", "")),
                float(row["sim_score"]),
                int(row["sim_success"]),
            )

    models = sorted(by_model)
    rollout_keys = sorted(by_rollout)
    summaries = {model: metric_summary(model_rows) for model, model_rows in by_model.items()}

    lines = [
        "# VLM Rollout Model Comparison",
        "",
        "## 统计口径",
        "",
        "- 输入文件: `outputs/*_scores.jsonl`",
        "- 每个单元格格式: `vlm_score / vlm_success`",
        "- rollout 去重和对齐键: `episode_path`；缺失时回退到 `task_id/episode_id`。",
        "- success 规则: `vlm_success = 1` 当且仅当 `vlm_score == 1.0`",
        "- 相关系数基于连续分数 `sim_score` 与 `vlm_score` 计算；success 指标基于二值 `sim_success` 与 `vlm_success` 计算。",
        "- 相关系数主要用于横向比较模型趋势；最终判断仍建议结合 MAE、success 混淆矩阵和具体 mismatch case。",
        "",
        "## 覆盖情况",
        "",
        f"- models: {len(models)}",
        f"- unique_rollouts: {len(rollout_keys)}",
        f"- raw_rows: {raw_row_count}",
        f"- deduplicated_rows: {len(rows)}",
    ]
    if duplicates:
        lines.append(f"- duplicate_model_rollout_rows_removed: {raw_row_count - len(rows)}")

    model_metric_table(lines, "模型整体指标汇总", by_model)
    model_metric_table(lines, "按 Run 分组指标", by_model_run)
    model_metric_table(lines, "按任务分组指标", by_model_task)

    lines.extend(["", "## 全部 Rollout 结果表", ""])

    header = ["episode_path", "run", "task_id", "episode_id", "sim_score", "sim_success", *models]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|---|---|---|---|---:|---:|" + "|".join(["---:"] * len(models)) + "|")
    for key in rollout_keys:
        run, task_id, episode_id, sim_score, sim_success = rollout_meta.get(
            key,
            ("unknown", "", "", math.nan, -1),
        )
        cells = [
            key,
            run,
            task_id,
            episode_id,
            fmt(sim_score, 3),
            str(sim_success),
            *[compact_score(by_rollout[key].get(model)) for model in models],
        ]
        lines.append("| " + " | ".join(markdown_cell(cell) for cell in cells) + " |")

    lines.extend(["", "## 与仿真不一致的条目", ""])
    mismatch_rows = [
        row
        for row in rows
        if "error" not in row and int(row["sim_success"]) != int(row["vlm_success"])
    ]
    if mismatch_rows:
        lines.append("| model | episode_path | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | reason |")
        lines.append("|---|---|---|---|---:|---:|---:|---:|---|")
        for row in sorted(mismatch_rows, key=lambda item: (item["model"], rollout_key(item))):
            lines.append(
                "| {model} | {episode_path} | {task_id} | {episode_id} | {sim_score} | {sim_success} | "
                "{vlm_score} | {vlm_success} | {reason} |".format(
                    model=markdown_cell(row["model"]),
                    episode_path=markdown_cell(rollout_key(row)),
                    task_id=markdown_cell(row["task_id"]),
                    episode_id=markdown_cell(row["episode_id"]),
                    sim_score=fmt(float(row["sim_score"]), 3),
                    sim_success=int(row["sim_success"]),
                    vlm_score=fmt(float(row["vlm_score"]), 3),
                    vlm_success=int(row["vlm_success"]),
                    reason=markdown_cell(row.get("vlm_reason", "")),
                )
            )
    else:
        lines.append("No mismatches.")

    failed_rows = [row for row in rows if "error" in row]
    if failed_rows:
        lines.extend(["", "## 失败请求", ""])
        lines.append("| model | episode_path | task_id | episode_id | error |")
        lines.append("|---|---|---|---|---|")
        for row in failed_rows:
            lines.append(
                f"| {markdown_cell(row.get('model', 'unknown'))} | {markdown_cell(rollout_key(row))} | "
                f"{markdown_cell(row.get('task_id', ''))} | "
                f"{markdown_cell(row.get('episode_id', ''))} | {markdown_cell(row.get('error', ''))} |"
            )

    lines.extend(["", "## 初步结论", ""])
    scored_summaries = {model: summary for model, summary in summaries.items() if summary["scored"]}
    if scored_summaries:
        best_acc_value = max(summary["success_accuracy"] or -1 for summary in scored_summaries.values())
        best_pearson_value = max(
            summary["score_pearson"] if summary["score_pearson"] is not None else -2
            for summary in scored_summaries.values()
        )
        best_mae_value = min(
            summary["score_mae"] if summary["score_mae"] is not None else float("inf")
            for summary in scored_summaries.values()
        )
        best_acc_models = [
            model
            for model, summary in scored_summaries.items()
            if summary["success_accuracy"] == best_acc_value
        ]
        best_pearson_models = [
            model
            for model, summary in scored_summaries.items()
            if summary["score_pearson"] == best_pearson_value
        ]
        best_mae_models = [
            model
            for model, summary in scored_summaries.items()
            if summary["score_mae"] == best_mae_value
        ]
        lines.append(
            "- success 一致率最高: "
            + ", ".join(f"`{model}`" for model in best_acc_models)
            + f" ({fmt(best_acc_value)})。"
        )
        lines.append(
            "- 连续分数 Pearson 最高: "
            + ", ".join(f"`{model}`" for model in best_pearson_models)
            + f" ({fmt(best_pearson_value)})。"
        )
        lines.append(
            "- 连续分数 MAE 最低: "
            + ", ".join(f"`{model}`" for model in best_mae_models)
            + f" ({fmt(best_mae_value)})。"
        )
        suspect_models = [
            model
            for model, summary in scored_summaries.items()
            if summary["no_visual_count"] >= max(2, summary["scored"] // 3)
        ]
        if suspect_models:
            lines.append(
                "- 以下模型多次声称无法看到图片或缺少视觉证据，结果可信度需要单独复核: "
                + ", ".join(f"`{model}`" for model in suspect_models)
                + "。"
            )

        candidate_models = [model for model in scored_summaries if model not in suspect_models]
        if candidate_models:
            recommended = min(
                candidate_models,
                key=lambda model: (
                    -(scored_summaries[model]["success_accuracy"] or -1),
                    -(scored_summaries[model]["score_pearson"] if scored_summaries[model]["score_pearson"] is not None else -2),
                    scored_summaries[model]["score_mae"] if scored_summaries[model]["score_mae"] is not None else float("inf"),
                ),
            )
            lines.append(
                f"- 综合 success 一致率、连续分数相关性、MAE 和视觉可用性，当前更建议把 `{recommended}` 作为主参考模型。"
            )

        mismatch_by_rollout = Counter(rollout_key(row) for row in mismatch_rows)
        if mismatch_by_rollout:
            hardest = mismatch_by_rollout.most_common(3)
            formatted = ", ".join(f"`{episode_path}` ({count})" for episode_path, count in hardest)
            lines.append(f"- 模型最常与 sim 不一致的 rollout: {formatted}。")
    else:
        lines.append("- 没有可统计的成功打分行。")

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-glob",
        default="outputs/*_scores.jsonl",
        help="Input JSONL glob. Default: outputs/*_scores.jsonl.",
    )
    parser.add_argument(
        "--output",
        default="outputs/model_comparison_summary.md",
        help="Output Markdown path. Default: outputs/model_comparison_summary.md.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paths = sorted(Path(".").glob(args.input_glob))
    if not paths:
        raise FileNotFoundError(f"No files matched {args.input_glob}")

    rows: list[dict[str, Any]] = []
    for path in paths:
        rows.extend(read_jsonl(path))
    deduped_rows, duplicates = deduplicate_rows(rows)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        build_report(deduped_rows, raw_row_count=len(rows), duplicates=duplicates),
        encoding="utf-8",
    )
    print(
        f"Wrote {output_path} from {len(paths)} files, "
        f"{len(rows)} raw rows, {len(deduped_rows)} deduplicated rows"
    )


if __name__ == "__main__":
    main()
