# GPT Rollout Score Report

- num_rollouts: 10
- scored_rollouts: 10
- failed_rollouts: 0
- agreement_rate: 0.500

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| gemini-2.5-flash | apple_to_fruit_bowl | 001 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly placed inside the fruit bowl at the end of the rollout. | 51 | 50 | 50 | synced_camera_composite |
| gemini-2.5-flash | apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end of the rollout. | 11 | 11 | 50 | synced_camera_composite |
| gemini-2.5-flash | bookmark_on_book | 000 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly placed on the open book with significant overlap. | 51 | 50 | 50 | synced_camera_composite |
| gemini-2.5-flash | bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the book with significant overlap. | 11 | 11 | 50 | synced_camera_composite |
| gemini-2.5-flash | collect_coffee_beans | 000 | 0.14286 | 0 | 0.214286 | 0 | 1 | The lid was not placed on the jar, and only 3 out of 7 coffee beans were collected into the jar. | 117 | 50 | 50 | synced_camera_composite |
| gemini-2.5-flash | collect_coffee_beans | 001 | 0.5 | 0 | 0.5 | 0 | 1 | The lid is not on the jar, but all 7 coffee beans are visibly inside the jar. | 117 | 50 | 50 | synced_camera_composite |
| gemini-2.5-flash | detergent | 001 | 1.0 | 1 | 0.666667 | 0 | 0 | Two weighted sub-conditions are visibly satisfied. | 74 | 50 | 50 | synced_camera_composite |
| gemini-2.5-flash | put_glass_in_glassbox | 002 | 1.0 | 1 | 1 | 1 | 1 | The glasses are inside the closed box with both temples visibly folded. | 76 | 50 | 50 | synced_camera_composite |
| gemini-2.5-flash | put_glass_in_glassbox | 010 | 0.0 | 0 | 1 | 1 | 0 | Both temples of the glasses are folded, the glasses are inside the box, and the box is closed. | 101 | 50 | 50 | synced_camera_composite |
| gemini-2.5-flash | utensils_to_holder | 001 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 67 | 50 | 50 | synced_camera_composite |

## Mismatches

- apple_to_fruit_bowl/001: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/000: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/001: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/010: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/001: sim_success=0, vlm_success=1, vlm_score=1.0
