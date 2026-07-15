# VLM Rollout Model Comparison

## 统计口径

- 输入文件: `outputs/*_scores.jsonl`
- 每个单元格格式: `vlm_score / vlm_success`
- rollout 去重和对齐键: `episode_path`；缺失时回退到 `task_id/episode_id`。
- success 规则: `vlm_success = 1` 当且仅当 `vlm_score == 1.0`
- 相关系数基于连续分数 `sim_score` 与 `vlm_score` 计算；success 指标基于二值 `sim_success` 与 `vlm_success` 计算。
- 相关系数主要用于横向比较模型趋势；最终判断仍建议结合 MAE、success 混淆矩阵和具体 mismatch case。

## 覆盖情况

- models: 4
- unique_rollouts: 360
- raw_rows: 1440
- deduplicated_rows: 1440

## 模型整体指标汇总

| group | scored/total | pearson_score | spearman_score | MAE | RMSE | success_acc | precision | recall | F1 | TP/TN/FP/FN | avg_sim_score | avg_vlm_score | vlm_success_rate | no_visual_reason |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| bailian/deepseek-v4-pro | 360/360 | 0.000 | -0.012 | 0.391 | 0.580 | 0.683 | 0.247 | 0.234 | 0.240 | 18/228/55/59 | 0.315 | 0.217 | 0.203 | 64 |
| gemini-3.5-flash | 360/360 | 0.723 | 0.717 | 0.135 | 0.313 | 0.892 | 0.707 | 0.844 | 0.769 | 65/256/27/12 | 0.315 | 0.374 | 0.256 | 0 |
| gpt-5 | 360/360 | 0.726 | 0.685 | 0.128 | 0.300 | 0.911 | 1.000 | 0.584 | 0.738 | 45/283/0/32 | 0.315 | 0.220 | 0.125 | 0 |
| gpt-5.5 | 360/360 | 0.817 | 0.819 | 0.083 | 0.241 | 0.933 | 0.896 | 0.779 | 0.833 | 60/276/7/17 | 0.315 | 0.300 | 0.186 | 0 |

## 按 Run 分组指标

| group | scored/total | pearson_score | spearman_score | MAE | RMSE | success_acc | precision | recall | F1 | TP/TN/FP/FN | avg_sim_score | avg_vlm_score | vlm_success_rate | no_visual_reason |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| bailian/deepseek-v4-pro \| cosmos_test_50k | 120/120 | -0.057 | -0.026 | 0.293 | 0.519 | 0.742 | 0.042 | 0.111 | 0.061 | 1/88/23/8 | 0.100 | 0.229 | 0.200 | 19 |
| bailian/deepseek-v4-pro \| ebench-test_step_h30 | 120/120 | 0.086 | 0.089 | 0.446 | 0.627 | 0.608 | 0.438 | 0.326 | 0.373 | 14/59/18/29 | 0.465 | 0.271 | 0.267 | 21 |
| bailian/deepseek-v4-pro \| lingbot_57500_1 | 120/120 | -0.083 | -0.094 | 0.434 | 0.591 | 0.700 | 0.176 | 0.120 | 0.143 | 3/81/14/22 | 0.381 | 0.150 | 0.142 | 24 |
| gemini-3.5-flash \| cosmos_test_50k | 120/120 | 0.641 | 0.632 | 0.103 | 0.283 | 0.933 | 0.533 | 0.889 | 0.667 | 8/104/7/1 | 0.100 | 0.186 | 0.125 | 0 |
| gemini-3.5-flash \| ebench-test_step_h30 | 120/120 | 0.720 | 0.703 | 0.156 | 0.333 | 0.875 | 0.792 | 0.884 | 0.835 | 38/67/10/5 | 0.465 | 0.518 | 0.400 | 0 |
| gemini-3.5-flash \| lingbot_57500_1 | 120/120 | 0.675 | 0.691 | 0.147 | 0.320 | 0.867 | 0.655 | 0.760 | 0.704 | 19/85/10/6 | 0.381 | 0.417 | 0.242 | 0 |
| gpt-5 \| cosmos_test_50k | 120/120 | 0.921 | 0.876 | 0.018 | 0.107 | 0.992 | 1.000 | 0.889 | 0.941 | 8/111/0/1 | 0.100 | 0.096 | 0.067 | 0 |
| gpt-5 \| ebench-test_step_h30 | 120/120 | 0.714 | 0.681 | 0.187 | 0.354 | 0.858 | 1.000 | 0.605 | 0.754 | 26/77/0/17 | 0.465 | 0.322 | 0.217 | 0 |
| gpt-5 \| lingbot_57500_1 | 120/120 | 0.566 | 0.529 | 0.180 | 0.365 | 0.883 | 1.000 | 0.440 | 0.611 | 11/95/0/14 | 0.381 | 0.242 | 0.092 | 0 |
| gpt-5.5 \| cosmos_test_50k | 120/120 | 0.756 | 0.781 | 0.045 | 0.194 | 0.967 | 0.778 | 0.778 | 0.778 | 7/109/2/2 | 0.100 | 0.111 | 0.075 | 0 |
| gpt-5.5 \| ebench-test_step_h30 | 120/120 | 0.842 | 0.827 | 0.099 | 0.247 | 0.933 | 0.949 | 0.860 | 0.902 | 37/75/2/6 | 0.465 | 0.438 | 0.325 | 0 |
| gpt-5.5 \| lingbot_57500_1 | 120/120 | 0.736 | 0.763 | 0.105 | 0.276 | 0.900 | 0.842 | 0.640 | 0.727 | 16/92/3/9 | 0.381 | 0.350 | 0.158 | 0 |

## 按任务分组指标

