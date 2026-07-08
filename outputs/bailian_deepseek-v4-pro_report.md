# GPT Rollout Score Report

- num_rollouts: 360
- scored_rollouts: 360
- failed_rollouts: 0
- agreement_rate: 0.683

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 000 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 001 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 003 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 004 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 005 | 0.0 | 0 | 0 | 0 | 1 | No visible evidence of the apple inside the fruit bowl is provided in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 006 | 1.0 | 1 | 0 | 0 | 0 | No frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 007 | 1.0 | 1 | 0 | 0 | 0 | No visual evidence is provided; the required final state cannot be confirmed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 008 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 009 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 010 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 011 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 013 | 1.0 | 1 | 0 | 0 | 0 | No visible evidence of the apple inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 014 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 015 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 016 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 017 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 018 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 000 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 003 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book with sufficient overlap. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 004 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly on the book with at least 40% overlap. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 005 | 0.0 | 0 | 0 | 0 | 1 | No images provided; cannot visually verify the final state of the bookmark and book. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 007 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 008 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 009 | 0.0 | 0 | 0 | 0 | 1 | No image frames are visible in the provided input to evaluate the bookmark placement. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 011 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 013 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 015 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | No frames provided; unable to evaluate bookmark placement. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 017 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence available. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 019 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | No frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 001 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided in the input; cannot evaluate the final state. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided in the input; cannot evaluate visible evidence. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 003 | 0.0 | 0 | 0 | 0 | 1 | No visible frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 004 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence of lid on jar or beans inside jar is present in the provided frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 005 | 0.0 | 0 | 1 | 1 | 0 | Lid is placed on the jar and all 7 coffee beans are visible inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided; unable to evaluate the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 007 | 0.0 | 0 | 1 | 1 | 0 | The lid is placed on the jar and all 7 coffee beans are inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 008 | 0.0 | 0 | 0 | 0 | 1 | Frames not provided; cannot assess visual evidence. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence available; cannot confirm lid placement or coffee beans inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 010 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence available; the frames were not provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 011 | 0.0 | 0 | 0 | 0 | 1 | No frames provided to evaluate the task. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 012 | 0.28571 | 0 | 0.5 | 0 | 1 | The lid is placed on the jar, but all coffee beans are on top of the lid instead of inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | No video frames were provided to the assistant, so no evidence of lid placement or beans inside the jar is visible. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 015 | 0.0 | 0 | 0 | 0 | 1 | No frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 016 | 0.0 | 0 | 0 | 0 | 1 | No frames are visible to evaluate; therefore no lid or beans can be counted. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 017 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence provided; cannot evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 018 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence available to evaluate the task. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | No frames provided; unable to evaluate lid or beans. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 000 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 001 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 002 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 003 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 004 | 0.0 | 0 | 1 | 1 | 0 | All three detergent items are visibly placed in the basket. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 005 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 006 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 007 | 0.0 | 0 | 0 | 0 | 1 | No images provided; unable to observe any detergent item completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 008 | 0.0 | 0 | 1 | 1 | 0 | All three detergent bottles are visibly placed in the target container. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 009 | 0.0 | 0 | 0 | 0 | 1 | No frames are provided to evaluate the task. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 010 | 0.0 | 0 | 0 | 0 | 1 | No frames provided to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 011 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 013 | 0.0 | 0 | 0.666667 | 0 | 1 | Two weighted sub-conditions are visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 014 | 0.0 | 0 | 0 | 0 | 1 | No frames provided to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 015 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 016 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 017 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 018 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 019 | 0.0 | 0 | 0.666667 | 0 | 1 | Two weighted sub-conditions are visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 000 | 0.0 | 0 | 0 | 0 | 1 | No image frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 001 | 0.33333 | 0 | 1 | 1 | 0 | The glasses are inside the box, both temples are folded, and the box is closed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation; cannot determine visible evidence. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 003 | 0.0 | 0 | 0 | 0 | 1 | No visual frames were provided; unable to evaluate any of the three conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided; unable to evaluate any condition. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 005 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 006 | 0.0 | 0 | 0.666667 | 0 | 1 | The glasses were placed inside the box and the box was closed, but the temples were not folded (they remained extended throughout). | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 007 | 0.0 | 0 | 0 | 0 | 1 | No frames provided to evaluate; unable to assess task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 008 | 0.0 | 0 | 0 | 0 | 1 | No frames provided to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 009 | 0.0 | 0 | 0 | 0 | 1 | No image frames provided to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0 | 0 | 1 | No video frames provided to evaluate the task conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0 | 0 | 1 | No frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 012 | 0.33333 | 0 | 0 | 0 | 1 | Frames not provided. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 013 | 0.0 | 0 | 0 | 0 | 1 | No visible frames provided; unable to evaluate task conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 014 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence of any condition being satisfied from the provided frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 015 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 016 | 0.0 | 0 | 0 | 0 | 1 | No visual frames provided; cannot assess task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 017 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence of any condition being satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 018 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 019 | 0.0 | 0 | 0 | 0 | 1 | No frames provided; unable to evaluate any conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 000 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 001 | 0.0 | 0 | 0.5 | 0 | 1 | Exactly one half-credit condition is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 003 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 005 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 006 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 007 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 008 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence is provided to determine the final state of the utensils. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 010 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 011 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 013 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | No visible evidence provided. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 015 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 016 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 017 | 0.0 | 0 | 0.5 | 0 | 1 | Exactly one half-credit condition is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 018 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | No frames provided; cannot determine if utensils are on holder. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple is still held by the robot gripper and not released inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 004 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 005 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 006 | 1.0 | 1 | 0 | 0 | 0 | No frames are visible to evaluate; the required final state cannot be confirmed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 007 | 1.0 | 1 | 0 | 0 | 0 | The apple is not visibly inside the fruit bowl in the provided frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 009 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 010 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 011 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 013 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied because no image frames are available for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 014 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 015 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 016 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied because no visual frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 019 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied because no frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 002 | 1.0 | 1 | 0 | 0 | 0 | No frames were provided to evaluate the bookmark placement. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 003 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 005 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 007 | 1.0 | 1 | 0 | 0 | 0 | No images provided; cannot verify if the bookmark is placed on the book with sufficient overlap. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | No frames provided; unable to assess visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 009 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 010 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 011 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 013 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 015 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is placed on the book with full visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 016 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 017 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 018 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 019 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied because no image data was provided. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 000 | 0.14286 | 0 | 1 | 1 | 0 | The lid is placed on the jar and all 7 coffee beans are visible inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | Final frame shows lid not on jar and no coffee beans inside jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | No frames provided to evaluate; no visible evidence of lid placement or beans inside jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 003 | 0.42857 | 0 | 0 | 0 | 1 | Frames are not provided; no visible evidence of lid on jar or beans inside. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 004 | 0.5 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 005 | 0.35714 | 0 | 0 | 0 | 1 | No frames provided; cannot evaluate the placement of the lid or the number of beans inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 008 | 0.5 | 0 | 0 | 0 | 1 | No visual evidence provided in the frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 009 | 0.42857 | 0 | 0 | 0 | 1 | No visual evidence provided; cannot see frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 010 | 0.14286 | 0 | 0 | 0 | 1 | No visual frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 011 | 0.21429 | 0 | 1 | 1 | 0 | The lid is correctly placed on the jar and all 7 coffee beans are clearly visible inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 012 | 0.0 | 0 | 0 | 0 | 1 | No frames provided to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 013 | 0.5 | 0 | 0 | 0 | 1 | No frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | No visible evidence of the lid placed on the jar or coffee beans inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 015 | 0.07143 | 0 | 0 | 0 | 1 | No visual frames were provided; unable to evaluate lid or coffee beans. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 016 | 0.0 | 0 | 1 | 1 | 0 | The lid is on the jar and all 7 coffee beans are inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 017 | 0.14286 | 0 | 0 | 0 | 1 | No frames were provided, so no evidence of lid placement or coffee beans inside the jar is visible. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 018 | 0.0 | 0 | 0 | 0 | 1 | No frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 019 | 0.5 | 0 | 0 | 0 | 1 | No image frames available for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 000 | 1.0 | 1 | 0 | 0 | 0 | No visible evidence of detergent items being completed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 001 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 002 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 003 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 004 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 005 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 006 | 1.0 | 1 | 0 | 0 | 0 | Unable to evaluate: no visual frames provided. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 007 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 008 | 1.0 | 1 | 0 | 0 | 0 | No detergent items are visibly completed in the provided frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 009 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed into the bin. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 010 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 011 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 012 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 013 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 014 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed in the required final state. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 015 | 1.0 | 1 | 0 | 0 | 0 | No visible evidence of completed detergent items. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 016 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 017 | 1.0 | 1 | 0 | 0 | 0 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 018 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 019 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed in the sink. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 000 | 0.33333 | 0 | 0 | 0 | 1 | No images were provided in the conversation; unable to evaluate the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 001 | 0.66667 | 0 | 0 | 0 | 1 | No image frames provided; unable to assess task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 002 | 1.0 | 1 | 0 | 0 | 0 | No visual evidence available to evaluate the frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 003 | 1.0 | 1 | 1 | 1 | 1 | Both temples are visibly folded, the glasses are inside the box, and the box lid is closed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | No frames provided, cannot evaluate the task. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 005 | 0.33333 | 0 | 0 | 0 | 1 | No visual evidence provided; frames are missing. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 006 | 0.66667 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 007 | 0.0 | 0 | 1 | 1 | 0 | Both temples are folded, the glasses are placed inside the box, and the box lid is closed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 008 | 0.0 | 0 | 0 | 0 | 1 | No visual frames provided; cannot evaluate task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 009 | 0.0 | 0 | 0 | 0 | 1 | No frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 010 | 0.0 | 0 | 0 | 0 | 1 | The input frames are not provided; visual evidence is missing. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 011 | 1.0 | 1 | 0 | 0 | 0 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 012 | 1.0 | 1 | 0 | 0 | 0 | No images were provided for evaluation, so no conditions could be confirmed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 013 | 1.0 | 1 | 0 | 0 | 0 | No image frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0 | 0 | 1 | No visual frames were provided to evaluate the task conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 015 | 0.0 | 0 | 0 | 0 | 1 | No frames provided; cannot evaluate task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 016 | 1.0 | 1 | 1 | 1 | 1 | The glasses are inside the box, both temples are folded, and the box is closed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 017 | 0.0 | 0 | 0 | 0 | 1 | No visible frames provided; cannot assess task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 018 | 1.0 | 1 | 0 | 0 | 0 | No frames were provided for evaluation; cannot determine if any conditions are satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 019 | 0.0 | 0 | 0 | 0 | 1 | No visible evidence of glasses inside box, temples folded, or box closed in any frame. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 000 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 001 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 002 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 003 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 005 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 006 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 007 | 0.5 | 0 | 0 | 0 | 1 | No visual evidence provided; cannot assess the final state. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 008 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 010 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 011 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 012 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 013 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 014 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 015 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 016 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 017 | 0.5 | 0 | 0.5 | 0 | 1 | Exactly one half-credit condition is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 018 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 004 | 1.0 | 1 | 0 | 0 | 0 | No frames provided; cannot assess if apple is in fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 005 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 006 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied because no image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 007 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 009 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 010 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 011 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 013 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 014 | 1.0 | 1 | 0 | 0 | 0 | The apple is not visible inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 015 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 016 | 0.0 | 0 | 0 | 0 | 1 | No visual frames were provided in the input; cannot determine if the apple is in the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 017 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 018 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 000 | 1.0 | 1 | 0 | 0 | 0 | No visual evidence of the final state is provided; the input frames are not visible to the evaluator. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 001 | 1.0 | 1 | 0 | 0 | 0 | No visible frames provided to evaluate the final state. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 003 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 004 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied because no frames are visible to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 005 | 1.0 | 1 | 0 | 0 | 0 | No images were provided to assess the final state. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 007 | 1.0 | 1 | 0 | 0 | 0 | No visible evidence provided; the image frames are not accessible to the evaluator. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 008 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is placed on the book with visible overlap exceeding 40%. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 009 | 1.0 | 1 | 0 | 0 | 0 | No visible evidence provided; cannot determine if bookmark is on book. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 011 | 1.0 | 1 | 0 | 0 | 0 | The provided frames do not contain visible evidence of the bookmark on the book. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation; the required final state cannot be verified. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 013 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 014 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is placed entirely on the book with clear full overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 015 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 016 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 017 | 1.0 | 1 | 0 | 0 | 0 | No frames provided to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | No frames were provided, so the required final state cannot be verified. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | bookmark_on_book | 019 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | No visible evidence from frames; images not accessible. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | No visual evidence available; frames not provided. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 002 | 0.07143 | 0 | 0 | 0 | 1 | Cannot evaluate; no image data provided. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 003 | 0.42857 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visible inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 004 | 0.5 | 0 | 0 | 0 | 1 | No visual evidence available: frames not provided. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 005 | 0.0 | 0 | 0 | 0 | 1 | No video frames were provided; cannot assess lid or coffee beans. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | No visual frames provided; unable to assess lid or bean positions from the given text placeholders. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | No image frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 008 | 0.42857 | 0 | 0 | 0 | 1 | No visible evidence of lid placement or beans inside the jar in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | No visible frames were supplied to evaluate the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 010 | 0.0 | 0 | 1 | 1 | 0 | The lid is visibly placed on the jar and all 7 coffee beans are inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 011 | 0.35714 | 0 | 0 | 0 | 1 | No images were provided to evaluate the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 012 | 0.0 | 0 | 0 | 0 | 1 | No visual frames were provided; unable to confirm lid placement or coffee beans inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | No visible evidence of lid on jar or beans inside jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | No visual frames provided; cannot evaluate lid placement or bean count. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 015 | 0.42857 | 0 | 0 | 0 | 1 | No visual evidence of lid on jar or coffee beans inside jar is visible in the provided frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 016 | 1.0 | 1 | 0 | 0 | 0 | No visible evidence of lid on jar or beans inside jar. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 017 | 1.0 | 1 | 0 | 0 | 0 | No frames provided to evaluate the rollout. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 018 | 1.0 | 1 | 0 | 0 | 0 | Images not provided; cannot evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | Cannot see the provided frames; no visual evidence to evaluate lid or beans. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 000 | 0.66667 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 001 | 0.33333 | 0 | 0 | 0 | 1 | No frames provided to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 002 | 0.66667 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 003 | 0.66667 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 004 | 0.33333 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 005 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 006 | 0.66667 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 007 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 008 | 0.33333 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 009 | 0.66667 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 010 | 0.66667 | 0 | 1 | 1 | 0 | All three detergent bottles are visibly placed in the bin. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 011 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 012 | 0.66667 | 0 | 0 | 0 | 1 | Frames not provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 013 | 0.33333 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 014 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 015 | 0.0 | 0 | 0 | 0 | 1 | No images provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 016 | 0.66667 | 0 | 0 | 0 | 1 | No visual frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 017 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 018 | 0.66667 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | detergent | 019 | 0.66667 | 0 | 0 | 0 | 1 | No visible evidence of completed detergent items. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 000 | 0.33333 | 0 | 0 | 0 | 1 | No frames were provided to evaluate the task. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 001 | 0.33333 | 0 | 0 | 0 | 1 | No frames provided; unable to verify any condition. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0 | 0 | 1 | No visual frames provided; cannot assess task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 003 | 0.33333 | 0 | 0 | 0 | 1 | No visible frames provided to evaluate the conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | No visual evidence available in the provided frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 005 | 0.0 | 0 | 0 | 0 | 1 | No images provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 006 | 0.33333 | 0 | 0 | 0 | 1 | No frames provided, cannot evaluate visible evidence. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 007 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses are inside the box but both temples remain unfolded and stick out from under the lid, preventing the box from being fully closed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 008 | 0.33333 | 0 | 0 | 0 | 1 | Frames are not visible; cannot assess completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 009 | 0.33333 | 0 | 0 | 0 | 1 | No visual evidence provided; unable to verify any conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0 | 0 | 1 | No visual evidence available in the provided frames. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0 | 0 | 1 | No image frames were provided to evaluate the task. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 012 | 1.0 | 1 | 0 | 0 | 0 | No video frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 013 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses are inside the box with both temples folded, but the box lid is open, not closed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0 | 0 | 1 | No image frames provided for evaluation; unable to assess task completion. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 015 | 0.33333 | 0 | 1 | 1 | 0 | Both temples are folded, the glasses are inside the box, and the box is fully closed. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 016 | 0.66667 | 0 | 0 | 0 | 1 | No frames were provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 017 | 0.33333 | 0 | 0 | 0 | 1 | No visual frames provided for evaluation. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 018 | 0.33333 | 0 | 0 | 0 | 1 | No visible evidence of glasses inside box, temples folded, or box closed in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | put_glass_in_glassbox | 019 | 0.33333 | 0 | 0 | 0 | 1 | No visible frames provided; cannot assess any of the three conditions. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 000 | 1.0 | 1 | 0 | 0 | 0 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 001 | 0.5 | 0 | 0 | 0 | 1 | No visual evidence provided; unable to evaluate. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied because the input frames are not provided or visible to the evaluator. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 003 | 0.5 | 0 | 0 | 0 | 1 | No visible frames were provided; cannot confirm the required final state. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 004 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 005 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 006 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 007 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 010 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 011 | 0.0 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 013 | 0.5 | 0 | 0 | 0 | 1 | No visible evidence of the required final state. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 016 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 017 | 0.5 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 018 | 0.5 | 0 | 1 | 1 | 0 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| bailian/deepseek-v4-pro | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |

