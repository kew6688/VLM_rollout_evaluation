# GPT Rollout Score Report

- num_rollouts: 10
- scored_rollouts: 10
- failed_rollouts: 0
- agreement_rate: 0.600

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| qwen-max | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple is not inside the fruit bowl in the final frame. | 51 | 1 | 1 | synced_camera_composite |
| qwen-max | apple_to_fruit_bowl | 002 | 1.0 | 1 | 0 | 0 | 0 | The apple is not inside the fruit bowl in the final frame. | 11 | 1 | 1 | synced_camera_composite |
| qwen-max | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book with at least 40% visible overlap. | 51 | 1 | 1 | synced_camera_composite |
| qwen-max | bookmark_on_book | 004 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not placed on the book with at least 40% visible overlap. | 11 | 1 | 1 | synced_camera_composite |
| qwen-max | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are inside the jar. | 117 | 1 | 1 | synced_camera_composite |
| qwen-max | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are inside the jar. | 117 | 1 | 1 | synced_camera_composite |
| qwen-max | detergent | 001 | 1.0 | 1 | 0 | 0 | 0 | No detergent items are visibly completed in the frame. | 74 | 1 | 1 | synced_camera_composite |
| qwen-max | put_glass_in_glassbox | 002 | 1.0 | 1 | 0 | 0 | 0 | The glasses are not inside the box, the temples are not folded, and the box is not closed. | 76 | 1 | 1 | synced_camera_composite |
| qwen-max | put_glass_in_glassbox | 010 | 0.0 | 0 | 0 | 0 | 1 | The glasses are not inside the box, the temples are not folded, and the box is not closed. | 101 | 1 | 1 | synced_camera_composite |
| qwen-max | utensils_to_holder | 001 | 0.5 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is on the holder. | 67 | 1 | 1 | synced_camera_composite |

## Mismatches

- apple_to_fruit_bowl/002: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/004: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/001: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/002: sim_success=1, vlm_success=0, vlm_score=0.0
