# GPT Rollout Score Report

- num_rollouts: 360
- scored_rollouts: 360
- failed_rollouts: 0
- agreement_rate: 0.942

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| qwen3.6-plus | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is never placed inside the blue fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 001 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table next to the bowl and is never placed inside it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in the final frames, indicating the apple was not successfully placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 004 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible resting inside the white fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 005 | 0.0 | 0 | 0 | 0 | 1 | The apple was grasped but dropped or moved away, and the fruit bowl remains empty at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The green apple is visibly placed inside the green fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 007 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The apple is held by the robot arm near the edge of the table and is not placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 009 | 0.0 | 0 | 1 | 1 | 0 | The apple is clearly visible inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 010 | 0.0 | 0 | 1 | 1 | 0 | The apple is visibly placed inside the fruit bowl in the final frames, as seen in the top and right camera views. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 011 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface near the edge and is never placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 013 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible inside the fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 015 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the blue patterned fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 016 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the white fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the right side of the table near the bananas and is not placed inside the white bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple is resting on the table surface and the bowl is empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and the fruit bowl is empty at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible on the table next to the book, not placed on top of it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The robot fails to place the bookmark on the book, and the simulation ends with the camera view falling away before the task is completed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on the book with sufficient overlap in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 003 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book; the book remains open and empty throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 004 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on top of the book in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 005 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book; the open book pages are visibly empty in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark was placed on the table surface away from the book rather than on top of it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 007 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is visibly placed on the open book with significant overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The robot picks up the bookmark but the simulation crashes or falls away before the bookmark is placed on the book. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 009 | 0.0 | 0 | 0 | 0 | 1 | The robot placed a black object on the book instead of the wooden bookmark with the blue tassel. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The robot holds the bookmark throughout the sequence and the simulation crashes before the bookmark is placed on the book. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 011 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the left side of the table and is never placed on the book. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The robot fails to place the bookmark on the book, and the simulation ends with the robot launching into the air. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 013 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frames, as the book pages are empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 014 | 0.0 | 0 | 1 | 1 | 0 | The bookmark is clearly placed on the open book with significant overlap visible in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table next to the book throughout the video and is never placed on top of it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The open book is visible on the desk, but no bookmark is placed on top of it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 017 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is manipulated near the desk edge but is never placed on the open book before the simulation glitches. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 019 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | The lid is on the table and the coffee beans remain scattered on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 001 | 0.0 | 0 | 0 | 0 | 1 | The lid was never placed on the jar and no coffee beans were collected into the jar, as both remained on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | The lid is resting on the table and the coffee beans are scattered on the surface, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 003 | 0.0 | 0 | 0.5 | 0 | 1 | The lid remains on the table throughout the rollout and is not placed on the jar, but all 7 coffee beans appear to have been scooped into the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 004 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and is never placed on the jar, and all coffee beans remain on the table surface rather than being collected inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 005 | 0.0 | 0 | 0 | 0 | 1 | The lid was not placed on the jar and the coffee beans remained on the table outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | The robot failed to place the lid on the jar and did not collect any coffee beans, leaving the jar open and empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The lid is on the table and the coffee beans remain on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 008 | 0.0 | 0 | 0 | 0 | 1 | The lid was not placed on the jar and no coffee beans were collected into the jar, as they remain visible on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | The lid was not placed on the jar and no coffee beans were collected into the jar, as both remained on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 010 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and no coffee beans are placed inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 011 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and the coffee beans remain scattered on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 012 | 0.28571 | 0 | 1 | 1 | 0 | The lid is securely placed on the jar and all 7 coffee beans are inside the jar as they are no longer visible on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and the coffee beans are never placed inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid is resting on the table and the coffee beans are scattered on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 015 | 0.0 | 0 | 0 | 0 | 1 | The jar is open and held by the robot, and all coffee beans remain on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 016 | 0.0 | 0 | 0 | 0 | 1 | The lid is lying on the table and not on the jar, and the coffee beans remain scattered on the table surface rather than inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 017 | 0.0 | 0 | 0 | 0 | 1 | The lid was never placed on the jar and no coffee beans were collected into the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 018 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and all coffee beans remain on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and all 7 coffee beans are still on the table outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 000 | 0.0 | 0 | 0 | 0 | 1 | The basket remains empty throughout the rollout, indicating that no detergent items were successfully placed or handed over. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 001 | 0.0 | 0 | 0 | 0 | 1 | The wooden box remains empty throughout the rollout and all three detergent bottles are left scattered on the counter surface. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 002 | 0.0 | 0 | 0.333333 | 0 | 1 | Only one detergent item (the white spray bottle) is visibly being held for handover, while the other two items remain on the counter and the basket is empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 003 | 0.0 | 0 | 0 | 0 | 1 | No detergent items were placed in the wooden box or handed over, as the box remains empty and all items are still scattered on the surface. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 004 | 0.0 | 0 | 0 | 0 | 1 | The wooden basket remains empty in the final frames, indicating that none of the detergent items were successfully placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 005 | 0.0 | 0 | 0 | 0 | 1 | The basket remains empty at the end of the rollout, indicating no detergent items were successfully placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 006 | 0.0 | 0 | 0 | 0 | 1 | The basket remains empty throughout the rollout and no detergent items are successfully placed or handed over. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 007 | 0.0 | 0 | 0 | 0 | 1 | The target basket remains empty throughout the rollout, indicating no detergent items were successfully placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 008 | 0.0 | 0 | 0.333333 | 0 | 1 | Only one detergent item (the white bottle) was successfully placed in the basket, while the green and blue bottles remained on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 009 | 0.0 | 0 | 0 | 0 | 1 | No detergent items were placed in the basket or handed over; all items remain on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 010 | 0.0 | 0 | 0 | 0 | 1 | The robot failed to place any of the three detergent items into the wooden basket, leaving them scattered on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 011 | 0.0 | 0 | 0 | 0 | 1 | The robot moved some items but the wooden box remains visibly empty in the final frames, indicating no detergent items were successfully placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 012 | 0.0 | 0 | 0 | 0 | 1 | The robot knocked the detergent bottles off the counter and the basket remains empty, so no items were successfully placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 013 | 0.0 | 0 | 0 | 0 | 1 | No detergent items were placed in the box or handed over; all three items remain on the counter surface. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 014 | 0.0 | 0 | 0 | 0 | 1 | The basket remains empty throughout the rollout, indicating no detergent items were successfully placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 015 | 0.0 | 0 | 0 | 0 | 1 | The basket remains empty and the detergent bottles are scattered on the counter, so no items are completed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 016 | 0.0 | 0 | 0 | 0 | 1 | The robot failed to place any of the three detergent bottles into the basket, leaving them scattered on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 017 | 0.0 | 0 | 0 | 0 | 1 | The basket is empty and no detergent items are visibly placed inside it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 018 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed in the basket; they remain scattered on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 019 | 0.0 | 0 | 0 | 0 | 1 | No detergent items were placed in the basket; all three items remain scattered on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 000 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table with temples unfolded and the box remains open throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 001 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses box is closed and the glasses are inside, but the folded temples are not visible. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses are inside the box, but the box is not fully closed and the temples are not folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 003 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded throughout the entire rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table with temples unfolded and the box remains open throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 005 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the box with temples unfolded, and the box remains open throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 006 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses temples appear folded, but the glasses remain outside the open box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 007 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table with temples unfolded and the box remains open throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 008 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with unfolded temples at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 009 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain unfolded and outside the open box throughout the entire rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside with temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 012 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses are inside the box and the temples are folded, but the box lid remains open. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 013 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with their temples unfolded throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 014 | 0.0 | 0 | 0.666667 | 0 | 1 | The glasses box is closed and the glasses are inside, but the temples were last seen unfolded and never visibly folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 015 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses are inside the box, but the temples are not folded and the box is not closed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 016 | 0.0 | 0 | 0 | 0 | 1 | The glasses temples are not folded, the box is open, and the glasses are not inside the box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 017 | 0.0 | 0 | 0 | 0 | 1 | The glasses are held by the robot with temples unfolded and are not inside the open box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 018 | 0.0 | 0 | 0 | 0 | 1 | The glasses are not inside the box, the temples are not folded, and the box remains open. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 019 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 000 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both remain on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 001 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed in the holder; they remain on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is on the holder; the spoon is moved into the sink and the fork remains on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 003 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder, as the holder remains empty throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | The robot moved the holder but did not place either the spoon or the fork onto it; both utensils remain on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 005 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both remain on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 006 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is visible inside the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 007 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork remains on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | The robot pushed the holder away and neither the spoon nor the fork was placed on it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed in the holder; both utensils remain on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 010 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork was placed on the holder; the robot interacted with the holder and a plate but left the utensils on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 011 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed in the holder; both remain on the table surface in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | The spoon and fork remain on the table throughout the visible rollout and are never placed into the holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 013 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is successfully placed on the holder, but the spoon remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both utensils remain on the table surface throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both remain visible on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 016 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both remain on the table surface. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 017 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; the spoon remains on the table and the holder is empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 018 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork was placed on the holder; both remained on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | In the final frame, the spoon is lying on the table next to the holder and the fork is held by the gripper, so neither utensil is placed on the holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface throughout the rollout and is never placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table to the right of the bowl and is never placed inside the empty fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 002 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the white fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty at the end of the rollout, and the apple is not inside it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 004 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table while the robot arm hovers over the empty fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 005 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table to the right of the bowl and is not placed inside it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The green apple is clearly placed inside the green fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 007 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly placed inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl remains empty at the end of the rollout, indicating the apple was not placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 009 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 010 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible resting inside the fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 011 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is never placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in the final frames, indicating the apple was not placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 013 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table to the right of the bowl throughout the rollout and is never placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 015 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and is not placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 016 | 0.0 | 0 | 1 | 1 | 0 | The apple is clearly visible inside the white fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table next to the bananas and is not inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table to the right and is never placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The apple is not visible inside the fruit bowl; the bowl appears empty in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is held by the robot or lying on the table away from the book, never achieving the required overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 002 | 1.0 | 1 | 1 | 1 | 1 | The white bookmark is successfully placed on the open page of the book with significant overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 003 | 1.0 | 1 | 1 | 1 | 1 | The yellow bookmark is visibly placed on top of the open book with significant overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 004 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is successfully placed on the open book with sufficient overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 005 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on the open book with significant overlap, satisfying the condition. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible lying on the table in earlier frames and is not placed on the book in the final state. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 007 | 1.0 | 1 | 0 | 0 | 0 | The bookmark (green card) remains on the table and was not placed on the book; the robot placed a tool on the book instead. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The robot holds the bookmark throughout the sequence but never places it on the book. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 009 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on top of the open book with significant overlap exceeding 40%. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible lying on the table in earlier frames and is not placed on the book in the final state. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 011 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on top of the open book with significant overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is lying on the table far away from the book with no overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 013 | 1.0 | 1 | 0 | 0 | 0 | The robot placed a white tube-like object on the book, while the actual bookmark remains untouched on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table surface far from the book and is never placed on top of it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible on the table next to the book but not placed on top of it with sufficient overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The robot is holding the yellow bookmark and has not placed it on the open book. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 017 | 1.0 | 1 | 1 | 1 | 1 | The white bookmark is visibly placed on top of the open book pages with significant overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frames, indicating it was not successfully placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 019 | 1.0 | 1 | 1 | 1 | 1 | The blue bookmark is clearly placed on the open book's page with significant visible overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | The lid remains on the table and the coffee beans are still scattered on the table surface, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 001 | 0.5 | 0 | 0.5 | 0 | 1 | The coffee beans are inside the jar, but the lid is lying on the table next to the jar instead of being placed on it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | The lid remained on the table and was never placed on the jar, and all coffee beans remained on the table surface. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 003 | 0.42857 | 0 | 0 | 0 | 1 | The lid is placed next to the jar rather than on it, and no coffee beans are visibly inside the jar at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 004 | 0.5 | 0 | 1 | 1 | 0 | The lid is securely placed on the jar and all coffee beans are visibly inside the jar with none remaining on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 005 | 0.35714 | 0 | 0.5 | 0 | 1 | All 7 coffee beans are inside the jar, but the lid was not placed on the jar and remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 006 | 0.0 | 0 | 0.5 | 0 | 1 | The coffee beans are inside the jar, but the lid remains on the table and was not placed on the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The lid is placed on the table and all coffee beans remain on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 008 | 0.5 | 0 | 0.5 | 0 | 1 | The coffee beans are inside the jar, but the lid is resting on the table next to the jar instead of being placed on top. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 009 | 0.42857 | 0 | 0.5 | 0 | 1 | The coffee beans are successfully collected inside the jar, but the lid is lying on the table next to the jar rather than being placed on top. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 010 | 0.14286 | 0 | 0 | 0 | 1 | The lid remains on the table and the coffee beans are still visible on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 011 | 0.21429 | 0 | 0.857143 | 0 | 1 | The lid is on the jar, but only 5 of the 7 coffee beans are inside the jar while 2 remain on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 012 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 013 | 0.5 | 0 | 1 | 1 | 0 | The lid is visibly placed on the jar and all coffee beans are inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and all coffee beans are visible on the table surface, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 015 | 0.07143 | 0 | 0 | 0 | 1 | The lid is on the table and the coffee beans remain on the table outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 016 | 0.0 | 0 | 0 | 0 | 1 | The lid is placed on the table instead of the jar, and all coffee beans remain scattered on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 017 | 0.14286 | 0 | 0.357143 | 0 | 1 | The lid is not on the jar, and only 5 of the 7 coffee beans are visible inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 018 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and all 7 coffee beans are still visible on the table, so no part of the task was completed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 019 | 0.5 | 0 | 0.5 | 0 | 1 | The coffee beans are successfully inside the jar, but the lid is lying on the table next to the jar and not placed on top. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 000 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items (blue bottle, green spray, white spray) were successfully placed into the wooden basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 001 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles were successfully picked up and placed into the wooden box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 002 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items were successfully picked up and placed into the wooden basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 003 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items (blue bottle, green spray bottle, and white spray bottle) were successfully picked up and placed into the wooden basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 004 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles were successfully picked up and placed into the wooden basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 005 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles (blue, green, and white) are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 006 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 007 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 008 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items (blue bottle, green spray, and white spray) are visibly placed inside the wooden basket by the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 009 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items (blue bottle, grey bottle, and white spray bottle) are visibly placed inside the wooden basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 010 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles were successfully picked up and placed into the wooden box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 011 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles were successfully picked up and placed into the wooden box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 012 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 013 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items (small blue bottle, white spray bottle, and blue OxiClean bottle) were successfully picked up and placed into the wooden box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 014 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items (purple spray bottle, white spray bottle, and blue OxiClean bottle) were successfully picked up and placed into the wooden box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 015 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 016 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 017 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 018 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 019 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles were successfully picked up and placed into the wooden basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 000 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses are inside the box with temples folded, but the box lid remains open. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 001 | 0.66667 | 0 | 0.333333 | 0 | 1 | The box is closed, but the glasses are underneath it rather than inside, and the temples are not folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 002 | 1.0 | 1 | 1 | 1 | 1 | The glasses are inside the closed box with both temples folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 003 | 1.0 | 1 | 1 | 1 | 1 | The glasses are placed inside the box with temples folded, and the box is fully closed in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 004 | 0.0 | 0 | 0.666667 | 0 | 1 | The robot placed the glasses in the box and closed the lid, but the temples were never folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 005 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are left outside with unfolded temples. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 006 | 0.66667 | 0 | 1 | 1 | 0 | The robot successfully folded both temples, placed the glasses inside the box, and fully closed the box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 007 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are not completely inside as a temple arm is visibly sticking out, and the temples are not folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 008 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses are placed inside the box, but the temples are not folded and the box remains open in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 009 | 0.0 | 0 | 1 | 1 | 0 | The glasses temples are folded, the glasses are inside the box, and the box is fully closed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 010 | 0.0 | 0 | 0.666667 | 0 | 1 | The temples are folded and the box is closed, but the glasses are visibly protruding from the box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 011 | 1.0 | 1 | 1 | 1 | 1 | The glasses temples are folded, the glasses are placed inside the box, and the box is fully closed in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 012 | 1.0 | 1 | 1 | 1 | 1 | The glasses are inside the box with temples folded, and the box is fully closed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 013 | 1.0 | 1 | 1 | 1 | 1 | The glasses are inside the fully closed box with both temples folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are outside the box with their temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 015 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses are placed inside the box, but the temples are not folded and the box is not fully closed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 016 | 1.0 | 1 | 1 | 1 | 1 | The robot folded the glasses temples, placed the glasses inside the box, and fully closed the box lid. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 017 | 0.0 | 0 | 0.333333 | 0 | 1 | The box is closed, but the glasses temples are not folded and are protruding from the box, so the glasses are not completely inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 018 | 1.0 | 1 | 1 | 1 | 1 | The glasses were placed in the box with temples folded, and the box was subsequently closed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 019 | 0.0 | 0 | 0.333333 | 0 | 1 | The box is closed, but the glasses are not completely inside as one temple is sticking out, and the temples do not appear properly folded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 000 | 0.0 | 0 | 0 | 0 | 1 | The holder is empty in the final frames, with both the spoon and fork remaining on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 001 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is successfully placed in the holder, but the spoon is still being held by the robot arm and has not been placed yet. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed in the holder; both remain on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 003 | 0.0 | 0 | 0 | 0 | 1 | The holder remains empty throughout the rollout, and the fork is visible on the table in the final frames while the spoon is missing. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; the spoon remains on the table and the fork is manipulated but not successfully placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 005 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is successfully placed in the holder, but the spoon is still being held by the robot gripper and has not been released. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 006 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 007 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the table surface and are not placed in the holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both utensils remain on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 010 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 011 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 012 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed on the holder, but the fork remains on the table and was not placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 013 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork remains on the table and is not placed in the holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 014 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both utensils remain on the table surface. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 016 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is successfully placed on the holder, but the spoon remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 017 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork is not. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 018 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork is not visible in the holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both remain on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface next to the bananas and is not inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is not inside the fruit bowl at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table next to the bowl and is not placed inside it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is not inside the fruit bowl at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 004 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the white fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 005 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible resting inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the green fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 007 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is never placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface near the bananas and is not inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 009 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface to the right of the bowl throughout the entire sequence and is never placed inside the bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 010 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible resting inside the fruit bowl in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 011 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible resting inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is visibly empty in the final frames, and the apple is not inside it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 013 | 1.0 | 1 | 1 | 1 | 1 | The apple is clearly visible resting inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 015 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and was not placed inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 016 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table next to the bowl throughout the rollout and is never placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table to the right of the bowl throughout the rollout and is never placed inside. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table surface and is not inside the fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and is never placed inside the empty fruit bowl. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 000 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is visible on the far left side of the table and not placed on the book. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 001 | 1.0 | 1 | 1 | 1 | 1 | The yellow bookmark is clearly placed on the open book with significant visible overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book; it remains separate on the table near the pen holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 003 | 1.0 | 1 | 1 | 1 | 1 | The yellow bookmark is visibly placed on the open book with significant overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 004 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the open book; the book pages are empty in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 005 | 1.0 | 1 | 0 | 0 | 0 | The robot placed a blue bottle-like object on the book, while the actual colorful bookmark remains untouched near the pen holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 007 | 1.0 | 1 | 1 | 1 | 1 | The robot successfully placed the long grey bookmark object onto the open book with significant visible overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 009 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is clearly placed on the open book with significant visible overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book; the book remains empty in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 011 | 1.0 | 1 | 1 | 1 | 1 | The black bookmark is visibly placed on the open book's page with significant overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is lying on the table surface next to the book, not placed on top of it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 013 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is clearly placed on the open book with significant visible overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is never placed on the book; it remains on the table or out of view while the book stays open without it. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is visible next to the book but is never placed on top of it with the required overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk near the pencil holder and is never placed on the open book. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 017 | 1.0 | 1 | 1 | 1 | 1 | The white bookmark is successfully placed on the open page of the book with full overlap. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book; the open book pages are clearly visible without the bookmark on top. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | bookmark_on_book | 019 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on the book in the final frame, as the book pages are empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and the coffee beans are still scattered outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 001 | 0.5 | 0 | 1 | 1 | 0 | The lid is securely placed on the jar and all 7 coffee beans are visibly inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 002 | 0.07143 | 0 | 0.5 | 0 | 1 | The lid is placed on the jar, but the coffee beans remain on the table and were not collected. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 003 | 0.42857 | 0 | 0.714286 | 0 | 1 | The lid is placed on the jar, but only 3 of the 7 coffee beans are visibly inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 004 | 0.5 | 0 | 1 | 1 | 0 | The lid is securely placed on the jar and all 7 coffee beans are inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 005 | 0.0 | 0 | 0 | 0 | 1 | The lid is on the table and not on the jar, and no coffee beans are clearly visible inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and the coffee beans are still on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The jar is not visible in the final frames, so the lid placement and beans inside cannot be verified. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 008 | 0.42857 | 0 | 1 | 1 | 0 | The lid is placed on the jar and all 7 coffee beans are visibly inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and the coffee beans remain on the table outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 010 | 0.0 | 0 | 0 | 0 | 1 | The lid is lying on the table next to the jar, and the coffee beans are scattered on the table outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 011 | 0.35714 | 0 | 0.857143 | 0 | 1 | The lid is placed on the jar, but only 5 of the 7 coffee beans are inside while 2 remain visible on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 012 | 0.0 | 0 | 0 | 0 | 1 | The lid is placed next to the jar rather than on it, and the coffee beans remain visible on the table outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | The lid is resting on the spoon holder and the coffee beans remain on the table, not inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid was placed on a stand rather than the jar, and all coffee beans remained on the table outside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 015 | 0.42857 | 0 | 1 | 1 | 0 | The lid is placed on the jar and all 7 coffee beans are visibly inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 016 | 1.0 | 1 | 1 | 1 | 1 | The lid is securely placed on the jar and all 7 coffee beans are visibly inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 017 | 1.0 | 1 | 0 | 0 | 0 | The lid is tilted open and not parallel to the tabletop, and the coffee beans are not clearly visible inside the jar at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 018 | 1.0 | 1 | 1 | 1 | 1 | The lid is securely placed on the jar and all 7 coffee beans are visibly inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | The lid is not placed on the jar and no coffee beans are inside the jar. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 000 | 0.66667 | 0 | 0.666667 | 0 | 1 | Only 2 of the 3 detergent items (green and white bottles) are visibly placed in the basket, while the blue bottle is removed from the counter but not seen in the basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 001 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent item (the green bottle) is visibly placed inside the wooden box, while the other items remain on the counter or are being held by the robot. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 002 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two of the three detergent items are visibly placed in the basket, while one remains on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 003 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items (green and white bottles) were placed in the box, but the blue bottle remained on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 004 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent item (the white bottle) was visibly placed into the basket, while the other two items remained on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 005 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items (blue, green, and white bottles) are visibly placed inside the basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 006 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are placed in the basket, but the third grey bottle remains on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 007 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 008 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent item (the blue spray bottle) is visibly placed in the basket, while the green spray and white bottle remain on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 009 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed in the basket, but the third blue bottle remains on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 010 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items were successfully placed in the wooden box, but the third blue bottle remained on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 011 | 0.0 | 0 | 0.333333 | 0 | 1 | Only one detergent item (the white bottle) is visibly placed inside the wooden box, while the other items remain on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 012 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed in the basket, but the third purple bottle remains on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 013 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one of the three detergent items is visibly placed in the wooden box, while the other two remain on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 014 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles were successfully picked up and placed into the wooden basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 015 | 0.0 | 0 | 0.666667 | 0 | 1 | Two detergent bottles were successfully placed in the basket, but the third blue bottle with the yellow top remained on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 016 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed in the basket, but the third purple bottle remains on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 017 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 018 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed inside the basket, but the third blue bottle remains on the surface outside the basket. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | detergent | 019 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed inside the basket, while the third bottle remains on the counter. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 000 | 0.33333 | 0 | 0 | 0 | 1 | The glasses remain outside the box with temples unfolded and the box open throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 001 | 0.33333 | 0 | 0 | 0 | 1 | The glasses remain unfolded on the table and were not placed inside the box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are outside on the table with temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 003 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are outside on the table with temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table with temples open and the box remains open throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 005 | 0.0 | 0 | 1 | 1 | 0 | The robot folded the glasses' temples, placed them inside the box, and fully closed the box lid. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 006 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside on the table with their temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 007 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are held outside with unfolded temples. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 008 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses are inside the box with temples folded, but the box remains open at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 009 | 0.33333 | 0 | 0.666667 | 0 | 1 | The robot successfully folded the glasses temples and closed the box, but the glasses were left on the table outside the closed box. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are outside on the table with temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain on the table with temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 012 | 1.0 | 1 | 1 | 1 | 1 | The glasses are inside the box with temples folded, and the box is fully closed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 013 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are outside with unfolded temples. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside with temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 015 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside with unfolded temples. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 016 | 0.66667 | 0 | 1 | 1 | 0 | The glasses are inside the box with temples folded, and the box is fully closed as seen in the final frames. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 017 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside on the table with their temples unfolded. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 018 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside with unfolded temples. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | put_glass_in_glassbox | 019 | 0.33333 | 0 | 0.333333 | 0 | 1 | The temples appear folded, but the glasses are not completely inside the box and the box is not fully closed as a temple is protruding. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 000 | 1.0 | 1 | 1 | 1 | 1 | Both the wooden spoon and the white fork are clearly placed inside the grey dish rack holder in the final frame. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 001 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed on the holder, but the fork is not visible on the holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | The spoon and fork are placed on the white plate, while the grey utensil holder remains empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 003 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork is not placed in the holder by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 004 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is successfully placed on the holder, but the spoon remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 005 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed on the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 006 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork is still being held by the robot arm at the end of the video and has not been placed. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 007 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed in the holder; both remain on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both remain on the table surface at the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 009 | 0.0 | 0 | 0.5 | 0 | 1 | The fork is placed in the holder, but the spoon remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 010 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 011 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; the spoon is on the plate and the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; both remain on the table surface. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 013 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed on the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed in the holder; both remain on the table throughout the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder; the fork remains on the table and the holder compartments appear empty. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 016 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the holder, but the fork is placed on a plate instead of the holder. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 017 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork remains on the table. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 018 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is successfully placed in the holder, but the fork is not visible in the holder by the end of the rollout. | 50 | 1 | 1 | synced_camera_composite |
| qwen3.6-plus | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | The spoon is placed on the plate and the fork remains on the table, so neither utensil is on the holder. | 50 | 1 | 1 | synced_camera_composite |

## Mismatches

- apple_to_fruit_bowl/009: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/010: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/007: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/014: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/012: sim_success=0, vlm_success=1, vlm_score=1.0
- apple_to_fruit_bowl/016: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/007: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/013: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/004: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/013: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/006: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/009: sim_success=0, vlm_success=1, vlm_score=1.0
- bookmark_on_book/000: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/005: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/001: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/004: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/008: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/015: sim_success=0, vlm_success=1, vlm_score=1.0
- collect_coffee_beans/017: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/005: sim_success=0, vlm_success=1, vlm_score=1.0
- put_glass_in_glassbox/016: sim_success=0, vlm_success=1, vlm_score=1.0
