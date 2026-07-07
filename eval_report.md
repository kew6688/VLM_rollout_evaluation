# Rollout Episodes 的 VLM 评分 Prompt

目标：对当前保存的 rollout episode 分别让 VLM 输出三个值：

```json
{"score": 0.0, "success": 0, "reason": "visible evidence for the score"}
```

统一规则：

- 每个 rollout 单独评估一次。
- 视频抽帧后按时间顺序输入模型，帧名固定为 `frame_000`, `frame_001`, ...。
- 只根据可见画面评分，不参考 `result_info.json`。
- `score` 必须严格按下面每个 task 的 metric 权重计算，范围为 `[0, 1]`。
- `success = 1` 当且仅当 `score == 1`，否则 `success = 0`。
- 只返回一个 JSON object，不要输出 Markdown、置信度或额外字段；`reason` 用一句话说明可见证据。

通用开头可以放在每个 prompt 前：

```text
You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.
Return JSON only with exactly three keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
The reason must be one short sentence explaining the visible evidence behind the score.
```

## Prompt 1: apple_to_fruit_bowl

Episodes:

- `rollout_video/apple_to_fruit_bowl_test_mini/001/001/top_camera.mp4`
- `rollout_video/apple_to_fruit_bowl_test_mini/002/top_camera.mp4`
- 每个 episode 可选多视角：同目录下 `overlook_camera.mp4`, `left_camera.mp4`, `right_camera.mp4`

Prompt:

```text
You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.

Task: apple_to_fruit_bowl
Instruction: Put the apple into the fruit bowl.

Metric:
- score = 1.0 if the apple is placed inside the fruit bowl.
- score = 0.0 otherwise.

Scoring:
- If the apple is visibly inside the fruit bowl at the end of the rollout, return {"score": 1.0, "success": 1}.
- If the apple is not inside the fruit bowl, is dropped outside, only touched, only moved near the bowl, or the final state is ambiguous, return {"score": 0.0, "success": 0, "reason": "visible evidence for the score"}.

Return JSON only with exactly three keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
The reason must be one short sentence explaining the visible evidence behind the score.
```

## Prompt 2: bookmark_on_book

Episodes:

- `rollout_video/bookmark_on_book_test_mini/000/000/top_camera.mp4`
- `rollout_video/bookmark_on_book_test_mini/004/004/top_camera.mp4`
- 每个 episode 可选多视角：同目录下 `overlook_camera.mp4`, `left_camera.mp4`, `right_camera.mp4`

Prompt:

```text
You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.

Task: bookmark_on_book
Instruction: Place the bookmark on the book.

Metric:
- score = 1.0 if the bookmark is placed on the book with at least 40% visible overlap.
- score = 0.0 otherwise.

Scoring:
- If the bookmark is visibly on top of the book and at least about 40% of the bookmark overlaps the book, return {"score": 1.0, "success": 1}.
- If the bookmark is not on the book, overlaps less than about 40%, is dropped elsewhere, only touched, or the final state is ambiguous, return {"score": 0.0, "success": 0, "reason": "visible evidence for the score"}.

Return JSON only with exactly three keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
The reason must be one short sentence explaining the visible evidence behind the score.
```

## Prompt 3: detergent

Episodes:

- `rollout_video/detergent_test_mini/001/001/top_camera.mp4`
- 每个 episode 可选多视角：同目录下 `overlook_camera.mp4`, `left_camera.mp4`, `right_camera.mp4`

Prompt:

```text
You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.

Task: detergent
Instruction: Complete the detergent task by placing or handing over all detergent items as required.

Metric:
- There are 3 detergent items.
- Each completed detergent item is worth 1/3.
- score = (number of visibly completed detergent items) / 3.
- success = 1 only if all 3 detergent items are completed, so score = 1.0.

Scoring:
- If 0 detergent items are completed, return {"score": 0.0, "success": 0, "reason": "visible evidence for the score"}.
- If 1 detergent item is completed, return {"score": 0.3333333333, "success": 0}.
- If 2 detergent items are completed, return {"score": 0.6666666667, "success": 0}.
- If 3 detergent items are completed, return {"score": 1.0, "success": 1}.
- Count only detergent items whose final required state is visibly completed. Do not count items that are only contacted, moved partway, dropped, or ambiguous.

Return JSON only with exactly three keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
The reason must be one short sentence explaining the visible evidence behind the score.
```

## Prompt 4: utensils_to_holder

Episodes:

- `rollout_video/utensils_to_holder_test_mini/001/001/top_camera.mp4`
- 每个 episode 可选多视角：同目录下 `overlook_camera.mp4`, `left_camera.mp4`, `right_camera.mp4`

Prompt:

