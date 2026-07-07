# GPT Rollout Score Report

- num_rollouts: 10
- scored_rollouts: 10
- failed_rollouts: 0
- agreement_rate: 0.900

| task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | frame_mode | cameras |
|---|---|---:|---:|---:|---:|---:|---|---|
| apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| collect_coffee_beans | 001 | 0.5 | 0 | 0.357143 | 0 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| detergent | 001 | 1.0 | 1 | 1 | 1 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| put_glass_in_glassbox | 002 | 1.0 | 1 | 0.666667 | 0 | 0 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| put_glass_in_glassbox | 010 | 0.0 | 0 | 0.333333 | 0 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |
| utensils_to_holder | 001 | 0.5 | 0 | 0.5 | 0 | 1 | synced_camera_composite | top_camera.mp4,overlook_camera.mp4,left_camera.mp4,right_camera.mp4 |

## Mismatches

- put_glass_in_glassbox/002: sim_success=1, vlm_success=0, vlm_score=0.6666666667
