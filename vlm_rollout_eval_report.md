# VLM Rollout Evaluation 简略报告

## 1. 评测目标

本次评测使用 VLM 对机器人 policy rollout 视频进行自动打分，用于对比仿真环境中的 `result_info.json` 与不同视觉语言模型的判断是否一致。

模型输入为 rollout 视频抽帧后的多视角图片；模型输出只保留两个字段：

```json
{"score": number, "success": 0 or 1}
```

其中：

- `score`: 按任务 metric 权重计算，范围 `[0, 1]`。
- `success`: 当且仅当 `score == 1` 时为 `1`，否则为 `0`。

## 2. 当前评测数据

当前共整理了 6 类任务、10 个 episode。

| rollout_id | sim score | sim success | preprocessed frames |
|---|---:|---:|---:|
| apple_to_fruit_bowl/001 | 0.0 | 0 | 51 |
| apple_to_fruit_bowl/002 | 1.0 | 1 | 11 |
| bookmark_on_book/000 | 0.0 | 0 | 51 |
| bookmark_on_book/004 | 1.0 | 1 | 11 |
| collect_coffee_beans/000 | 0.14286 | 0 | 117 |
| collect_coffee_beans/001 | 0.5 | 0 | 117 |
| detergent/001 | 1.0 | 1 | 74 |
| put_glass_in_glassbox/002 | 1.0 | 1 | 76 |
| put_glass_in_glassbox/010 | 0.0 | 0 | 101 |
| utensils_to_holder/001 | 0.5 | 0 | 67 |

预处理图片位置：

```text
outputs/preprocessed_frames/{task_id}/{episode_id}/four_camera/frame_*.jpg
```

当前共生成 676 张四视角拼图。

## 3. 视频处理规则

每个 episode 使用 4 个同步相机：

- `top_camera.mp4`
- `overlook_camera.mp4`
- `left_camera.mp4`
- `right_camera.mp4`

抽帧与拼图规则：

- 默认每秒抽 1 帧。
- 四个相机按相同 frame index 同步抽帧。
- 每个时间点拼成一张 2x2 composite image。
- 拼图布局：
  - 左上：top camera
  - 右上：overlook camera
  - 左下：left camera
  - 右下：right camera
- 每张子图带相机名称标签。
- 图片按时间顺序输入 VLM。

## 4. 评分规则

通用规则：

- 只根据可见画面评分。
- 不把 `result_info.json` 输入给模型。
- 不奖励“意图”，只按最终或 metric 要求的可见状态给分。
- `score` 按 task metric 权重计算。
- `success = 1` 当且仅当 `score == 1`。

各任务 metric：

| task_id | metric |
|---|---|
| apple_to_fruit_bowl | 苹果放入水果碗中，满足为 1，否则为 0 |
| bookmark_on_book | 书签放到书上且至少 40% 重叠，满足为 1，否则为 0 |
| detergent | 3 个 detergent item，每个完成得 1/3 |
| utensils_to_holder | 勺子放到 holder 得 0.5，叉子放到 holder 得 0.5 |
| put_glass_in_glassbox | 两个镜腿折叠 1/3，眼镜盒闭合 1/3，眼镜在盒中 1/3 |
| collect_coffee_beans | 盖子放在罐子上 0.5，7 个咖啡豆每个在罐子里得 0.5/7 |

详细 prompt 见：

```text
评分.md
```

## 5. 模型结果汇总占位

### 5.1 Rollout 级结果

| model | rollout_id | sim score | sim success | vlm score | vlm success | agreement |
|---|---|---:|---:|---:|---:|---:|
| TBD | apple_to_fruit_bowl/001 | 0.0 | 0 | TBD | TBD | TBD |
| TBD | apple_to_fruit_bowl/002 | 1.0 | 1 | TBD | TBD | TBD |
| TBD | bookmark_on_book/000 | 0.0 | 0 | TBD | TBD | TBD |
| TBD | bookmark_on_book/004 | 1.0 | 1 | TBD | TBD | TBD |
| TBD | collect_coffee_beans/000 | 0.14286 | 0 | TBD | TBD | TBD |
| TBD | collect_coffee_beans/001 | 0.5 | 0 | TBD | TBD | TBD |
| TBD | detergent/001 | 1.0 | 1 | TBD | TBD | TBD |
| TBD | put_glass_in_glassbox/002 | 1.0 | 1 | TBD | TBD | TBD |
| TBD | put_glass_in_glassbox/010 | 0.0 | 0 | TBD | TBD | TBD |
| TBD | utensils_to_holder/001 | 0.5 | 0 | TBD | TBD | TBD |

### 5.2 模型级汇总

| model | num episodes | avg vlm score | vlm success rate | agreement rate | false positive | false negative |
|---|---:|---:|---:|---:|---:|---:|
| GPT | TBD | TBD | TBD | TBD | TBD | TBD |
| Gemini | TBD | TBD | TBD | TBD | TBD | TBD |
| Claude | TBD | TBD | TBD | TBD | TBD | TBD |
| Other VLM | TBD | TBD | TBD | TBD | TBD | TBD |

定义：

- `agreement`: `sim success == vlm success`。
- `false positive`: `sim success = 0` 但 `vlm success = 1`。
- `false negative`: `sim success = 1` 但 `vlm success = 0`。

## 6. 后续计划

- 先用 GPT 跑全量 10 个 episode。
- 检查 `score` 与 `success` 是否满足 schema。
- 对不一致样本人工复核四视角图片。
- 继续接入其他 VLM，复用同一批预处理图片和同一套 prompt。
- 最终比较各模型与仿真结果的一致率、假阳性和假阴性。
