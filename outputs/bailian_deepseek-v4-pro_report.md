# GPT Rollout Score Report

- num_rollouts: 10
- scored_rollouts: 10
- failed_rollouts: 0
- agreement_rate: 0.900

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided; cannot visually verify the apple's final position. | 51 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. | 11 | 11 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | No visible evidence provided; frames are not accessible. | 51 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 11 | 11 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | No image data provided; cannot assess task completion from visible evidence. | 117 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | No video frames provided; cannot evaluate task. | 117 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 001 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 74 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 002 | 1.0 | 1 | 0 | 0 | 0 | No video frames were provided; unable to evaluate the robot policy rollout. | 76 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 010 | 0.0 | 0 | 0 | 0 | 1 | No frames provided for evaluation. | 101 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 001 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 67 | 50 | 50 | synced_camera_composite |

## Mismatches

- put_glass_in_glassbox/002: sim_success=1, vlm_success=0, vlm_score=0.0
