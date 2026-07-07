# GPT Rollout Score Report

- num_rollouts: 10
- scored_rollouts: 10
- failed_rollouts: 0
- agreement_rate: 0.700

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| grok-4 | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table throughout and is never placed inside the fruit bowl. | 51 | 50 | 50 | synced_camera_composite |
| grok-4 | apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 11 | 11 | 50 | synced_camera_composite |
| grok-4 | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is never placed on the book with visible overlap. | 51 | 50 | 50 | synced_camera_composite |
| grok-4 | bookmark_on_book | 004 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not placed on the book with visible overlap in any final frame. | 11 | 11 | 50 | synced_camera_composite |
| grok-4 | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | Lid is off the jar and zero beans are visibly inside the jar in final frames. | 117 | 50 | 50 | synced_camera_composite |
| grok-4 | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | Lid is off the jar and zero beans are inside at the end. | 117 | 50 | 50 | synced_camera_composite |
| grok-4 | detergent | 001 | 1.0 | 1 | 0.666667 | 0 | 0 | Two weighted sub-conditions are visibly satisfied. | 74 | 50 | 50 | synced_camera_composite |
| grok-4 | put_glass_in_glassbox | 002 | 1.0 | 1 | 0 | 0 | 0 | Final frames show open empty box with glasses outside on table and temples unfolded. | 76 | 50 | 50 | synced_camera_composite |
| grok-4 | put_glass_in_glassbox | 010 | 0.0 | 0 | 0 | 0 | 1 | Glasses remain outside the open box with temples unfolded in final frames. | 101 | 50 | 50 | synced_camera_composite |
| grok-4 | utensils_to_holder | 001 | 0.5 | 0 | 0.5 | 0 | 1 | Exactly one half-credit condition is visibly satisfied. | 67 | 50 | 50 | synced_camera_composite |

## Mismatches

- bookmark_on_book/004: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/001: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/002: sim_success=1, vlm_success=0, vlm_score=0.0