| group | scored/total | pearson_score | spearman_score | MAE | RMSE | success_acc | precision | recall | F1 | TP/TN/FP/FN | avg_sim_score | avg_vlm_score | vlm_success_rate | no_visual_reason |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| bailian/deepseek-v4-pro \| apple_to_fruit_bowl | 60/60 | -0.093 | -0.093 | 0.467 | 0.683 | 0.533 | 0.286 | 0.182 | 0.222 | 4/28/10/18 | 0.367 | 0.233 | 0.233 | 4 |
| bailian/deepseek-v4-pro \| bookmark_on_book | 60/60 | -0.001 | -0.001 | 0.433 | 0.658 | 0.567 | 0.316 | 0.316 | 0.316 | 6/28/13/13 | 0.317 | 0.317 | 0.317 | 8 |
| bailian/deepseek-v4-pro \| collect_coffee_beans | 60/60 | -0.129 | -0.055 | 0.261 | 0.435 | 0.850 | 0.000 | 0.000 | N/A | 0/51/6/3 | 0.174 | 0.108 | 0.100 | 22 |
| bailian/deepseek-v4-pro \| detergent | 60/60 | -0.028 | -0.034 | 0.528 | 0.684 | 0.583 | 0.462 | 0.250 | 0.324 | 6/29/7/18 | 0.533 | 0.239 | 0.217 | 7 |
| bailian/deepseek-v4-pro \| put_glass_in_glassbox | 60/60 | 0.170 | 0.144 | 0.300 | 0.447 | 0.850 | 0.400 | 0.250 | 0.308 | 2/49/3/6 | 0.300 | 0.111 | 0.083 | 20 |
| bailian/deepseek-v4-pro \| utensils_to_holder | 60/60 | 0.036 | 0.048 | 0.358 | 0.512 | 0.717 | 0.000 | 0.000 | N/A | 0/43/16/1 | 0.200 | 0.292 | 0.267 | 3 |
| gemini-3.5-flash \| apple_to_fruit_bowl | 60/60 | 0.452 | 0.457 | 0.278 | 0.524 | 0.733 | 0.607 | 0.773 | 0.680 | 17/27/11/5 | 0.367 | 0.478 | 0.467 | 0 |
| gemini-3.5-flash \| bookmark_on_book | 60/60 | 0.887 | 0.887 | 0.050 | 0.224 | 0.950 | 0.900 | 0.947 | 0.923 | 18/39/2/1 | 0.317 | 0.333 | 0.333 | 0 |
| gemini-3.5-flash \| collect_coffee_beans | 60/60 | 0.721 | 0.807 | 0.142 | 0.273 | 0.850 | 0.200 | 0.667 | 0.308 | 2/49/8/1 | 0.174 | 0.233 | 0.167 | 0 |
| gemini-3.5-flash \| detergent | 60/60 | 0.877 | 0.891 | 0.089 | 0.228 | 0.950 | 0.889 | 1.000 | 0.941 | 24/33/3/0 | 0.533 | 0.611 | 0.450 | 0 |
| gemini-3.5-flash \| put_glass_in_glassbox | 60/60 | 0.742 | 0.768 | 0.111 | 0.236 | 0.900 | 0.667 | 0.500 | 0.571 | 4/50/2/4 | 0.300 | 0.344 | 0.100 | 0 |
| gemini-3.5-flash \| utensils_to_holder | 60/60 | 0.443 | 0.479 | 0.142 | 0.281 | 0.967 | 0.000 | 0.000 | N/A | 0/58/1/1 | 0.200 | 0.242 | 0.017 | 0 |
| gpt-5 \| apple_to_fruit_bowl | 60/60 | 0.929 | 0.929 | 0.033 | 0.183 | 0.967 | 1.000 | 0.909 | 0.952 | 20/38/0/2 | 0.367 | 0.333 | 0.333 | 0 |
| gpt-5 \| bookmark_on_book | 60/60 | 0.273 | 0.273 | 0.283 | 0.532 | 0.717 | 1.000 | 0.105 | 0.190 | 2/41/0/17 | 0.317 | 0.033 | 0.033 | 0 |
| gpt-5 \| collect_coffee_beans | 60/60 | 0.288 | 0.313 | 0.158 | 0.295 | 0.950 | N/A | 0.000 | N/A | 0/57/0/3 | 0.174 | 0.037 | 0.000 | 0 |
| gpt-5 \| detergent | 60/60 | 0.957 | 0.958 | 0.039 | 0.129 | 0.967 | 1.000 | 0.917 | 0.957 | 22/36/0/2 | 0.533 | 0.539 | 0.367 | 0 |
| gpt-5 \| put_glass_in_glassbox | 60/60 | 0.684 | 0.639 | 0.139 | 0.247 | 0.883 | 1.000 | 0.125 | 0.222 | 1/52/0/7 | 0.300 | 0.261 | 0.017 | 0 |
| gpt-5 \| utensils_to_holder | 60/60 | 0.558 | 0.550 | 0.117 | 0.242 | 0.983 | N/A | 0.000 | N/A | 0/59/0/1 | 0.200 | 0.117 | 0.000 | 0 |
| gpt-5.5 \| apple_to_fruit_bowl | 60/60 | 0.856 | 0.856 | 0.067 | 0.258 | 0.933 | 0.909 | 0.909 | 0.909 | 20/36/2/2 | 0.367 | 0.367 | 0.367 | 0 |
| gpt-5.5 \| bookmark_on_book | 60/60 | 0.617 | 0.617 | 0.167 | 0.408 | 0.833 | 1.000 | 0.474 | 0.643 | 9/41/0/10 | 0.317 | 0.150 | 0.150 | 0 |
| gpt-5.5 \| collect_coffee_beans | 60/60 | 0.716 | 0.883 | 0.107 | 0.211 | 0.900 | 0.000 | 0.000 | N/A | 0/54/3/3 | 0.174 | 0.179 | 0.050 | 0 |
| gpt-5.5 \| detergent | 60/60 | 0.963 | 0.967 | 0.033 | 0.122 | 0.983 | 0.960 | 1.000 | 0.980 | 24/35/1/0 | 0.533 | 0.556 | 0.417 | 0 |
| gpt-5.5 \| put_glass_in_glassbox | 60/60 | 0.836 | 0.764 | 0.083 | 0.188 | 0.967 | 1.000 | 0.750 | 0.857 | 6/52/0/2 | 0.300 | 0.339 | 0.100 | 0 |
| gpt-5.5 \| utensils_to_holder | 60/60 | 0.859 | 0.863 | 0.042 | 0.144 | 0.983 | 0.500 | 1.000 | 0.667 | 1/58/1/0 | 0.200 | 0.208 | 0.033 | 0 |

## 全部 Rollout 结果表