```text
You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.

Task: utensils_to_holder
Instruction: Place both the spoon and the fork onto the holder.

Metric:
- The spoon placed on the holder is worth 0.5.
- The fork placed on the holder is worth 0.5.
- The order does not matter.
- score = 0.5 * spoon_on_holder + 0.5 * fork_on_holder.
- success = 1 only if both spoon and fork are on the holder, so score = 1.0.

Scoring:
- If neither utensil is on the holder, return {"score": 0.0, "success": 0, "reason": "visible evidence for the score"}.
- If exactly one of the spoon or fork is on the holder, return {"score": 0.5, "success": 0}.
- If both the spoon and fork are on the holder, return {"score": 1.0, "success": 1}.
- Do not count a utensil that is only touched, moved near the holder, dropped outside the holder, or visually ambiguous.

Return JSON only with exactly three keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
The reason must be one short sentence explaining the visible evidence behind the score.
```

## Prompt 5: put_glass_in_glassbox

Episodes:

- `rollout_video/put_glass_in_glassbox_test_mini/002/002/top_camera.mp4`
- `rollout_video/put_glass_in_glassbox_test_mini/010/010/top_camera.mp4`
- 每个 episode 可选多视角：同目录下 `overlook_camera.mp4`, `left_camera.mp4`, `right_camera.mp4`

Prompt:

```text
You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.

Task: put_glass_in_glassbox
Instruction: Put the glasses into the glasses box, fold the temples, and close the box.

Metric:
- Both temples of the glasses folded is worth 1/3.
- The glasses box closed is worth 1/3.
- The glasses inside the glasses box is worth 1/3.
- score = (1/3) * temples_folded + (1/3) * box_closed + (1/3) * glasses_inside_box.
- success = 1 only if all three conditions are satisfied, so score = 1.0.

Important detail:
- For the "glasses inside the glasses box" condition, count it as satisfied as long as the glasses are inside the box, even if the temples are not folded or the box is not closed.
- For the "temples folded" condition, both temples must be visibly folded. If only one temple is folded or the view is ambiguous, do not count this condition.

Scoring:
- Return score as one of 0.0, 0.3333333333, 0.6666666667, or 1.0 according to how many of the three conditions are visibly satisfied.
- Return success = 1 only when score = 1.0.
- Do not count conditions that are only attempted, partially visible, or ambiguous.

Return JSON only with exactly three keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
The reason must be one short sentence explaining the visible evidence behind the score.
```

## Prompt 6: collect_coffee_beans

Episodes:

- `rollout_video/collect_coffee_beans_test_mini/000/000/top_camera.mp4`
- `rollout_video/collect_coffee_beans_test_mini/001/001/top_camera.mp4`
- 每个 episode 可选多视角：同目录下 `overlook_camera.mp4`, `left_camera.mp4`, `right_camera.mp4`

Prompt:

```text
You are evaluating one robot policy rollout in simulation.
You will receive sampled video frames in chronological order.
Judge only from visible evidence in the frames.
Compute score strictly from the task metric.

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

Return JSON only with exactly three keys:
{"score": number, "success": 0 or 1, "reason": string}
Set success to 1 if and only if score equals 1. Otherwise set success to 0.
The reason must be one short sentence explaining the visible evidence behind the score.
```

## 仿真结果对照，仅用于后处理报告，不输入模型

| rollout_id | rollout path | sim score | sim success |
|---|---|---:|---:|
| apple_to_fruit_bowl/001 | `rollout_video/apple_to_fruit_bowl_test_mini/001/001` | 0.0 | 0 |
| apple_to_fruit_bowl/002 | `rollout_video/apple_to_fruit_bowl_test_mini/002` | 1.0 | 1 |
| bookmark_on_book/000 | `rollout_video/bookmark_on_book_test_mini/000/000` | 0.0 | 0 |
| bookmark_on_book/004 | `rollout_video/bookmark_on_book_test_mini/004/004` | 1.0 | 1 |
| collect_coffee_beans/000 | `rollout_video/collect_coffee_beans_test_mini/000/000` | 0.14286 | 0 |
| collect_coffee_beans/001 | `rollout_video/collect_coffee_beans_test_mini/001/001` | 0.5 | 0 |
| detergent/001 | `rollout_video/detergent_test_mini/001/001` | 1.0 | 1 |
| utensils_to_holder/001 | `rollout_video/utensils_to_holder_test_mini/001/001` | 0.5 | 0 |
| put_glass_in_glassbox/002 | `rollout_video/put_glass_in_glassbox_test_mini/002/002` | 1.0 | 1 |
| put_glass_in_glassbox/010 | `rollout_video/put_glass_in_glassbox_test_mini/010/010` | 0.0 | 0 |