## Mismatches

- apple_to_fruit_bowl/000: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/001: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/003: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/004: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/006: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/007: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/008: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/009: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/011: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/013: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/014: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/016: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/017: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/018: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/000: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/008: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/011: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/015: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/019: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/005: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/007: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/001: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/002: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/003: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/004: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/008: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/001: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/000: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/008: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/013: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/015: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/006: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/007: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/009: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/010: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/014: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/019: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/002: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/007: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/010: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/011: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/013: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/015: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/016: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/018: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/019: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/000: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/011: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/016: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/000: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/001: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/003: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/004: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/005: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/006: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/007: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/008: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/010: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/011: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/013: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/015: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/016: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/017: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/002: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/007: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/011: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/012: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/013: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/018: sim_success=1, vlm_success=0, vlm_score=0.0
- utensils_to_holder/001: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/002: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/003: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/005: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/008: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/011: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/012: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/013: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/015: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/004: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/005: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/006: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/011: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/014: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/015: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/017: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/018: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/000: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/001: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/003: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/005: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/007: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/008: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/009: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/011: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/014: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/015: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/016: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/017: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/010: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/016: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/017: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/018: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/005: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/006: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/007: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/010: sim_success=0, vlm_success=1, vlm_score=1.0
- detergent/014: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/017: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/012: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/015: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/000: sim_success=1, vlm_success=0, vlm_score=0.0
- utensils_to_holder/010: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/011: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/018: sim_success=0, vlm_success=1, vlm_score=1.0
