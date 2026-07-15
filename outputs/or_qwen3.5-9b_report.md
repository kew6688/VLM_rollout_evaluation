# GPT Rollout Score Report

- num_rollouts: 10
- scored_rollouts: 10
- failed_rollouts: 0
- agreement_rate: 0.900

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| or/qwen3.5-9b | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple is not placed inside the fruit bowl at the end of the rollout. | 51 | 10 | 50 | synced_camera_composite |
| or/qwen3.5-9b | apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl in the final frames. | 11 | 11 | 50 | synced_camera_composite |
| or/qwen3.5-9b | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table next to the book throughout the video and is never placed on the book. | 51 | 50 | 50 | synced_camera_composite |
| or/qwen3.5-9b | bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the book with significant overlap in the final frame. | 11 | 11 | 50 | synced_camera_composite |
| or/qwen3.5-9b | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | The lid is held by the robot arm and never placed on the jar, and the coffee beans remain on the table and are not collected into the jar. | 117 | 50 | 50 | synced_camera_composite |
| or/qwen3.5-9b | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | The lid is not on the jar and the coffee beans are not visibly inside the jar. | 117 | 50 | 50 | synced_camera_composite |
| or/qwen3.5-9b | detergent | 001 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket in the final frames. | 74 | 50 | 50 | synced_camera_composite |
| or/qwen3.5-9b | put_glass_in_glassbox | 002 | 1.0 | 1 | 1 | 1 | 1 | The glasses are placed inside the box, the temples are folded, and the box is closed. | 76 | 50 | 50 | synced_camera_composite |
| or/qwen3.5-9b | put_glass_in_glassbox | 010 | 0.0 | 0 | 1 | 1 | 0 | The final frames show the glasses box is closed, the glasses are inside the box, and the temples were folded during the placement process. | 101 | 50 | 50 | synced_camera_composite |
| or/qwen3.5-9b | utensils_to_holder | 001 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is placed on the holder, but the spoon remains on the counter. | 67 | 50 | 50 | synced_camera_composite |

## Mismatches

- put_glass_in_glassbox/010: sim_success=0, vlm_success=1, vlm_score=1.0
