# GPT Rollout Score Report

- num_rollouts: 360
- scored_rollouts: 360
- failed_rollouts: 0
- agreement_rate: 0.886

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| kimi-k2.6 | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is never placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 001 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | The apple is visibly resting on the table next to the bowl, not inside it, in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in all final camera views; the apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 004 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the white fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 005 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in the final frames and the apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 007 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout, the apple remains on the table next to the empty fruit bowl and was never placed inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 009 | 0.0 | 0 | 1 | 1 | 0 | The red apple is clearly visible resting inside the fruit bowl in the final camera views. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 010 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly resting inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 011 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frames from all camera angles. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and is never placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 013 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 015 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 016 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the white fruit bowl in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple is not visibly inside the fruit bowl at the end of the rollout; the bowl remains empty in all camera views. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and is never placed inside the empty fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in all final camera views and the apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 000 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly resting on the lower-left corner of the book with sufficient overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains in the robot gripper and is never visibly placed on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on the book with at least 40% overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 003 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible on the table next to the ruler and not on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 004 | 0.0 | 0 | 1 | 1 | 0 | The light blue bookmark is visibly resting flat on the open book's page with full overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 005 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly resting on the open book's page in the final frame with full overlap. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visibly placed on the table away from the book, not on top of it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 007 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible on the table next to the book, not on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table and is not placed on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 009 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly resting on the open book with well over 40% of its length overlapping the pages. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains in the robot gripper or on the table and is not placed on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 011 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table and is not visibly placed on the book in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark ends up on the left side of the desk, completely separate from the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 013 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visibly lying on the table, not on the book, in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on the book; the final frames show the open book without any bookmark overlapping its pages. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table and is not visibly placed on the book with any overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 017 | 0.0 | 0 | 0 | 0 | 1 | The robot is still holding the bookmark in its gripper and has not placed it on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on the book with at least 40% overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 019 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in any camera view at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 001 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 003 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 004 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 005 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar; all beans remain on the table and the jar is missing from view by the end. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The lid is visibly on the table and not on the jar, and no coffee beans are visibly inside the jar with all beans remaining scattered on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 008 | 0.0 | 0 | 0 | 0 | 1 | The lid is held by the gripper and not placed on the jar, and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 010 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 011 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout, the jar is not visible, the lid is not on the jar, and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 012 | 0.28571 | 0 | 1 | 1 | 0 | The lid is properly placed on the jar and all 7 coffee beans are inside with none visible outside. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | The lid remains off the jar on the table and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid is visibly on the table and all coffee beans remain scattered outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 015 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 016 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 017 | 0.0 | 0 | 0 | 0 | 1 | The lid is not placed on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 018 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | The lid is not placed on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 000 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed in the basket by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 001 | 0.0 | 0 | 0 | 0 | 1 | No detergent items were placed in the wooden box; all three remain visibly scattered on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 002 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed in the basket; all three remain on the counter or in the gripper. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 003 | 0.0 | 0 | 0 | 0 | 1 | All three detergent items remain scattered outside the wooden box and are not visibly placed in their required receptacle at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 004 | 0.0 | 0 | 0 | 0 | 1 | The basket is visibly empty at the end of the rollout and the robot is still grasping the blue spray bottle, with no detergent items successfully placed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 005 | 0.0 | 0 | 0 | 0 | 1 | None of the three detergent items were placed in the basket; all remain scattered on the counter at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 006 | 0.0 | 0 | 0 | 0 | 1 | None of the three detergent items were visibly placed in the basket or handed over by the end of the rollout; one remains on the counter and two are still in the robot's grippers. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 007 | 0.0 | 0 | 0.333333 | 0 | 1 | Only one of the three detergent bottles was visibly placed into the sink, while the other two remain on the counter outside the target. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 008 | 0.0 | 0 | 0.333333 | 0 | 1 | Only the Cif bottle is visibly placed inside the wooden basket; the green and blue spray bottles remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 009 | 0.0 | 0 | 0 | 0 | 1 | None of the three detergent items are visibly placed in the basket or handed over by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 010 | 0.0 | 0 | 0 | 0 | 1 | All three detergent bottles remain visibly scattered on the counter and none are placed inside the wooden basket at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 011 | 0.0 | 0 | 0 | 0 | 1 | The wooden basket remains visibly empty at the end of the rollout and none of the three detergent bottles were successfully placed inside. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 012 | 0.0 | 0 | 0 | 0 | 1 | The wooden basket remains visibly empty and no detergent items are seen in a completed placed state. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 013 | 0.0 | 0 | 0 | 0 | 1 | None of the three detergent items were placed in the wooden box; all remain scattered on the counter or floor. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 014 | 0.0 | 0 | 0 | 0 | 1 | None of the 3 detergent items were placed in the basket or handed over; they remain scattered on the counter and floor. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 015 | 0.0 | 0 | 0 | 0 | 1 | None of the three detergent items were placed in the target basket, leaving them scattered on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 016 | 0.0 | 0 | 0 | 0 | 1 | None of the three detergent items were placed in the basket or handed over; they remain on the counter or floor. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 017 | 0.0 | 0 | 0 | 0 | 1 | All three detergent items remain visibly on the counter outside the basket and were not placed or handed over by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 018 | 0.0 | 0 | 0 | 0 | 1 | All three detergent items remain scattered on the counter and none are visibly placed inside the basket or handed over. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 019 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed in the basket or handed over by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 000 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with unfolded temples at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 001 | 0.33333 | 0 | 0 | 0 | 1 | No frame clearly shows the glasses inside the box, both temples folded, or the box fully closed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0.666667 | 0 | 1 | Glasses are inside the box with both temples folded, but the box is not fully closed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 003 | 0.0 | 0 | 0 | 0 | 1 | The glasses are not inside the box, both temples are unfolded, and the box remains open. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with both temples visibly unfolded throughout the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 005 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with both temples visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 006 | 0.0 | 0 | 0 | 0 | 1 | The glasses are visibly outside the open box with both temples unfolded at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 007 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with unfolded temples throughout the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 008 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open case with both temples visibly unfolded at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 009 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open glasses box with both temples unfolded in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses temples are visibly folded, but the glasses remain outside the open box. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box ends up closed, but the glasses remain outside the box on the table and both temples are visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 012 | 0.33333 | 0 | 0.333333 | 0 | 1 | Glasses are placed inside the glasses box but the temples remain visibly unfolded and the box is not closed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 013 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table outside the open box with both temples visibly unfolded in all frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 014 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses box is closed but the glasses are not visibly inside and the temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 015 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses are placed inside the box but the temples remain visibly unfolded and the box is not closed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 016 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with both temples visibly extended, and the box is never fully closed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 017 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with unfolded temples at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 018 | 0.0 | 0 | 0 | 0 | 1 | The glasses were never placed inside the box, the temples remained unfolded, and the box stayed open throughout the entire rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 019 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table outside the open box with both temples unfolded throughout the entire rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 000 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain visible on the table and are not placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 001 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain on the counter and are not placed on the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 002 | 0.0 | 0 | 0.5 | 0 | 1 | The fork is placed in the utensil holder but the spoon is dropped into the sink and not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 003 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout, neither the spoon nor the fork is visible on the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the utensil holder in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 005 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout both the spoon and the fork remain on the table, not in or on the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 006 | 0.0 | 0 | 0.5 | 0 | 1 | Only the spoon is resting in the utensil holder; the fork remains on the table and was not placed in the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 007 | 0.5 | 0 | 1 | 1 | 0 | Both the spoon and fork are visibly placed in the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork are visible in the sink at the end of the rollout, not placed on the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder in the visible frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 010 | 0.0 | 0 | 1 | 1 | 0 | Both the spoon and fork are visibly resting in the utensil holder compartments in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 011 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork remains on the counter and is not placed in the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed in the utensil holder; both remain on the table throughout the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 013 | 0.5 | 0 | 0.5 | 0 | 1 | Only the fork is placed on the holder; the spoon is not on the holder in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visible inside the utensil holder in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 015 | 0.0 | 0 | 1 | 1 | 0 | Both the fork and the spoon are clearly visible inside the utensil holder compartments in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 016 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the counter and are not placed on the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 017 | 0.0 | 0 | 0.5 | 0 | 1 | The fork was placed in the holder but the spoon remained on the counter and was not placed in the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 018 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain untouched on the counter throughout the rollout and are never placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is resting on the holder in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table edge and was never placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout, the apple is visibly on the table and not inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the white fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in the final frames and the red apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 004 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table edge and is never placed inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 005 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 007 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The apple is visible on the table next to the bowl, not inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 009 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 010 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the fruit bowl in the final frames across all camera views. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 011 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 012 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly inside the fruit bowl in the final frames from all camera angles. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 013 | 0.0 | 0 | 0 | 0 | 1 | The apple is visible on the table beside the fruit bowl, never having been placed inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 015 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the right edge throughout the rollout and is never placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 016 | 0.0 | 0 | 0 | 0 | 1 | The apple is visible on the table outside the bowl in the final frames, while the bowl interior is empty. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple remains visible on the table at the end of the rollout and is never placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple is visibly on the table and not inside the empty fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in all final camera views with no apple inside. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table next to the open book and is never placed on top of it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table beside the open book and is never placed on top of the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 002 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book with substantial overlap covering the page. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 003 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book with substantial overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | In the final frame, the light-blue bookmark is clearly resting on the left page of the open book with well over 40% visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 005 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly resting on the open book with clear overlap exceeding 40% in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible on the table next to the open book and is not placed on the book with any visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 007 | 1.0 | 1 | 1 | 1 | 1 | The dark bookmark is visibly resting on the open book pages with substantial overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is resting on the table next to the book and is not placed on top of the book with any visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 009 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly resting on the open book pages with well over 40% overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visibly lying on the table beside the book rather than placed on top of the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 011 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book with substantial overlap exceeding 40%. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is placed on the table away from the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 013 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly resting on the open book's page with substantial overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains in the robot's gripper and is not placed on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table next to the book and is not placed on top of it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains grasped by the robot gripper and is not released onto the book in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 017 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book with clearly more than 40% overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible on the table and not placed on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 019 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book's page with well over 40% overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | The lid remains on the table and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | The lid is visibly next to the jar rather than on it, and no coffee beans are clearly visible inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain visibly scattered on the table outside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 003 | 0.42857 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 004 | 0.5 | 0 | 0.5 | 0 | 1 | The lid is on the jar but no coffee beans are visibly inside the opaque lidded jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 005 | 0.35714 | 0 | 0.357143 | 0 | 1 | The lid is not on the jar and only 5 coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout the jar is no longer visible in any camera, the lid remains on the table, and no beans can be verified inside. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The lid is visibly on the table and all coffee beans remain on the table, not inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 008 | 0.5 | 0 | 0 | 0 | 1 | The lid is off the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 009 | 0.42857 | 0 | 0.5 | 0 | 1 | The lid is not on the jar at the end of the rollout, though all 7 coffee beans are visible inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 010 | 0.14286 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 011 | 0.21429 | 0 | 0.285714 | 0 | 1 | The lid is not on the jar and only 4 of 7 coffee beans are visibly inside the jar with 3 remaining on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 012 | 0.0 | 0 | 0.5 | 0 | 1 | The lid is visibly placed on the jar but all seven coffee beans remain on the table and none are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 013 | 0.5 | 0 | 1 | 1 | 0 | The lid is on the jar and all 7 coffee beans are visibly collected inside the jar before the lid is placed, with no beans remaining on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid is off the jar on the lower shelf and all seven coffee beans are visibly scattered on the tabletop, not inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 015 | 0.07143 | 0 | 0.142857 | 0 | 1 | The lid remains on the table and is not placed on the jar, and only 2 of the 7 coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 016 | 0.0 | 0 | 0 | 0 | 1 | The lid is left on the table and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 017 | 0.14286 | 0 | 0.214286 | 0 | 1 | The lid is visibly on the table rather than on the jar, and only three coffee beans are clearly visible inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 018 | 0.0 | 0 | 0.0714286 | 0 | 1 | The lid is left on the table rather than on the jar, and only one coffee bean is visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 019 | 0.5 | 0 | 0.5 | 0 | 1 | The lid is off the jar on the table while all 7 coffee beans are inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 000 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden box. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 001 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden box by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 002 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout with none remaining on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 003 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 004 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 005 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed in the basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 006 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed in the basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 007 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 008 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 009 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 010 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 011 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items were visibly placed into the wooden box. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 012 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 013 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden box by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 014 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden storage box by the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 015 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 016 | 1.0 | 1 | 1 | 1 | 1 | All three detergent spray bottles are visibly placed inside the wooden basket in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 017 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 018 | 1.0 | 1 | 1 | 1 | 1 | All three detergent spray bottles are visibly placed inside the basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 019 | 1.0 | 1 | 1 | 1 | 1 | All three detergent spray bottles are visibly placed inside the wooden basket with no bottles remaining on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 000 | 0.33333 | 0 | 1 | 1 | 0 | The glasses are visibly placed inside the box with both temples folded, and the box is fully closed in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 001 | 0.66667 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside the box with temples extended. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 002 | 1.0 | 1 | 1 | 1 | 1 | The glasses are completely inside the closed box with both temples visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 003 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses are inside the closed box, but both temples were not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 004 | 0.0 | 0 | 1 | 1 | 0 | Both temples are visibly folded during manipulation, the glasses are completely inside the box, and the box is fully closed in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 005 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is fully closed, but the glasses remain outside the box with both temples visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 006 | 0.66667 | 0 | 0.333333 | 0 | 1 | The glasses box is closed but the glasses are not completely inside and their temples remain visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 007 | 0.0 | 0 | 0.666667 | 0 | 1 | The glasses are inside the closed box, but the temples were never visibly folded before or during placement. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 008 | 0.0 | 0 | 0 | 0 | 1 | The final frames show the glasses box open with the glasses partially inside and at least one temple visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 009 | 0.0 | 0 | 1 | 1 | 0 | The glasses are visibly inside the closed box and both temples were clearly folded in the frames immediately before the box was shut. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 010 | 0.0 | 0 | 0.666667 | 0 | 1 | Both temples are folded and the box is closed, but the glasses remain outside the box on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 011 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses are completely inside the box and the box is fully closed, but both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 012 | 1.0 | 1 | 1 | 1 | 1 | Glasses are fully inside the closed box with both temples visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 013 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses are placed inside the box and the box is fully closed, but both temples are not visibly folded before or after closing. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses are visibly on the table next to the closed glasses box, not inside it, although both temples appear folded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 015 | 0.0 | 0 | 0.333333 | 0 | 1 | The box is closed but the glasses remain partially outside with both temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 016 | 1.0 | 1 | 1 | 1 | 1 | The glasses are visibly placed inside the box, both temples are folded, and the box is fully closed in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 017 | 0.0 | 0 | 0.666667 | 0 | 1 | The glasses were placed inside the box and the box was fully closed, but both temples remained visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 018 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses were placed inside the box and the box was fully closed, but both temples remained visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 019 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses box is closed but the glasses are not completely inside and one temple is visibly unfolded and sticking out. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 000 | 0.0 | 0 | 1 | 1 | 0 | Both the spoon and the fork are clearly visible inside the gray utensil holder in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 001 | 0.5 | 0 | 0.5 | 0 | 1 | Only the fork is placed on the holder; the spoon is still in the robot gripper and not on the holder at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the counter and are never placed into the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 003 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder but the fork remains on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the table or in the robot gripper, not placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 005 | 0.5 | 0 | 1 | 1 | 0 | Both the fork and the spoon are visibly resting inside the gray utensil holder in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 006 | 0.5 | 0 | 0.5 | 0 | 1 | Only the spoon is placed on the holder while the fork remains on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 007 | 0.5 | 0 | 0.5 | 0 | 1 | Only the spoon is clearly placed in the utensil holder; the fork is not visible in the holder at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain visible on the counter and are not placed in the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain visible on the table and are not placed in the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 010 | 0.5 | 0 | 1 | 1 | 0 | Both the spoon and the fork are visibly resting in the utensil holder compartments in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 011 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder but the fork remains on the table and was never placed in the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 012 | 0.5 | 0 | 0.5 | 0 | 1 | Only the spoon is placed in the utensil holder; the fork remains on the table and is not placed in the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 013 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork remains on the table in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 014 | 0.5 | 0 | 0.5 | 0 | 1 | Only the spoon is resting in the utensil holder at the end of the rollout; the fork remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | Both the wooden spoon and the fork remain on the countertop and are not placed in the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 016 | 0.5 | 0 | 0.5 | 0 | 1 | Only the fork was placed on the holder; the spoon remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 017 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the utensil holder, but the fork is not visible on the holder in any final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 018 | 0.5 | 0 | 0.5 | 0 | 1 | Only the spoon is placed on the holder; the fork is not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the counter and are not placed on the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 000 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly resting inside the blue and white fruit bowl in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple is visibly on the table and not inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table next to the empty bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is not visibly placed inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 004 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the white fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 005 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frames across multiple camera views. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the green fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 007 | 0.0 | 0 | 0 | 0 | 1 | The apple is visibly resting on the table next to the fruit bowl, not inside it, in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The apple is visibly on the table surface and not inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 009 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout, the red apple is visibly resting on the table to the right of the fruit bowl rather than inside it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 010 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frames of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 011 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 012 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly inside the fruit bowl in the final sampled frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 013 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible resting inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the fruit bowl in the final frame from all camera angles. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 015 | 0.0 | 0 | 0 | 0 | 1 | The apple is visibly on the table at the end of the rollout and not inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 016 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout, the apple is visible on the table rather than inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple is visible on the table and not inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple is visibly on the table near the bananas and not inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and is never placed inside the fruit bowl, which is visibly empty in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 000 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains on the table next to the open book and is never placed on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 001 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not on the book in the final frame; it remains on the table beside the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table and is not placed on the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 003 | 1.0 | 1 | 1 | 1 | 1 | The yellow bookmark is visibly resting on the open book with well over 40% overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 004 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is still on the table next to the book and not placed on top of it. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 005 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly resting on the open book with the majority of its area overlapping the page in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on the book in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 007 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly resting on the open book with substantial overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on the book with at least 40% overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 009 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is clearly resting on the open book with visible overlap well exceeding 40% in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 010 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly resting on the open book with sufficient overlap in the top and left camera views. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 011 | 1.0 | 1 | 1 | 1 | 1 | The pink bookmark is visibly resting on the open book's page in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visibly lying on the table next to the book, not placed on top of the book with any overlap. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 013 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book page with sufficient overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 014 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly resting on top of the closed book with at least 40% overlap in the final camera views. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible on the table beside the open book and is not placed on top of the book. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 016 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly resting on the open book with at least 40% overlap in the final table views. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 017 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book pages with substantial overlap exceeding 40% in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not on the book in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | bookmark_on_book | 019 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is clearly visible resting on the open book with sufficient overlap in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout the jar lid is visibly off the jar and all coffee beans remain scattered on the table outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 001 | 0.5 | 0 | 0.5 | 0 | 1 | The lid is visibly placed on the jar at the end, but the coffee beans are not visibly inside the jar because the lid is on and the jar is opaque. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 002 | 0.07143 | 0 | 0.5 | 0 | 1 | The lid is placed on the jar but no coffee beans were visibly collected inside the jar; all beans remain outside. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 003 | 0.42857 | 0 | 0.5 | 0 | 1 | The lid is placed on the jar but no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 004 | 0.5 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 005 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and the jar is open with no coffee beans visibly inside. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | The lid is left on the table and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The red jar is not visible in the final frame, so the lid cannot be confirmed on the jar and no coffee beans can be counted inside. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 008 | 0.42857 | 0 | 0.5 | 0 | 1 | The lid is visibly placed on the jar at the end, but no coffee beans are clearly visible inside the opaque jar because the lid covers the opening. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 010 | 0.0 | 0 | 0 | 0 | 1 | The lid is visibly off the jar on the table and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 011 | 0.35714 | 0 | 0.5 | 0 | 1 | The lid is placed on the jar but no coffee beans are visibly inside the opaque lidded jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 012 | 0.0 | 0 | 0 | 0 | 1 | The lid is on the table next to the jar rather than on it, and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | At the end of the rollout, the lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 015 | 0.42857 | 0 | 1 | 1 | 0 | The lid is visibly placed on the jar and all 7 coffee beans are inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 016 | 1.0 | 1 | 1 | 1 | 1 | The lid is visibly placed on the jar and all 7 coffee beans were seen being collected into the jar before the lid was placed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 017 | 1.0 | 1 | 0.5 | 0 | 0 | The lid is placed on the jar but no coffee beans are visibly inside the opaque jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 018 | 1.0 | 1 | 1 | 1 | 1 | The lid is properly placed on the jar and all 7 coffee beans are visibly inside the jar at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 000 | 0.66667 | 0 | 0.666667 | 0 | 1 | Only two detergent items are visibly placed inside the wooden basket in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 001 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only the green detergent bottle is visibly inside the wooden box, while the other two bottles remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 002 | 0.66667 | 0 | 0.666667 | 0 | 1 | Only two detergent bottles are visibly placed inside the basket while the third bottle remains on the counter and is not completed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 003 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are inside the wooden basket but the blue bottle remains outside on the counter at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 004 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent item was visibly placed into the wooden basket; the other two spray bottles remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 005 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 006 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed inside the wooden basket, while the third bottle remains on the counter outside the basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 007 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 008 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only the blue detergent bottle is visibly placed in the basket; the green spray bottle and green flat bottle remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 009 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed inside the wooden basket, while the third blue bottle remains on the counter and is not placed in the basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 010 | 0.66667 | 0 | 0.666667 | 0 | 1 | Only two of the three detergent bottles are visibly placed inside the wooden basket; the third purple spray bottle remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 011 | 0.0 | 0 | 0.333333 | 0 | 1 | Only one detergent item is visibly placed inside the wooden box while the other two remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 012 | 0.66667 | 0 | 1 | 1 | 0 | All three detergent items are visibly placed inside the wooden basket at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 013 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent item (the blue OxiClean bottle) was visibly placed into the wooden basket, while the other two spray bottles remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 014 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed in the wooden box. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 015 | 0.0 | 0 | 0.666667 | 0 | 1 | Only two detergent bottles are visibly inside the basket at the end; the blue bottle with the yellow cap remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 016 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed in the wooden basket, while one remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 017 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 018 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly inside the basket, but the light blue spray bottle remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | detergent | 019 | 0.66667 | 0 | 0.666667 | 0 | 1 | Only two of the three detergent items are visibly inside the basket at the end of the rollout; the purple spray bottle remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 000 | 0.33333 | 0 | 0 | 0 | 1 | At the end of the rollout the glasses lie outside the open box and at least one temple is visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 001 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses are visibly outside the box with unfolded temples, while the box itself appears closed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed but the robot is holding the glasses outside the box with temples open. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 003 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed but the glasses remain outside on the table with both temples visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table with temples open, outside the still-open and empty glasses box. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 005 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 006 | 0.33333 | 0 | 0 | 0 | 1 | The target glasses box remains open, the glasses are outside, and both temples are unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 007 | 0.33333 | 0 | 0 | 0 | 1 | The glasses are not fully inside the open box and both temples remain visibly unfolded in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 008 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses are fully inside the box with both temples folded, but the box lid remains visibly open. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 009 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is fully closed, but the glasses remain outside the box and both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with both temples unfolded in the visible frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are visibly outside the box and both temples remain unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 012 | 1.0 | 1 | 1 | 1 | 1 | Glasses are completely inside the box with both temples visibly folded and the box fully closed. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 013 | 0.33333 | 0 | 0 | 0 | 1 | The glasses are visibly on the table outside the open box with both temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses temples are visibly folded and the box is closed, but the glasses remain outside the box on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 015 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed but the glasses remain outside the box with unfolded temples. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 016 | 0.66667 | 0 | 0.666667 | 0 | 1 | The glasses are inside the box with both temples folded, but the box remains open at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 017 | 0.33333 | 0 | 0.666667 | 0 | 1 | Both temples are folded and the glasses box is closed, but the glasses remain visibly outside the box. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 018 | 0.33333 | 0 | 0.333333 | 0 | 1 | The red box is closed on the table, but the robot is holding the glasses outside with both temples visibly unfolded. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | put_glass_in_glassbox | 019 | 0.33333 | 0 | 1 | 1 | 0 | The glasses are visibly inside the closed box with both temples folded before placement and the box fully closed in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 000 | 1.0 | 1 | 1 | 1 | 1 | Both the wooden spoon and the fork are visibly placed in the utensil holder compartments. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 001 | 0.5 | 0 | 1 | 1 | 0 | Both the wooden spoon and the metal fork are visibly resting inside the utensil holder in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | The spoon is visibly left on the countertop and the fork is not seen inside the utensil holder in the final frame, so neither utensil is confirmed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 003 | 0.5 | 0 | 1 | 1 | 0 | Both the wooden spoon and the fork are visibly resting inside the utensil holder in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 004 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is resting in the gray utensil holder, but the wooden spoon is still on the counter at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 005 | 0.5 | 0 | 0.5 | 0 | 1 | Only the spoon is placed in the utensil holder; the fork remains on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 006 | 0.0 | 0 | 1 | 1 | 0 | Both the spoon and fork are visibly placed in the utensil holder compartments by the final frames. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 007 | 0.0 | 0 | 0 | 0 | 1 | The spoon is visibly held by the robot gripper and the fork is on the table in the final frames, so neither utensil is on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork are visible on the table in the final frames, not placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork are visibly resting on the utensil holder in any frame; the spoon is repeatedly placed back on the table and the fork is never transferred to the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 010 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is placed in the utensil holder, but the fork remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 011 | 0.0 | 0 | 0.5 | 0 | 1 | The fork is placed in the utensil holder but the spoon ends up on the plate instead of the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain on the table and are not placed in the utensil holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 013 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed on the utensil holder but the fork remains on the table. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the table and were not placed onto the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 015 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is placed in the utensil holder but the fork remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 016 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the utensil holder but the fork is left on the plate instead of being placed in the holder. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 017 | 0.5 | 0 | 1 | 1 | 0 | Both the wooden spoon and the metal fork are visibly resting in the utensil holder in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 018 | 0.5 | 0 | 1 | 1 | 0 | Both the spoon and fork are visibly placed in the utensil holder by the final frame. | 50 | 50 | 50 | synced_camera_composite |
| kimi-k2.6 | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | The spoon is resting on the plate instead of the holder, and the fork is not placed in the holder. | 50 | 50 | 50 | synced_camera_composite |

## Mismatches

- apple_to_fruit_bowl/009: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/010: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/000: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/004: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/005: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/009: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/012: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/007: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/010: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/015: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/005: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/011: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/012: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/013: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/000: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/003: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/004: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/009: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/011: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/013: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/018: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- utensils_to_holder/000: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/005: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/010: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/000: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/012: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/000: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/001: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/010: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/014: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/016: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/019: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/015: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/017: sim_success=1, vlm_success=0, vlm_score=0.5
- detergent/012: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/019: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/001: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/003: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/006: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/017: sim_success=0, vlm_success=1, vlm_score=1.0
- utensils_to_holder/018: sim_success=0, vlm_success=1, vlm_score=1.0