| episode_path | run | task_id | episode_id | sim_score | sim_success | bailian/deepseek-v4-pro | gemini-3.5-flash | gpt-5 | gpt-5.5 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/000 | cosmos_test_50k | apple_to_fruit_bowl | 000 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/001 | cosmos_test_50k | apple_to_fruit_bowl | 001 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/002 | cosmos_test_50k | apple_to_fruit_bowl | 002 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/003 | cosmos_test_50k | apple_to_fruit_bowl | 003 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/004 | cosmos_test_50k | apple_to_fruit_bowl | 004 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/005 | cosmos_test_50k | apple_to_fruit_bowl | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/006 | cosmos_test_50k | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/007 | cosmos_test_50k | apple_to_fruit_bowl | 007 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/008 | cosmos_test_50k | apple_to_fruit_bowl | 008 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/009 | cosmos_test_50k | apple_to_fruit_bowl | 009 | 0.000 | 0 | 1.000 / 1 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/010 | cosmos_test_50k | apple_to_fruit_bowl | 010 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/011 | cosmos_test_50k | apple_to_fruit_bowl | 011 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/012 | cosmos_test_50k | apple_to_fruit_bowl | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/013 | cosmos_test_50k | apple_to_fruit_bowl | 013 | 1.000 | 1 | 0.000 / 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/014 | cosmos_test_50k | apple_to_fruit_bowl | 014 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/015 | cosmos_test_50k | apple_to_fruit_bowl | 015 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/016 | cosmos_test_50k | apple_to_fruit_bowl | 016 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/017 | cosmos_test_50k | apple_to_fruit_bowl | 017 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/018 | cosmos_test_50k | apple_to_fruit_bowl | 018 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/019 | cosmos_test_50k | apple_to_fruit_bowl | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/000 | cosmos_test_50k | bookmark_on_book | 000 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/001 | cosmos_test_50k | bookmark_on_book | 001 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/002 | cosmos_test_50k | bookmark_on_book | 002 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/003 | cosmos_test_50k | bookmark_on_book | 003 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/004 | cosmos_test_50k | bookmark_on_book | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/005 | cosmos_test_50k | bookmark_on_book | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/006 | cosmos_test_50k | bookmark_on_book | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/007 | cosmos_test_50k | bookmark_on_book | 007 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/008 | cosmos_test_50k | bookmark_on_book | 008 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/009 | cosmos_test_50k | bookmark_on_book | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/010 | cosmos_test_50k | bookmark_on_book | 010 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/011 | cosmos_test_50k | bookmark_on_book | 011 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/012 | cosmos_test_50k | bookmark_on_book | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/013 | cosmos_test_50k | bookmark_on_book | 013 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/014 | cosmos_test_50k | bookmark_on_book | 014 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/015 | cosmos_test_50k | bookmark_on_book | 015 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/016 | cosmos_test_50k | bookmark_on_book | 016 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/017 | cosmos_test_50k | bookmark_on_book | 017 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/018 | cosmos_test_50k | bookmark_on_book | 018 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/bookmark_on_book/019 | cosmos_test_50k | bookmark_on_book | 019 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/000 | cosmos_test_50k | collect_coffee_beans | 000 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/001 | cosmos_test_50k | collect_coffee_beans | 001 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/002 | cosmos_test_50k | collect_coffee_beans | 002 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/003 | cosmos_test_50k | collect_coffee_beans | 003 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.214 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/004 | cosmos_test_50k | collect_coffee_beans | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/005 | cosmos_test_50k | collect_coffee_beans | 005 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/006 | cosmos_test_50k | collect_coffee_beans | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/007 | cosmos_test_50k | collect_coffee_beans | 007 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/008 | cosmos_test_50k | collect_coffee_beans | 008 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/009 | cosmos_test_50k | collect_coffee_beans | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/010 | cosmos_test_50k | collect_coffee_beans | 010 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/011 | cosmos_test_50k | collect_coffee_beans | 011 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/012 | cosmos_test_50k | collect_coffee_beans | 012 | 0.286 | 0 | 0.500 / 0 | 1.000 / 1 | 0.500 / 0 | 0.786 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/013 | cosmos_test_50k | collect_coffee_beans | 013 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/014 | cosmos_test_50k | collect_coffee_beans | 014 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/015 | cosmos_test_50k | collect_coffee_beans | 015 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/016 | cosmos_test_50k | collect_coffee_beans | 016 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/017 | cosmos_test_50k | collect_coffee_beans | 017 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/018 | cosmos_test_50k | collect_coffee_beans | 018 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/019 | cosmos_test_50k | collect_coffee_beans | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/000 | cosmos_test_50k | detergent | 000 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/001 | cosmos_test_50k | detergent | 001 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/002 | cosmos_test_50k | detergent | 002 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/003 | cosmos_test_50k | detergent | 003 | 0.000 | 0 | 1.000 / 1 | 0.333 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/004 | cosmos_test_50k | detergent | 004 | 0.000 | 0 | 1.000 / 1 | 0.333 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/005 | cosmos_test_50k | detergent | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/006 | cosmos_test_50k | detergent | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/007 | cosmos_test_50k | detergent | 007 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/008 | cosmos_test_50k | detergent | 008 | 0.000 | 0 | 1.000 / 1 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/009 | cosmos_test_50k | detergent | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/010 | cosmos_test_50k | detergent | 010 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/011 | cosmos_test_50k | detergent | 011 | 0.000 | 0 | 0.000 / 0 | 0.333 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/012 | cosmos_test_50k | detergent | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/013 | cosmos_test_50k | detergent | 013 | 0.000 | 0 | 0.667 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/014 | cosmos_test_50k | detergent | 014 | 0.000 | 0 | 0.000 / 0 | 0.667 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/015 | cosmos_test_50k | detergent | 015 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/016 | cosmos_test_50k | detergent | 016 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/017 | cosmos_test_50k | detergent | 017 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/018 | cosmos_test_50k | detergent | 018 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/detergent/019 | cosmos_test_50k | detergent | 019 | 0.000 | 0 | 0.667 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/000 | cosmos_test_50k | put_glass_in_glassbox | 000 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/001 | cosmos_test_50k | put_glass_in_glassbox | 001 | 0.333 | 0 | 1.000 / 1 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/002 | cosmos_test_50k | put_glass_in_glassbox | 002 | 0.333 | 0 | 0.000 / 0 | 0.667 / 0 | 0.333 / 0 | 0.333 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/003 | cosmos_test_50k | put_glass_in_glassbox | 003 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/004 | cosmos_test_50k | put_glass_in_glassbox | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/005 | cosmos_test_50k | put_glass_in_glassbox | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/006 | cosmos_test_50k | put_glass_in_glassbox | 006 | 0.000 | 0 | 0.667 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/007 | cosmos_test_50k | put_glass_in_glassbox | 007 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/008 | cosmos_test_50k | put_glass_in_glassbox | 008 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/009 | cosmos_test_50k | put_glass_in_glassbox | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/010 | cosmos_test_50k | put_glass_in_glassbox | 010 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.000 / 0 | 0.333 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/011 | cosmos_test_50k | put_glass_in_glassbox | 011 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/012 | cosmos_test_50k | put_glass_in_glassbox | 012 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/013 | cosmos_test_50k | put_glass_in_glassbox | 013 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/014 | cosmos_test_50k | put_glass_in_glassbox | 014 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.333 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/015 | cosmos_test_50k | put_glass_in_glassbox | 015 | 0.000 | 0 | 0.000 / 0 | 0.333 / 0 | 0.000 / 0 | 0.333 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/016 | cosmos_test_50k | put_glass_in_glassbox | 016 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/017 | cosmos_test_50k | put_glass_in_glassbox | 017 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/018 | cosmos_test_50k | put_glass_in_glassbox | 018 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/019 | cosmos_test_50k | put_glass_in_glassbox | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/000 | cosmos_test_50k | utensils_to_holder | 000 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/001 | cosmos_test_50k | utensils_to_holder | 001 | 0.000 | 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/002 | cosmos_test_50k | utensils_to_holder | 002 | 0.000 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/003 | cosmos_test_50k | utensils_to_holder | 003 | 0.000 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/004 | cosmos_test_50k | utensils_to_holder | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/005 | cosmos_test_50k | utensils_to_holder | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/006 | cosmos_test_50k | utensils_to_holder | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/007 | cosmos_test_50k | utensils_to_holder | 007 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/008 | cosmos_test_50k | utensils_to_holder | 008 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/009 | cosmos_test_50k | utensils_to_holder | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/010 | cosmos_test_50k | utensils_to_holder | 010 | 0.000 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/011 | cosmos_test_50k | utensils_to_holder | 011 | 0.000 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/012 | cosmos_test_50k | utensils_to_holder | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/013 | cosmos_test_50k | utensils_to_holder | 013 | 0.500 | 0 | 1.000 / 1 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/014 | cosmos_test_50k | utensils_to_holder | 014 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/015 | cosmos_test_50k | utensils_to_holder | 015 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/016 | cosmos_test_50k | utensils_to_holder | 016 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/017 | cosmos_test_50k | utensils_to_holder | 017 | 0.000 | 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/018 | cosmos_test_50k | utensils_to_holder | 018 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| cosmos_test_50k/cosmos_test_50k/utensils_to_holder/019 | cosmos_test_50k | utensils_to_holder | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/000 | ebench-test_step_h30 | apple_to_fruit_bowl | 000 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/001 | ebench-test_step_h30 | apple_to_fruit_bowl | 001 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/002 | ebench-test_step_h30 | apple_to_fruit_bowl | 002 | 1.000 | 1 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/apple_to_fruit_bowl/003 | ebench-test_step_h30 | apple_to_fruit_bowl | 003 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/004 | ebench-test_step_h30 | apple_to_fruit_bowl | 004 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/005 | ebench-test_step_h30 | apple_to_fruit_bowl | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/006 | ebench-test_step_h30 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 / 0 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/apple_to_fruit_bowl/007 | ebench-test_step_h30 | apple_to_fruit_bowl | 007 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/apple_to_fruit_bowl/008 | ebench-test_step_h30 | apple_to_fruit_bowl | 008 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/009 | ebench-test_step_h30 | apple_to_fruit_bowl | 009 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/apple_to_fruit_bowl/010 | ebench-test_step_h30 | apple_to_fruit_bowl | 010 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/apple_to_fruit_bowl/011 | ebench-test_step_h30 | apple_to_fruit_bowl | 011 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/012 | ebench-test_step_h30 | apple_to_fruit_bowl | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/013 | ebench-test_step_h30 | apple_to_fruit_bowl | 013 | 0.000 | 0 | 0.000 / 0 | 0.700 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/014 | ebench-test_step_h30 | apple_to_fruit_bowl | 014 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/apple_to_fruit_bowl/015 | ebench-test_step_h30 | apple_to_fruit_bowl | 015 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/016 | ebench-test_step_h30 | apple_to_fruit_bowl | 016 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/017 | ebench-test_step_h30 | apple_to_fruit_bowl | 017 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/018 | ebench-test_step_h30 | apple_to_fruit_bowl | 018 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/apple_to_fruit_bowl/019 | ebench-test_step_h30 | apple_to_fruit_bowl | 019 | 0.000 | 0 | 1.000 / 1 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/000 | ebench-test_step_h30 | bookmark_on_book | 000 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/001 | ebench-test_step_h30 | bookmark_on_book | 001 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/002 | ebench-test_step_h30 | bookmark_on_book | 002 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/003 | ebench-test_step_h30 | bookmark_on_book | 003 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/004 | ebench-test_step_h30 | bookmark_on_book | 004 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/bookmark_on_book/005 | ebench-test_step_h30 | bookmark_on_book | 005 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/bookmark_on_book/006 | ebench-test_step_h30 | bookmark_on_book | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/007 | ebench-test_step_h30 | bookmark_on_book | 007 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/bookmark_on_book/008 | ebench-test_step_h30 | bookmark_on_book | 008 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/009 | ebench-test_step_h30 | bookmark_on_book | 009 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/bookmark_on_book/010 | ebench-test_step_h30 | bookmark_on_book | 010 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/011 | ebench-test_step_h30 | bookmark_on_book | 011 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/bookmark_on_book/012 | ebench-test_step_h30 | bookmark_on_book | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/013 | ebench-test_step_h30 | bookmark_on_book | 013 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/bookmark_on_book/014 | ebench-test_step_h30 | bookmark_on_book | 014 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/015 | ebench-test_step_h30 | bookmark_on_book | 015 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/016 | ebench-test_step_h30 | bookmark_on_book | 016 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/017 | ebench-test_step_h30 | bookmark_on_book | 017 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/018 | ebench-test_step_h30 | bookmark_on_book | 018 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/bookmark_on_book/019 | ebench-test_step_h30 | bookmark_on_book | 019 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/000 | ebench-test_step_h30 | collect_coffee_beans | 000 | 0.143 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/001 | ebench-test_step_h30 | collect_coffee_beans | 001 | 0.500 | 0 | 0.000 / 0 | 0.250 / 0 | 0.000 / 0 | 0.214 / 0 |
| ebench-test_step_h30/collect_coffee_beans/002 | ebench-test_step_h30 | collect_coffee_beans | 002 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/003 | ebench-test_step_h30 | collect_coffee_beans | 003 | 0.429 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.286 / 0 |
| ebench-test_step_h30/collect_coffee_beans/004 | ebench-test_step_h30 | collect_coffee_beans | 004 | 0.500 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/collect_coffee_beans/005 | ebench-test_step_h30 | collect_coffee_beans | 005 | 0.357 | 0 | 0.000 / 0 | 0.500 / 0 | 0.357 / 0 | 0.357 / 0 |
| ebench-test_step_h30/collect_coffee_beans/006 | ebench-test_step_h30 | collect_coffee_beans | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/007 | ebench-test_step_h30 | collect_coffee_beans | 007 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/008 | ebench-test_step_h30 | collect_coffee_beans | 008 | 0.500 | 0 | 0.000 / 0 | 0.200 / 0 | 0.000 / 0 | 0.071 / 0 |
| ebench-test_step_h30/collect_coffee_beans/009 | ebench-test_step_h30 | collect_coffee_beans | 009 | 0.429 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.214 / 0 |
| ebench-test_step_h30/collect_coffee_beans/010 | ebench-test_step_h30 | collect_coffee_beans | 010 | 0.143 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/011 | ebench-test_step_h30 | collect_coffee_beans | 011 | 0.214 | 0 | 1.000 / 1 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/012 | ebench-test_step_h30 | collect_coffee_beans | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/013 | ebench-test_step_h30 | collect_coffee_beans | 013 | 0.500 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.500 / 0 |
| ebench-test_step_h30/collect_coffee_beans/014 | ebench-test_step_h30 | collect_coffee_beans | 014 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/015 | ebench-test_step_h30 | collect_coffee_beans | 015 | 0.071 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.071 / 0 |
| ebench-test_step_h30/collect_coffee_beans/016 | ebench-test_step_h30 | collect_coffee_beans | 016 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/017 | ebench-test_step_h30 | collect_coffee_beans | 017 | 0.143 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.143 / 0 |
| ebench-test_step_h30/collect_coffee_beans/018 | ebench-test_step_h30 | collect_coffee_beans | 018 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/collect_coffee_beans/019 | ebench-test_step_h30 | collect_coffee_beans | 019 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| ebench-test_step_h30/detergent/000 | ebench-test_step_h30 | detergent | 000 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/001 | ebench-test_step_h30 | detergent | 001 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.667 / 0 | 1.000 / 1 |
| ebench-test_step_h30/detergent/002 | ebench-test_step_h30 | detergent | 002 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/003 | ebench-test_step_h30 | detergent | 003 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/004 | ebench-test_step_h30 | detergent | 004 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/005 | ebench-test_step_h30 | detergent | 005 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/006 | ebench-test_step_h30 | detergent | 006 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/007 | ebench-test_step_h30 | detergent | 007 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/008 | ebench-test_step_h30 | detergent | 008 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/009 | ebench-test_step_h30 | detergent | 009 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/010 | ebench-test_step_h30 | detergent | 010 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/011 | ebench-test_step_h30 | detergent | 011 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/012 | ebench-test_step_h30 | detergent | 012 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/013 | ebench-test_step_h30 | detergent | 013 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/014 | ebench-test_step_h30 | detergent | 014 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 0.667 / 0 | 1.000 / 1 |
| ebench-test_step_h30/detergent/015 | ebench-test_step_h30 | detergent | 015 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/016 | ebench-test_step_h30 | detergent | 016 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/017 | ebench-test_step_h30 | detergent | 017 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/018 | ebench-test_step_h30 | detergent | 018 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/detergent/019 | ebench-test_step_h30 | detergent | 019 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/put_glass_in_glassbox/000 | ebench-test_step_h30 | put_glass_in_glassbox | 000 | 0.333 | 0 | 0.000 / 0 | 1.000 / 1 | 0.667 / 0 | 0.667 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/001 | ebench-test_step_h30 | put_glass_in_glassbox | 001 | 0.667 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/002 | ebench-test_step_h30 | put_glass_in_glassbox | 002 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.667 / 0 | 1.000 / 1 |
| ebench-test_step_h30/put_glass_in_glassbox/003 | ebench-test_step_h30 | put_glass_in_glassbox | 003 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| ebench-test_step_h30/put_glass_in_glassbox/004 | ebench-test_step_h30 | put_glass_in_glassbox | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/005 | ebench-test_step_h30 | put_glass_in_glassbox | 005 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/006 | ebench-test_step_h30 | put_glass_in_glassbox | 006 | 0.667 | 0 | 0.000 / 0 | 0.333 / 0 | 0.667 / 0 | 0.667 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/007 | ebench-test_step_h30 | put_glass_in_glassbox | 007 | 0.000 | 0 | 1.000 / 1 | 0.667 / 0 | 0.333 / 0 | 0.667 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/008 | ebench-test_step_h30 | put_glass_in_glassbox | 008 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.333 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/009 | ebench-test_step_h30 | put_glass_in_glassbox | 009 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.667 / 0 | 0.667 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/010 | ebench-test_step_h30 | put_glass_in_glassbox | 010 | 0.000 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/011 | ebench-test_step_h30 | put_glass_in_glassbox | 011 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.667 / 0 | 1.000 / 1 |
| ebench-test_step_h30/put_glass_in_glassbox/012 | ebench-test_step_h30 | put_glass_in_glassbox | 012 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.667 / 0 | 1.000 / 1 |
| ebench-test_step_h30/put_glass_in_glassbox/013 | ebench-test_step_h30 | put_glass_in_glassbox | 013 | 1.000 | 1 | 0.000 / 0 | 0.667 / 0 | 0.333 / 0 | 1.000 / 1 |
| ebench-test_step_h30/put_glass_in_glassbox/014 | ebench-test_step_h30 | put_glass_in_glassbox | 014 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.000 / 0 | 0.333 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/015 | ebench-test_step_h30 | put_glass_in_glassbox | 015 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.333 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/016 | ebench-test_step_h30 | put_glass_in_glassbox | 016 | 1.000 | 1 | 1.000 / 1 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/017 | ebench-test_step_h30 | put_glass_in_glassbox | 017 | 0.000 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/018 | ebench-test_step_h30 | put_glass_in_glassbox | 018 | 1.000 | 1 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| ebench-test_step_h30/put_glass_in_glassbox/019 | ebench-test_step_h30 | put_glass_in_glassbox | 019 | 0.000 | 0 | 0.000 / 0 | 0.333 / 0 | 0.667 / 0 | 0.333 / 0 |
| ebench-test_step_h30/utensils_to_holder/000 | ebench-test_step_h30 | utensils_to_holder | 000 | 0.000 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/001 | ebench-test_step_h30 | utensils_to_holder | 001 | 0.500 | 0 | 1.000 / 1 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/002 | ebench-test_step_h30 | utensils_to_holder | 002 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/003 | ebench-test_step_h30 | utensils_to_holder | 003 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/004 | ebench-test_step_h30 | utensils_to_holder | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/005 | ebench-test_step_h30 | utensils_to_holder | 005 | 0.500 | 0 | 1.000 / 1 | 0.500 / 0 | 0.000 / 0 | 1.000 / 1 |
| ebench-test_step_h30/utensils_to_holder/006 | ebench-test_step_h30 | utensils_to_holder | 006 | 0.500 | 0 | 0.000 / 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/007 | ebench-test_step_h30 | utensils_to_holder | 007 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/008 | ebench-test_step_h30 | utensils_to_holder | 008 | 0.000 | 0 | 1.000 / 1 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/009 | ebench-test_step_h30 | utensils_to_holder | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/010 | ebench-test_step_h30 | utensils_to_holder | 010 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/011 | ebench-test_step_h30 | utensils_to_holder | 011 | 0.500 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/012 | ebench-test_step_h30 | utensils_to_holder | 012 | 0.500 | 0 | 1.000 / 1 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/013 | ebench-test_step_h30 | utensils_to_holder | 013 | 0.500 | 0 | 1.000 / 1 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/014 | ebench-test_step_h30 | utensils_to_holder | 014 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/015 | ebench-test_step_h30 | utensils_to_holder | 015 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/016 | ebench-test_step_h30 | utensils_to_holder | 016 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/017 | ebench-test_step_h30 | utensils_to_holder | 017 | 0.500 | 0 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 | 0.000 / 0 |
| ebench-test_step_h30/utensils_to_holder/018 | ebench-test_step_h30 | utensils_to_holder | 018 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| ebench-test_step_h30/utensils_to_holder/019 | ebench-test_step_h30 | utensils_to_holder | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/000 | lingbot_57500_1 | apple_to_fruit_bowl | 000 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/001 | lingbot_57500_1 | apple_to_fruit_bowl | 001 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/002 | lingbot_57500_1 | apple_to_fruit_bowl | 002 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/003 | lingbot_57500_1 | apple_to_fruit_bowl | 003 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/004 | lingbot_57500_1 | apple_to_fruit_bowl | 004 | 1.000 | 1 | 0.000 / 0 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/005 | lingbot_57500_1 | apple_to_fruit_bowl | 005 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/006 | lingbot_57500_1 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 / 0 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/007 | lingbot_57500_1 | apple_to_fruit_bowl | 007 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/008 | lingbot_57500_1 | apple_to_fruit_bowl | 008 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/009 | lingbot_57500_1 | apple_to_fruit_bowl | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/010 | lingbot_57500_1 | apple_to_fruit_bowl | 010 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/011 | lingbot_57500_1 | apple_to_fruit_bowl | 011 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/012 | lingbot_57500_1 | apple_to_fruit_bowl | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/013 | lingbot_57500_1 | apple_to_fruit_bowl | 013 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/014 | lingbot_57500_1 | apple_to_fruit_bowl | 014 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/015 | lingbot_57500_1 | apple_to_fruit_bowl | 015 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/016 | lingbot_57500_1 | apple_to_fruit_bowl | 016 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/017 | lingbot_57500_1 | apple_to_fruit_bowl | 017 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/018 | lingbot_57500_1 | apple_to_fruit_bowl | 018 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/019 | lingbot_57500_1 | apple_to_fruit_bowl | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/000 | lingbot_57500_1 | bookmark_on_book | 000 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/001 | lingbot_57500_1 | bookmark_on_book | 001 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/002 | lingbot_57500_1 | bookmark_on_book | 002 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/003 | lingbot_57500_1 | bookmark_on_book | 003 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/004 | lingbot_57500_1 | bookmark_on_book | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/005 | lingbot_57500_1 | bookmark_on_book | 005 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/006 | lingbot_57500_1 | bookmark_on_book | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/007 | lingbot_57500_1 | bookmark_on_book | 007 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/008 | lingbot_57500_1 | bookmark_on_book | 008 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/009 | lingbot_57500_1 | bookmark_on_book | 009 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/010 | lingbot_57500_1 | bookmark_on_book | 010 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/011 | lingbot_57500_1 | bookmark_on_book | 011 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/012 | lingbot_57500_1 | bookmark_on_book | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/013 | lingbot_57500_1 | bookmark_on_book | 013 | 1.000 | 1 | 1.000 / 1 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/014 | lingbot_57500_1 | bookmark_on_book | 014 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/015 | lingbot_57500_1 | bookmark_on_book | 015 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/016 | lingbot_57500_1 | bookmark_on_book | 016 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/017 | lingbot_57500_1 | bookmark_on_book | 017 | 1.000 | 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/018 | lingbot_57500_1 | bookmark_on_book | 018 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/bookmark_on_book/019 | lingbot_57500_1 | bookmark_on_book | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/000 | lingbot_57500_1 | collect_coffee_beans | 000 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/001 | lingbot_57500_1 | collect_coffee_beans | 001 | 0.500 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/002 | lingbot_57500_1 | collect_coffee_beans | 002 | 0.071 | 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/003 | lingbot_57500_1 | collect_coffee_beans | 003 | 0.429 | 0 | 0.000 / 0 | 1.000 / 1 | 0.357 / 0 | 0.857 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/004 | lingbot_57500_1 | collect_coffee_beans | 004 | 0.500 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/005 | lingbot_57500_1 | collect_coffee_beans | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/006 | lingbot_57500_1 | collect_coffee_beans | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/007 | lingbot_57500_1 | collect_coffee_beans | 007 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/008 | lingbot_57500_1 | collect_coffee_beans | 008 | 0.429 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/009 | lingbot_57500_1 | collect_coffee_beans | 009 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/010 | lingbot_57500_1 | collect_coffee_beans | 010 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/011 | lingbot_57500_1 | collect_coffee_beans | 011 | 0.357 | 0 | 0.000 / 0 | 0.857 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/012 | lingbot_57500_1 | collect_coffee_beans | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/013 | lingbot_57500_1 | collect_coffee_beans | 013 | 0.000 | 0 | 0.000 / 0 | 0.200 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/014 | lingbot_57500_1 | collect_coffee_beans | 014 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/015 | lingbot_57500_1 | collect_coffee_beans | 015 | 0.429 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/016 | lingbot_57500_1 | collect_coffee_beans | 016 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/017 | lingbot_57500_1 | collect_coffee_beans | 017 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 0.500 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/018 | lingbot_57500_1 | collect_coffee_beans | 018 | 1.000 | 1 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/019 | lingbot_57500_1 | collect_coffee_beans | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/000 | lingbot_57500_1 | detergent | 000 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/001 | lingbot_57500_1 | detergent | 001 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/002 | lingbot_57500_1 | detergent | 002 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/003 | lingbot_57500_1 | detergent | 003 | 0.667 | 0 | 0.000 / 0 | 1.000 / 1 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/004 | lingbot_57500_1 | detergent | 004 | 0.333 | 0 | 0.000 / 0 | 1.000 / 1 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/005 | lingbot_57500_1 | detergent | 005 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/detergent/006 | lingbot_57500_1 | detergent | 006 | 0.667 | 0 | 1.000 / 1 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/007 | lingbot_57500_1 | detergent | 007 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/detergent/008 | lingbot_57500_1 | detergent | 008 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/009 | lingbot_57500_1 | detergent | 009 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/010 | lingbot_57500_1 | detergent | 010 | 0.667 | 0 | 1.000 / 1 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/011 | lingbot_57500_1 | detergent | 011 | 0.000 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/012 | lingbot_57500_1 | detergent | 012 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/detergent/013 | lingbot_57500_1 | detergent | 013 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/014 | lingbot_57500_1 | detergent | 014 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/detergent/015 | lingbot_57500_1 | detergent | 015 | 0.000 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/016 | lingbot_57500_1 | detergent | 016 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/017 | lingbot_57500_1 | detergent | 017 | 1.000 | 1 | 0.000 / 0 | 1.000 / 1 | 1.000 / 1 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/detergent/018 | lingbot_57500_1 | detergent | 018 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/detergent/019 | lingbot_57500_1 | detergent | 019 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/000 | lingbot_57500_1 | put_glass_in_glassbox | 000 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/001 | lingbot_57500_1 | put_glass_in_glassbox | 001 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.000 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/002 | lingbot_57500_1 | put_glass_in_glassbox | 002 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/003 | lingbot_57500_1 | put_glass_in_glassbox | 003 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/004 | lingbot_57500_1 | put_glass_in_glassbox | 004 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/005 | lingbot_57500_1 | put_glass_in_glassbox | 005 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/006 | lingbot_57500_1 | put_glass_in_glassbox | 006 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/007 | lingbot_57500_1 | put_glass_in_glassbox | 007 | 0.333 | 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/008 | lingbot_57500_1 | put_glass_in_glassbox | 008 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/009 | lingbot_57500_1 | put_glass_in_glassbox | 009 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/010 | lingbot_57500_1 | put_glass_in_glassbox | 010 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/011 | lingbot_57500_1 | put_glass_in_glassbox | 011 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/012 | lingbot_57500_1 | put_glass_in_glassbox | 012 | 1.000 | 1 | 0.000 / 0 | 0.667 / 0 | 0.667 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/013 | lingbot_57500_1 | put_glass_in_glassbox | 013 | 0.333 | 0 | 0.667 / 0 | 0.667 / 0 | 0.000 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/014 | lingbot_57500_1 | put_glass_in_glassbox | 014 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/015 | lingbot_57500_1 | put_glass_in_glassbox | 015 | 0.333 | 0 | 1.000 / 1 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/016 | lingbot_57500_1 | put_glass_in_glassbox | 016 | 0.667 | 0 | 0.000 / 0 | 0.667 / 0 | 0.000 / 0 | 0.667 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/017 | lingbot_57500_1 | put_glass_in_glassbox | 017 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/018 | lingbot_57500_1 | put_glass_in_glassbox | 018 | 0.333 | 0 | 0.000 / 0 | 0.333 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/019 | lingbot_57500_1 | put_glass_in_glassbox | 019 | 0.333 | 0 | 0.000 / 0 | 0.667 / 0 | 0.333 / 0 | 0.333 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/000 | lingbot_57500_1 | utensils_to_holder | 000 | 1.000 | 1 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 1.000 / 1 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/001 | lingbot_57500_1 | utensils_to_holder | 001 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/002 | lingbot_57500_1 | utensils_to_holder | 002 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/003 | lingbot_57500_1 | utensils_to_holder | 003 | 0.500 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/004 | lingbot_57500_1 | utensils_to_holder | 004 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/005 | lingbot_57500_1 | utensils_to_holder | 005 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/006 | lingbot_57500_1 | utensils_to_holder | 006 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/007 | lingbot_57500_1 | utensils_to_holder | 007 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/008 | lingbot_57500_1 | utensils_to_holder | 008 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/009 | lingbot_57500_1 | utensils_to_holder | 009 | 0.000 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/010 | lingbot_57500_1 | utensils_to_holder | 010 | 0.000 | 0 | 1.000 / 1 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/011 | lingbot_57500_1 | utensils_to_holder | 011 | 0.000 | 0 | 1.000 / 1 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/012 | lingbot_57500_1 | utensils_to_holder | 012 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/013 | lingbot_57500_1 | utensils_to_holder | 013 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/014 | lingbot_57500_1 | utensils_to_holder | 014 | 0.000 | 0 | 0.000 / 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/015 | lingbot_57500_1 | utensils_to_holder | 015 | 0.000 | 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 | 0.000 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/016 | lingbot_57500_1 | utensils_to_holder | 016 | 0.500 | 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/017 | lingbot_57500_1 | utensils_to_holder | 017 | 0.500 | 0 | 0.000 / 0 | 0.000 / 0 | 0.500 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/018 | lingbot_57500_1 | utensils_to_holder | 018 | 0.500 | 0 | 1.000 / 1 | 0.000 / 0 | 0.000 / 0 | 0.500 / 0 |
| lingbot_57500_1/lingbot_57500_1/utensils_to_holder/019 | lingbot_57500_1 | utensils_to_holder | 019 | 0.000 | 0 | 0.000 / 0 | 0.000 / 0 | 0.500 / 0 | 0.000 / 0 |

