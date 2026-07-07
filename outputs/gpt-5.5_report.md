# GPT Rollout Score Report

- num_rollouts: 10
- scored_rollouts: 10
- failed_rollouts: 0
- agreement_rate: 0.900

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| gpt-5.5 | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 51 | 50 | 50 | synced_camera_composite |
| gpt-5.5 | apple_to_fruit_bowl | 002 | 1.0 | 1 | 0 | 0 | 0 | The apple is still held by the gripper above the bowl rather than visibly placed inside it. | 11 | 11 | 50 | synced_camera_composite |
| gpt-5.5 | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains beside the open book on the table rather than visibly overlapping the book. | 51 | 50 | 50 | synced_camera_composite |
| gpt-5.5 | bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 11 | 11 | 50 | synced_camera_composite |
| gpt-5.5 | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | The lid remains off the jar and the visible coffee beans are still on the tabletop rather than inside the jar. | 117 | 50 | 50 | synced_camera_composite |
| gpt-5.5 | collect_coffee_beans | 001 | 0.5 | 0 | 0.5 | 0 | 1 | All seven beans appear collected inside the open jar, but the lid remains on the tabletop beside it. | 117 | 50 | 50 | synced_camera_composite |
| gpt-5.5 | detergent | 001 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 74 | 50 | 50 | synced_camera_composite |
| gpt-5.5 | put_glass_in_glassbox | 002 | 1.0 | 1 | 1 | 1 | 1 | The glasses were visibly placed inside the box with both temples folded, and the box is closed at the end. | 76 | 50 | 50 | synced_camera_composite |
| gpt-5.5 | put_glass_in_glassbox | 010 | 0.0 | 0 | 0.333333 | 0 | 1 | The box is visibly closed, but the glasses are outside it and both temples are not visibly folded. | 101 | 50 | 50 | synced_camera_composite |
| gpt-5.5 | utensils_to_holder | 001 | 0.5 | 0 | 0.5 | 0 | 1 | Exactly one half-credit condition is visibly satisfied. | 67 | 50 | 50 | synced_camera_composite |

## Mismatches

- apple_to_fruit_bowl/002: sim_success=1, vlm_success=0, vlm_score=0.0