## 与仿真不一致的条目

| model | episode_path | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | reason |
|---|---|---|---|---:|---:|---:|---:|---|
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/000 | apple_to_fruit_bowl | 000 | 0.000 | 0 | 1.000 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/001 | apple_to_fruit_bowl | 001 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/003 | apple_to_fruit_bowl | 003 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/004 | apple_to_fruit_bowl | 004 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/006 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 | 0 | No frames provided for evaluation. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/007 | apple_to_fruit_bowl | 007 | 1.000 | 1 | 0.000 | 0 | No visual evidence is provided; the required final state cannot be confirmed. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/008 | apple_to_fruit_bowl | 008 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/009 | apple_to_fruit_bowl | 009 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/011 | apple_to_fruit_bowl | 011 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/013 | apple_to_fruit_bowl | 013 | 1.000 | 1 | 0.000 | 0 | No visible evidence of the apple inside the fruit bowl. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/014 | apple_to_fruit_bowl | 014 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/016 | apple_to_fruit_bowl | 016 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/017 | apple_to_fruit_bowl | 017 | 0.000 | 0 | 1.000 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/018 | apple_to_fruit_bowl | 018 | 0.000 | 0 | 1.000 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/bookmark_on_book/000 | bookmark_on_book | 000 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/bookmark_on_book/008 | bookmark_on_book | 008 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/bookmark_on_book/011 | bookmark_on_book | 011 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/bookmark_on_book/015 | bookmark_on_book | 015 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/bookmark_on_book/019 | bookmark_on_book | 019 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/005 | collect_coffee_beans | 005 | 0.000 | 0 | 1.000 | 1 | Lid is placed on the jar and all 7 coffee beans are visible inside the jar. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/007 | collect_coffee_beans | 007 | 0.000 | 0 | 1.000 | 1 | The lid is placed on the jar and all 7 coffee beans are inside the jar. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/detergent/001 | detergent | 001 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/detergent/002 | detergent | 002 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/detergent/003 | detergent | 003 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/detergent/004 | detergent | 004 | 0.000 | 0 | 1.000 | 1 | All three detergent items are visibly placed in the basket. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/detergent/008 | detergent | 008 | 0.000 | 0 | 1.000 | 1 | All three detergent bottles are visibly placed in the target container. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/put_glass_in_glassbox/001 | put_glass_in_glassbox | 001 | 0.333 | 0 | 1.000 | 1 | The glasses are inside the box, both temples are folded, and the box is closed. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/utensils_to_holder/000 | utensils_to_holder | 000 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/utensils_to_holder/008 | utensils_to_holder | 008 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/utensils_to_holder/013 | utensils_to_holder | 013 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | cosmos_test_50k/cosmos_test_50k/utensils_to_holder/015 | utensils_to_holder | 015 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/apple_to_fruit_bowl/006 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 | 0 | No frames are visible to evaluate; the required final state cannot be confirmed. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/apple_to_fruit_bowl/007 | apple_to_fruit_bowl | 007 | 1.000 | 1 | 0.000 | 0 | The apple is not visibly inside the fruit bowl in the provided frames. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/apple_to_fruit_bowl/009 | apple_to_fruit_bowl | 009 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/apple_to_fruit_bowl/010 | apple_to_fruit_bowl | 010 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/apple_to_fruit_bowl/014 | apple_to_fruit_bowl | 014 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/apple_to_fruit_bowl/019 | apple_to_fruit_bowl | 019 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/002 | bookmark_on_book | 002 | 1.000 | 1 | 0.000 | 0 | No frames were provided to evaluate the bookmark placement. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/007 | bookmark_on_book | 007 | 1.000 | 1 | 0.000 | 0 | No images provided; cannot verify if the bookmark is placed on the book with sufficient overlap. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/010 | bookmark_on_book | 010 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/011 | bookmark_on_book | 011 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/013 | bookmark_on_book | 013 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/015 | bookmark_on_book | 015 | 0.000 | 0 | 1.000 | 1 | The bookmark is placed on the book with full visible overlap. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/016 | bookmark_on_book | 016 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/018 | bookmark_on_book | 018 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/bookmark_on_book/019 | bookmark_on_book | 019 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied because no image data was provided. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/collect_coffee_beans/000 | collect_coffee_beans | 000 | 0.143 | 0 | 1.000 | 1 | The lid is placed on the jar and all 7 coffee beans are visible inside the jar. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/collect_coffee_beans/011 | collect_coffee_beans | 011 | 0.214 | 0 | 1.000 | 1 | The lid is correctly placed on the jar and all 7 coffee beans are clearly visible inside the jar at the end of the rollout. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/collect_coffee_beans/016 | collect_coffee_beans | 016 | 0.000 | 0 | 1.000 | 1 | The lid is on the jar and all 7 coffee beans are inside the jar. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/000 | detergent | 000 | 1.000 | 1 | 0.000 | 0 | No visible evidence of detergent items being completed. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/001 | detergent | 001 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/003 | detergent | 003 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/004 | detergent | 004 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/005 | detergent | 005 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/006 | detergent | 006 | 1.000 | 1 | 0.000 | 0 | Unable to evaluate: no visual frames provided. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/007 | detergent | 007 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/008 | detergent | 008 | 1.000 | 1 | 0.000 | 0 | No detergent items are visibly completed in the provided frames. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/010 | detergent | 010 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/011 | detergent | 011 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/013 | detergent | 013 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/015 | detergent | 015 | 1.000 | 1 | 0.000 | 0 | No visible evidence of completed detergent items. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/016 | detergent | 016 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/detergent/017 | detergent | 017 | 1.000 | 1 | 0.000 | 0 | No image frames were provided for evaluation. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/put_glass_in_glassbox/002 | put_glass_in_glassbox | 002 | 1.000 | 1 | 0.000 | 0 | No visual evidence available to evaluate the frames. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/put_glass_in_glassbox/007 | put_glass_in_glassbox | 007 | 0.000 | 0 | 1.000 | 1 | Both temples are folded, the glasses are placed inside the box, and the box lid is closed. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/put_glass_in_glassbox/011 | put_glass_in_glassbox | 011 | 1.000 | 1 | 0.000 | 0 | No image frames were provided for evaluation. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/put_glass_in_glassbox/012 | put_glass_in_glassbox | 012 | 1.000 | 1 | 0.000 | 0 | No images were provided for evaluation, so no conditions could be confirmed. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/put_glass_in_glassbox/013 | put_glass_in_glassbox | 013 | 1.000 | 1 | 0.000 | 0 | No image frames provided for evaluation. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/put_glass_in_glassbox/018 | put_glass_in_glassbox | 018 | 1.000 | 1 | 0.000 | 0 | No frames were provided for evaluation; cannot determine if any conditions are satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/001 | utensils_to_holder | 001 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/002 | utensils_to_holder | 002 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/003 | utensils_to_holder | 003 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/005 | utensils_to_holder | 005 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/008 | utensils_to_holder | 008 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/011 | utensils_to_holder | 011 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/012 | utensils_to_holder | 012 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/013 | utensils_to_holder | 013 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | ebench-test_step_h30/utensils_to_holder/015 | utensils_to_holder | 015 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/004 | apple_to_fruit_bowl | 004 | 1.000 | 1 | 0.000 | 0 | No frames provided; cannot assess if apple is in fruit bowl. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/005 | apple_to_fruit_bowl | 005 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/006 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied because no image frames were provided for evaluation. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/011 | apple_to_fruit_bowl | 011 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/014 | apple_to_fruit_bowl | 014 | 1.000 | 1 | 0.000 | 0 | The apple is not visible inside the fruit bowl at the end of the rollout. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/015 | apple_to_fruit_bowl | 015 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/017 | apple_to_fruit_bowl | 017 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/018 | apple_to_fruit_bowl | 018 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/000 | bookmark_on_book | 000 | 1.000 | 1 | 0.000 | 0 | No visual evidence of the final state is provided; the input frames are not visible to the evaluator. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/001 | bookmark_on_book | 001 | 1.000 | 1 | 0.000 | 0 | No visible frames provided to evaluate the final state. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/003 | bookmark_on_book | 003 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/005 | bookmark_on_book | 005 | 1.000 | 1 | 0.000 | 0 | No images were provided to assess the final state. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/007 | bookmark_on_book | 007 | 1.000 | 1 | 0.000 | 0 | No visible evidence provided; the image frames are not accessible to the evaluator. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/008 | bookmark_on_book | 008 | 0.000 | 0 | 1.000 | 1 | The bookmark is placed on the book with visible overlap exceeding 40%. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/009 | bookmark_on_book | 009 | 1.000 | 1 | 0.000 | 0 | No visible evidence provided; cannot determine if bookmark is on book. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/011 | bookmark_on_book | 011 | 1.000 | 1 | 0.000 | 0 | The provided frames do not contain visible evidence of the bookmark on the book. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/014 | bookmark_on_book | 014 | 0.000 | 0 | 1.000 | 1 | The bookmark is placed entirely on the book with clear full overlap in the final frame. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/015 | bookmark_on_book | 015 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/016 | bookmark_on_book | 016 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/017 | bookmark_on_book | 017 | 1.000 | 1 | 0.000 | 0 | No frames provided to evaluate. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/010 | collect_coffee_beans | 010 | 0.000 | 0 | 1.000 | 1 | The lid is visibly placed on the jar and all 7 coffee beans are inside the jar. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/016 | collect_coffee_beans | 016 | 1.000 | 1 | 0.000 | 0 | No visible evidence of lid on jar or beans inside jar. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/017 | collect_coffee_beans | 017 | 1.000 | 1 | 0.000 | 0 | No frames provided to evaluate the rollout. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/018 | collect_coffee_beans | 018 | 1.000 | 1 | 0.000 | 0 | Images not provided; cannot evaluate. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/detergent/005 | detergent | 005 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/detergent/006 | detergent | 006 | 0.667 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/detergent/007 | detergent | 007 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/detergent/010 | detergent | 010 | 0.667 | 0 | 1.000 | 1 | All three detergent bottles are visibly placed in the bin. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/detergent/014 | detergent | 014 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/detergent/017 | detergent | 017 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/012 | put_glass_in_glassbox | 012 | 1.000 | 1 | 0.000 | 0 | No video frames were provided for evaluation. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/015 | put_glass_in_glassbox | 015 | 0.333 | 0 | 1.000 | 1 | Both temples are folded, the glasses are inside the box, and the box is fully closed. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/utensils_to_holder/000 | utensils_to_holder | 000 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/utensils_to_holder/010 | utensils_to_holder | 010 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/utensils_to_holder/011 | utensils_to_holder | 011 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| bailian/deepseek-v4-pro | lingbot_57500_1/lingbot_57500_1/utensils_to_holder/018 | utensils_to_holder | 018 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/002 | apple_to_fruit_bowl | 002 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/009 | apple_to_fruit_bowl | 009 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/010 | apple_to_fruit_bowl | 010 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/013 | apple_to_fruit_bowl | 013 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/bookmark_on_book/002 | bookmark_on_book | 002 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/bookmark_on_book/007 | bookmark_on_book | 007 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/collect_coffee_beans/012 | collect_coffee_beans | 012 | 0.286 | 0 | 1.000 | 1 | The robot successfully collected all seven coffee beans into the jar and placed the lid flat on top. |
| gemini-3.5-flash | cosmos_test_50k/cosmos_test_50k/detergent/018 | detergent | 018 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/001 | apple_to_fruit_bowl | 001 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/002 | apple_to_fruit_bowl | 002 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/004 | apple_to_fruit_bowl | 004 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/006 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/008 | apple_to_fruit_bowl | 008 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/016 | apple_to_fruit_bowl | 016 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/018 | apple_to_fruit_bowl | 018 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/apple_to_fruit_bowl/019 | apple_to_fruit_bowl | 019 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | ebench-test_step_h30/collect_coffee_beans/004 | collect_coffee_beans | 004 | 0.500 | 0 | 1.000 | 1 | The robot successfully collected all seven coffee beans into the jar and placed the lid on top. |
| gemini-3.5-flash | ebench-test_step_h30/collect_coffee_beans/013 | collect_coffee_beans | 013 | 0.500 | 0 | 1.000 | 1 | The lid is successfully placed on the jar containing all seven coffee beans. |
| gemini-3.5-flash | ebench-test_step_h30/put_glass_in_glassbox/000 | put_glass_in_glassbox | 000 | 0.333 | 0 | 1.000 | 1 | The glasses are placed inside the box with both temples folded, and the box is closed. |
| gemini-3.5-flash | ebench-test_step_h30/put_glass_in_glassbox/009 | put_glass_in_glassbox | 009 | 0.000 | 0 | 1.000 | 1 | The robot successfully placed the glasses inside the box, folded both temples, and closed the box. |
| gemini-3.5-flash | ebench-test_step_h30/put_glass_in_glassbox/013 | put_glass_in_glassbox | 013 | 1.000 | 1 | 0.667 | 0 | The glasses are placed inside the box with folded temples, but the box is not fully closed. |
| gemini-3.5-flash | ebench-test_step_h30/put_glass_in_glassbox/016 | put_glass_in_glassbox | 016 | 1.000 | 1 | 0.667 | 0 | The glasses are inside the closed box, but the temples were not folded. |
| gemini-3.5-flash | ebench-test_step_h30/put_glass_in_glassbox/018 | put_glass_in_glassbox | 018 | 1.000 | 1 | 0.667 | 0 | The glasses are inside the box and the box is closed, but both temples were not visibly folded. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/000 | apple_to_fruit_bowl | 000 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/004 | apple_to_fruit_bowl | 004 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/006 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/apple_to_fruit_bowl/016 | apple_to_fruit_bowl | 016 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/017 | bookmark_on_book | 017 | 1.000 | 1 | 0.000 | 0 | The bookmark is not placed on the book. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/001 | collect_coffee_beans | 001 | 0.500 | 0 | 1.000 | 1 | The robot successfully collected all seven coffee beans into the jar and placed the lid on it. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/003 | collect_coffee_beans | 003 | 0.429 | 0 | 1.000 | 1 | The robot successfully collected all seven coffee beans into the jar and placed the lid on top. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/004 | collect_coffee_beans | 004 | 0.500 | 0 | 1.000 | 1 | The lid is successfully placed on the jar and all seven coffee beans are collected inside. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/008 | collect_coffee_beans | 008 | 0.429 | 0 | 1.000 | 1 | The lid is successfully placed on the jar with all seven coffee beans collected inside. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/015 | collect_coffee_beans | 015 | 0.429 | 0 | 1.000 | 1 | The robot successfully collected all seven coffee beans into the jar and placed the lid on top. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/018 | collect_coffee_beans | 018 | 1.000 | 1 | 0.000 | 0 | At the end of the rollout, the lid is on the table and the coffee beans are not visibly inside the jar. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/detergent/003 | detergent | 003 | 0.667 | 0 | 1.000 | 1 | All three detergent items are successfully placed inside the basket. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/detergent/004 | detergent | 004 | 0.333 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/012 | put_glass_in_glassbox | 012 | 1.000 | 1 | 0.667 | 0 | The glasses are inside the closed box, but the temples were not folded. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/utensils_to_holder/000 | utensils_to_holder | 000 | 1.000 | 1 | 0.500 | 0 | The spoon is successfully placed on the holder, but the fork remains held by the gripper at the end of the rollout. |
| gemini-3.5-flash | lingbot_57500_1/lingbot_57500_1/utensils_to_holder/014 | utensils_to_holder | 014 | 0.000 | 0 | 1.000 | 1 | Both the spoon and the fork are successfully placed on the holder. |
| gpt-5 | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/006 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 | 0 | The final frames show the apple near or on the rim of the bowl, not clearly placed inside. |
| gpt-5 | ebench-test_step_h30/apple_to_fruit_bowl/002 | apple_to_fruit_bowl | 002 | 1.000 | 1 | 0.000 | 0 | The apple is held above the bowl at the end and is not visibly inside it. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/002 | bookmark_on_book | 002 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the table next to the book with no visible overlap. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/004 | bookmark_on_book | 004 | 1.000 | 1 | 0.000 | 0 | The bookmark remains off to the side in the gripper and is not placed on the open book. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/005 | bookmark_on_book | 005 | 1.000 | 1 | 0.000 | 0 | The bookmark does not appear on top of the book; the book’s pages are visible without a significant overlapping bookmark. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/007 | bookmark_on_book | 007 | 1.000 | 1 | 0.000 | 0 | The tan bookmark is not on the book; a grey tool is placed on the book instead. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/011 | bookmark_on_book | 011 | 1.000 | 1 | 0.000 | 0 | The bookmark is not on the book; the open book remains clear with no visible overlap. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/013 | bookmark_on_book | 013 | 1.000 | 1 | 0.000 | 0 | The bookmark ends up on a gray surface near the robot, not on the book, so there is no visible overlap. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/017 | bookmark_on_book | 017 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the desk beside the book with no visible overlap. |
| gpt-5 | ebench-test_step_h30/bookmark_on_book/019 | bookmark_on_book | 019 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the desk and not on the book, with no visible overlap. |
| gpt-5 | ebench-test_step_h30/detergent/001 | detergent | 001 | 1.000 | 1 | 0.667 | 0 | Two detergent items are visibly placed in the basket, while the third is not clearly completed. |
| gpt-5 | ebench-test_step_h30/detergent/014 | detergent | 014 | 1.000 | 1 | 0.667 | 0 | Two detergent bottles are visibly placed inside the basket, while the third is not visibly completed. |
| gpt-5 | ebench-test_step_h30/put_glass_in_glassbox/002 | put_glass_in_glassbox | 002 | 1.000 | 1 | 0.667 | 0 | The glasses are placed inside the box and the box is closed, but one temple remains unfolded. |
| gpt-5 | ebench-test_step_h30/put_glass_in_glassbox/011 | put_glass_in_glassbox | 011 | 1.000 | 1 | 0.667 | 0 | The glasses are placed inside the box and the box is closed, but both temples are not visibly folded. |
| gpt-5 | ebench-test_step_h30/put_glass_in_glassbox/012 | put_glass_in_glassbox | 012 | 1.000 | 1 | 0.667 | 0 | The glasses are visibly inside the box and the box is closed, but both temples remain unfolded. |
| gpt-5 | ebench-test_step_h30/put_glass_in_glassbox/013 | put_glass_in_glassbox | 013 | 1.000 | 1 | 0.333 | 0 | The box is closed in the final frames, but the glasses are not inside and the temples are not folded. |
| gpt-5 | ebench-test_step_h30/put_glass_in_glassbox/016 | put_glass_in_glassbox | 016 | 1.000 | 1 | 0.667 | 0 | The glasses were placed inside and the box was closed, but both temples are not visibly folded. |
| gpt-5 | ebench-test_step_h30/put_glass_in_glassbox/018 | put_glass_in_glassbox | 018 | 1.000 | 1 | 0.667 | 0 | The box is closed with the glasses inside, but both temples are not visibly folded. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/000 | bookmark_on_book | 000 | 1.000 | 1 | 0.000 | 0 | The pink bookmark remains on the table beside the open book with no visible overlap. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/001 | bookmark_on_book | 001 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the table beside the book without visible overlap. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/003 | bookmark_on_book | 003 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the table separate from the book, with no visible overlap. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/005 | bookmark_on_book | 005 | 1.000 | 1 | 0.000 | 0 | The bookmark is not on the book at the end; it remains off the book with no significant overlap. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/007 | bookmark_on_book | 007 | 1.000 | 1 | 0.000 | 0 | The bookmark is not visibly placed on the book; no substantial overlap is seen. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/009 | bookmark_on_book | 009 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the table/robot surface and is not placed on the open book. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/011 | bookmark_on_book | 011 | 1.000 | 1 | 0.000 | 0 | The pink bookmark remains on the table and is not on top of the book. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/013 | bookmark_on_book | 013 | 1.000 | 1 | 0.000 | 0 | The bookmark is not on the book; it remains off to the side and not overlapping the book. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/017 | bookmark_on_book | 017 | 1.000 | 1 | 0.000 | 0 | The bookmark is not placed on the open book; no visible overlap between them. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/016 | collect_coffee_beans | 016 | 1.000 | 1 | 0.000 | 0 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/017 | collect_coffee_beans | 017 | 1.000 | 1 | 0.500 | 0 | The lid is not on the jar at the end, and all seven coffee beans are visibly inside the jar. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/018 | collect_coffee_beans | 018 | 1.000 | 1 | 0.000 | 0 | At the end the lid is not on the jar and no coffee beans are visibly inside the jar. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/put_glass_in_glassbox/012 | put_glass_in_glassbox | 012 | 1.000 | 1 | 0.667 | 0 | The box is closed with the glasses inside, but both temples are not visibly folded. |
| gpt-5 | lingbot_57500_1/lingbot_57500_1/utensils_to_holder/000 | utensils_to_holder | 000 | 1.000 | 1 | 0.500 | 0 | The wooden spoon is on the holder, but the fork remains off the holder and in the gripper/on the table. |
| gpt-5.5 | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/006 | apple_to_fruit_bowl | 006 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gpt-5.5 | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/009 | apple_to_fruit_bowl | 009 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gpt-5.5 | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/010 | apple_to_fruit_bowl | 010 | 0.000 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gpt-5.5 | cosmos_test_50k/cosmos_test_50k/apple_to_fruit_bowl/013 | apple_to_fruit_bowl | 013 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gpt-5.5 | ebench-test_step_h30/bookmark_on_book/002 | bookmark_on_book | 002 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the table beside the book rather than overlapping it. |
| gpt-5.5 | ebench-test_step_h30/bookmark_on_book/003 | bookmark_on_book | 003 | 1.000 | 1 | 0.000 | 0 | The bookmark is not visibly placed on the book with sufficient overlap in the final state. |
| gpt-5.5 | ebench-test_step_h30/bookmark_on_book/017 | bookmark_on_book | 017 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gpt-5.5 | ebench-test_step_h30/bookmark_on_book/019 | bookmark_on_book | 019 | 1.000 | 1 | 0.000 | 0 | The bookmark remains on the table beside the book rather than visibly overlapping it. |
| gpt-5.5 | ebench-test_step_h30/collect_coffee_beans/004 | collect_coffee_beans | 004 | 0.500 | 0 | 1.000 | 1 | The lid is visibly on the jar and all seven coffee beans were collected inside before the jar was closed. |
| gpt-5.5 | ebench-test_step_h30/put_glass_in_glassbox/016 | put_glass_in_glassbox | 016 | 1.000 | 1 | 0.667 | 0 | The glasses were placed in the box and the box was closed, but both temples were not visibly folded. |
| gpt-5.5 | ebench-test_step_h30/put_glass_in_glassbox/018 | put_glass_in_glassbox | 018 | 1.000 | 1 | 0.667 | 0 | The glasses are visibly placed in the box and the box is closed, but both temples are not clearly folded. |
| gpt-5.5 | ebench-test_step_h30/utensils_to_holder/005 | utensils_to_holder | 005 | 0.500 | 0 | 1.000 | 1 | The required final state is visibly satisfied. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/000 | bookmark_on_book | 000 | 1.000 | 1 | 0.000 | 0 | The bookmark remains beside the book rather than visibly on top with sufficient overlap. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/001 | bookmark_on_book | 001 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/007 | bookmark_on_book | 007 | 1.000 | 1 | 0.000 | 0 | The bookmark is not visibly placed on the book with sufficient overlap. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/009 | bookmark_on_book | 009 | 1.000 | 1 | 0.000 | 0 | The bookmark appears to still be held or only partially positioned near the book, so the required final state is not visibly satisfied. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/011 | bookmark_on_book | 011 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/bookmark_on_book/017 | bookmark_on_book | 017 | 1.000 | 1 | 0.000 | 0 | The required final state is not visibly satisfied. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/001 | collect_coffee_beans | 001 | 0.500 | 0 | 1.000 | 1 | The lid is visibly on the jar and all seven coffee beans were collected inside before it was closed. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/015 | collect_coffee_beans | 015 | 0.429 | 0 | 1.000 | 1 | The lid is visibly placed on the jar and all seven coffee beans were collected inside the jar. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/016 | collect_coffee_beans | 016 | 1.000 | 1 | 0.500 | 0 | All seven beans appear to be inside the jar, but the lid is not on the jar at the end. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/017 | collect_coffee_beans | 017 | 1.000 | 1 | 0.500 | 0 | All seven beans are visible in the jar, but the lid is tilted and not properly centered on the jar. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/018 | collect_coffee_beans | 018 | 1.000 | 1 | 0.500 | 0 | All seven beans are visible inside the jar, but the lid is left off the jar. |
| gpt-5.5 | lingbot_57500_1/lingbot_57500_1/detergent/012 | detergent | 012 | 0.667 | 0 | 1.000 | 1 | All three detergent items are visibly placed inside the basket. |

## 初步结论

- success 一致率最高: `gpt-5.5` (0.933)。
- 连续分数 Pearson 最高: `gpt-5.5` (0.817)。
- 连续分数 MAE 最低: `gpt-5.5` (0.083)。
- 综合 success 一致率、连续分数相关性、MAE 和视觉可用性，当前更建议把 `gpt-5.5` 作为主参考模型。
- 模型最常与 sim 不一致的 rollout: `ebench-test_step_h30/put_glass_in_glassbox/018` (4), `lingbot_57500_1/lingbot_57500_1/bookmark_on_book/017` (4), `lingbot_57500_1/lingbot_57500_1/collect_coffee_beans/018` (4)。
