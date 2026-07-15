# GPT Rollout Score Report

- num_rollouts: 360
- scored_rollouts: 360
- failed_rollouts: 0
- agreement_rate: 0.911

| model | task_id | episode_id | sim_score | sim_success | vlm_score | vlm_success | agreement | reason | source_frames | sent_frames | max_images | frame_mode |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| gpt-5 | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the tabletop near the right edge while the fruit bowl is empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 001 | 1.0 | 1 | 1 | 1 | 1 | In the final frame, the apple is visibly resting inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | At the end, the apple remains outside the bowl on the table and is not placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The bowl remains empty and the apple is not inside it at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 004 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 005 | 0.0 | 0 | 0 | 0 | 1 | At the end, the fruit bowl is empty and the apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 006 | 1.0 | 1 | 0 | 0 | 0 | The final frames show the apple near or on the rim of the bowl, not clearly placed inside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 007 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the right edge while the fruit bowl is empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 009 | 0.0 | 0 | 0 | 0 | 1 | The red apple remains on the table beside the bowl and is not inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 010 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table outside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 011 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and the fruit bowl is empty at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 013 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl in the final frame. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 015 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 016 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple is not inside the fruit bowl at the end; the bowl remains visibly empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and is not inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and the bowl is empty at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is on the table next to the open book with no substantial overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The pink bookmark remains on the table beside the book and is not placed with sufficient overlap on the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not on top of the book; no visible overlap between the bookmark and the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 003 | 0.0 | 0 | 0 | 0 | 1 | The bookmark stays on the table beside the open book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 004 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on top of the book at the end, with no overlap between them. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 005 | 0.0 | 0 | 0 | 0 | 1 | The blue bookmark is not on the open book at the end; the book is bare with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk (near the mug) and is not on the book, with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 007 | 0.0 | 0 | 0 | 0 | 1 | The yellow bookmark is not on top of the book at the end; the book pages are clear with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The bookmark stays on the desk and is never placed on top of the book with sufficient overlap before the rollout ends. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 009 | 0.0 | 0 | 0 | 0 | 1 | The bookmark stays on the table edge and is not placed on top of the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table and is not placed on the book with visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 011 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk beside the open book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk away from the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 013 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly on top of the book in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | In the final frames the bookmark is not on top of the book and shows no visible overlap with it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk beside the book with no substantial overlap visible. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk and is not placed on top of the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 017 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book; no visible overlap between the bookmark and the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark never appears on the book and remains near the table edge with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 019 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visible on top of the book at the end, with no overlap evident. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 001 | 0.0 | 0 | 0 | 0 | 1 | The lid is off to the side and all seven coffee beans remain on the table outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | At the end, the lid is off the jar and all coffee beans are on the table with none visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 003 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 004 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and the coffee beans are still on the tabletop, with none visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 005 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all seven coffee beans remain on the table with none visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all seven coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The lid is off to the side and the seven coffee beans remain on the table, with none visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 008 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain on the table, with none visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain on the table outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 010 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all seven beans remain outside the jar on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 011 | 0.0 | 0 | 0 | 0 | 1 | The lid remains off the jar and all coffee beans are still on the table, not inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 012 | 0.28571 | 0 | 0.5 | 0 | 1 | The lid is placed on the jar, but no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain on the table outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 015 | 0.0 | 0 | 0 | 0 | 1 | The jar remains open without the lid and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 016 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end; beans remain on the table and the jar is not used. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 017 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 018 | 0.0 | 0 | 0 | 0 | 1 | The lid stays on the table and all seven beans are visible on the tabletop outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all seven coffee beans are still on the table outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 000 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are placed or handed over; all remain on the counter and the basket is empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 001 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed or handed over; the basket remains empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 002 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed or handed over; the basket remains empty throughout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 003 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are placed in the basket or handed over; all three remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 004 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed in the basket or handed over by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 005 | 0.0 | 0 | 0 | 0 | 1 | All three detergent items remain on the counter and none are placed in the basket or otherwise completed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 006 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 007 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed or handed over; all remain on the counter and the basket is empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 008 | 0.0 | 0 | 0.333333 | 0 | 1 | Only the white detergent is visibly placed in the basket, while the green and blue bottles remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 009 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are placed or handed over as required; all three remain on the counter and the basket is empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 010 | 0.0 | 0 | 0 | 0 | 1 | All three detergent items remain on the counter and none are visibly placed or handed over as required. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 011 | 0.0 | 0 | 0 | 0 | 1 | None of the three detergent items are visibly placed or handed over to the required location; all remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 012 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 013 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are placed in the basket; all three remain outside on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 014 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed in the target container or handed over; all remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 015 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 016 | 0.0 | 0 | 0 | 0 | 1 | All detergent items remain on the counter and none are visibly placed into the basket or handed over. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 017 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are placed as required; the basket is empty and all items remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 018 | 0.0 | 0 | 0 | 0 | 1 | No detergent items are visibly placed or handed over; all three bottles remain on the counter and the basket is empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 019 | 0.0 | 0 | 0 | 0 | 1 | All three detergent items remain on the counter and the basket is empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 000 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table with both temples unfolded and the box stays open, never containing the glasses. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 001 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are not visible inside and there is no evidence of both temples being folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses are inside the open box, but the temples are not folded and the box is not closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 003 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples not folded and the box not closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded and the box not closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 005 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded throughout the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 006 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table beside the open box with temples unfolded, and the box is not closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 007 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded and the box never closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 008 | 0.0 | 0 | 0 | 0 | 1 | The glasses stay outside the open box with temples not folded and the box remains open throughout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 009 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box, the temples are not folded, and the box is not closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses case is closed, but the glasses remain outside the box with temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 012 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses are placed inside the box, but the temples are not folded and the box remains open. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 013 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain on the table with temples unfolded and the box is open, not containing the glasses. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 014 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses box appears closed, but the glasses are not inside it and both temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 015 | 0.0 | 0 | 0 | 0 | 1 | The box remains open with the glasses mostly outside and the temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 016 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with temples unfolded, and the box is not closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 017 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box with both temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 018 | 0.0 | 0 | 0 | 0 | 1 | Glasses remain outside the open box with both temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 019 | 0.0 | 0 | 0 | 0 | 1 | The glasses stay outside the open box with both temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 000 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visibly on the holder at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 001 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the table and are not placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visibly placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 003 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | Neither spoon nor fork is on the holder; both remain off the holder in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 005 | 0.0 | 0 | 0 | 0 | 1 | The spoon and fork remain on the table beside the holder, with neither placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 006 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the table, not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 007 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed on the holder, while the fork remains on the table off the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the holder by the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | In the final frames, the spoon remains on the countertop and the fork is not on the holder; the holder appears empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 010 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 011 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork are visibly placed on the holder; both remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain on the table and not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 013 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is placed in the holder while the spoon remains on the table, not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visibly placed in the utensil holder by the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 016 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 017 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is on the holder at the end; both remain off the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 018 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain on the countertop and are not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is on the holder; both remain off the holder at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the bananas and is not inside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table while the fruit bowl appears empty at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 002 | 1.0 | 1 | 0 | 0 | 0 | The apple is held above the bowl at the end and is not visibly inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl appears empty at the end, with no apple visible inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 004 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table outside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 005 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the right edge and the fruit bowl is visibly empty at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 007 | 1.0 | 1 | 1 | 1 | 1 | The required final state is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The apple falls off the table and the bowl remains empty at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 009 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 010 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 011 | 0.0 | 0 | 0 | 0 | 1 | The bowl is empty at the end and the apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is empty at the end and the apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 013 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and the fruit bowl is empty at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the wooden fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 015 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the bananas and is not inside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 016 | 0.0 | 0 | 0 | 0 | 1 | The bowl appears empty at the end and the apple is not visible inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The bowl appears empty at the end with no apple inside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table outside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The bowl remains empty at the end, and the apple is not visible inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 000 | 0.0 | 0 | 0 | 0 | 1 | The pink bookmark remains on the table beside the book with little to no overlap, not placed on top of the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 001 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table beside the book, with no significant overlap visible. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 002 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains on the table next to the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 003 | 1.0 | 1 | 1 | 1 | 1 | The bookmark is visibly placed on top of the open book with substantial (over 40%) overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 004 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains off to the side in the gripper and is not placed on the open book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 005 | 1.0 | 1 | 0 | 0 | 0 | The bookmark does not appear on top of the book; the book’s pages are visible without a significant overlapping bookmark. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not on the book at the end; it is absent from the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 007 | 1.0 | 1 | 0 | 0 | 0 | The tan bookmark is not on the book; a grey tool is placed on the book instead. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk and does not overlap the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 009 | 1.0 | 1 | 1 | 1 | 1 | The bookmark rests on top of the open book with clearly more than 40% visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the desk separate from the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 011 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not on the book; the open book remains clear with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is left on the table away from the book, with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 013 | 1.0 | 1 | 0 | 0 | 0 | The bookmark ends up on a gray surface near the robot, not on the book, so there is no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains beside the book and is not placed on top with sufficient overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The pink bookmark remains on the table beside the book with no significant overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The bookmark never appears on top of the book, with no visible overlap in the final views. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 017 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains on the desk beside the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark ends up away from the book rather than overlapping it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 019 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains on the desk and not on the book, with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 000 | 0.14286 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visible inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 002 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and all seven coffee beans are still outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 003 | 0.42857 | 0 | 0 | 0 | 1 | The lid is not placed on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 004 | 0.5 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 005 | 0.35714 | 0 | 0.357143 | 0 | 1 | The lid is not on the jar and two coffee beans remain on the table with only some (about five) visible inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | At the end the jar is off the table with the lid not on it and no beans visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain on the table outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 008 | 0.5 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 009 | 0.42857 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 010 | 0.14286 | 0 | 0 | 0 | 1 | The lid is on the table and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 011 | 0.21429 | 0 | 0 | 0 | 1 | The lid is not on the jar and coffee beans remain on the table with none visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 012 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all seven coffee beans remain on the tabletop, not inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 013 | 0.5 | 0 | 0 | 0 | 1 | The lid remains off the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid stays on the table and the jar appears empty with beans still outside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 015 | 0.07143 | 0 | 0 | 0 | 1 | The lid is off and all seven coffee beans remain on the tabletop outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 016 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain outside the jar on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 017 | 0.14286 | 0 | 0 | 0 | 1 | The lid is on the table, not on the jar, and all coffee beans remain outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 018 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 019 | 0.5 | 0 | 0 | 0 | 1 | At the end the lid is off the jar on the table and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 000 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket by the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 001 | 1.0 | 1 | 0.666667 | 0 | 0 | Two detergent items are visibly placed in the basket, while the third is not clearly completed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 002 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 003 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the wooden box by the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 004 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 005 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 006 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 007 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 008 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 009 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 010 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 011 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the wooden box at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 012 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 013 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 014 | 1.0 | 1 | 0.666667 | 0 | 0 | Two detergent bottles are visibly placed inside the basket, while the third is not visibly completed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 015 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 016 | 1.0 | 1 | 1 | 1 | 1 | By the final frame, all three detergent bottles are clearly placed inside the basket. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 017 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed into the basket. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 018 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 019 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 000 | 0.33333 | 0 | 0.666667 | 0 | 1 | The glasses are inside the box with both temples folded, but the box lid remains open. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 001 | 0.66667 | 0 | 0.333333 | 0 | 1 | The glasses box appears closed, but the glasses remain outside the box with unfolded temples. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 002 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses are placed inside the box and the box is closed, but one temple remains unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 003 | 1.0 | 1 | 1 | 1 | 1 | The glasses were placed inside the box with both temples visibly folded, and the lid was closed at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the open box and the temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 005 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside and the temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 006 | 0.66667 | 0 | 0.666667 | 0 | 1 | The glasses are placed inside the box and the box is closed, but both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 007 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses are not inside the box and the temples are not folded, but the box is closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 008 | 0.0 | 0 | 0 | 0 | 1 | The box remains open and appears empty with no glasses inside, and the temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 009 | 0.0 | 0 | 0.666667 | 0 | 1 | The glasses appear placed inside the case and the case is closed, but both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 010 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses box appears closed, but the glasses are outside it with temples not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 011 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses are placed inside the box and the box is closed, but both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 012 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses are visibly inside the box and the box is closed, but both temples remain unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 013 | 1.0 | 1 | 0.333333 | 0 | 0 | The box is closed in the final frames, but the glasses are not inside and the temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0 | 0 | 1 | The glasses stay outside the box with both temples unfolded, and the box is not visibly closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 015 | 0.0 | 0 | 0 | 0 | 1 | The glasses are outside an open box with temples not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 016 | 1.0 | 1 | 0.666667 | 0 | 0 | The glasses were placed inside and the box was closed, but both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 017 | 0.0 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are outside and their temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 018 | 1.0 | 1 | 0.666667 | 0 | 0 | The box is closed with the glasses inside, but both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 019 | 0.0 | 0 | 0.666667 | 0 | 1 | The glasses are inside the box and the box is closed, but the temples are not folded (one is protruding). | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 000 | 0.0 | 0 | 0 | 0 | 1 | At the end, both the spoon and the fork remain on the countertop and not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 001 | 0.5 | 0 | 0 | 0 | 1 | At the end, the spoon remains on the table and the fork lies on the drying rack rather than on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 003 | 0.0 | 0 | 0 | 0 | 1 | The holder is empty at the end; neither the spoon nor the fork is on it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 004 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the gray utensil holder; both remain on the countertop. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 005 | 0.5 | 0 | 0 | 0 | 1 | By the end, the spoon is on the table and the fork is in the drying rack, with neither placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 006 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is on the holder, while the fork remains on the table and not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 007 | 0.5 | 0 | 0.5 | 0 | 1 | Exactly one half-credit condition is visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and fork remain on the table rather than on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | The holder is empty while both the spoon and fork remain on the table, not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 010 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed in the utensil holder, but the fork remains on the countertop and not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 011 | 0.5 | 0 | 0 | 0 | 1 | The spoon is in the drying rack and the fork is on the table, with neither placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 012 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is clearly on the holder while the fork remains on the countertop. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 013 | 0.5 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is on the utensil holder; the spoon lies on the drying rack and the fork remains on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 014 | 0.5 | 0 | 0 | 0 | 1 | Neither utensil is on the holder; the spoon is in the drying rack and the fork remains off the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the table and are not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 016 | 0.5 | 0 | 0 | 0 | 1 | The spoon remains on the table and the fork is in the drying rack, with neither utensil on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 017 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is placed on the holder, but the fork is not visibly on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 018 | 0.5 | 0 | 0.5 | 0 | 1 | The wooden spoon ends up on the holder, but the fork is not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 019 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the countertop rather than on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 000 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table and is not placed inside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 001 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the edge and is not inside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 002 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table beside the bowl, which appears empty at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 003 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the right edge and is never placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 004 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 005 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 006 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly resting inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 007 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table outside the bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 008 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the edge and is not inside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 009 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the right edge and is not placed inside the fruit bowl. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 010 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 011 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 012 | 0.0 | 0 | 0 | 0 | 1 | The bowl remains empty and the apple is not visible inside it at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 013 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly inside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 014 | 1.0 | 1 | 1 | 1 | 1 | The apple is visibly placed inside the fruit bowl in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 015 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table outside the fruit bowl at the end of the rollout. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 016 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table next to the bowl, not inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 017 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table near the right edge and the bowl appears empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 018 | 0.0 | 0 | 0 | 0 | 1 | The apple remains on the table outside the fruit bowl at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | apple_to_fruit_bowl | 019 | 0.0 | 0 | 0 | 0 | 1 | The fruit bowl is empty at the end, and the apple is not inside it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 000 | 1.0 | 1 | 0 | 0 | 0 | The pink bookmark remains on the table beside the open book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 001 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains on the table beside the book without visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 002 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on top of the book; no visible overlap is present. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 003 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains on the table separate from the book, with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 004 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book and remains elsewhere on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 005 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not on the book at the end; it remains off the book with no significant overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 006 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not on the open book at the end, with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 007 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not visibly placed on the book; no substantial overlap is seen. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 008 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not on the book at the end, with no visible overlap between them. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 009 | 1.0 | 1 | 0 | 0 | 0 | The bookmark remains on the table/robot surface and is not placed on the open book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 010 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains off the book and is not visibly placed on top with sufficient overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 011 | 1.0 | 1 | 0 | 0 | 0 | The pink bookmark remains on the table and is not on top of the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 012 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is on the desk beside the book with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 013 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not on the book; it remains off to the side and not overlapping the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 014 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is never visibly placed on top of the book; it ends up away from the book near the pencil holder/off-screen. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 015 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains on the table separate from the book, with no visible overlap. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 016 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not visibly placed on top of the book with sufficient overlap in the final frames. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 017 | 1.0 | 1 | 0 | 0 | 0 | The bookmark is not placed on the open book; no visible overlap between them. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 018 | 0.0 | 0 | 0 | 0 | 1 | The bookmark remains off the book, with no visible overlap on the book. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | bookmark_on_book | 019 | 0.0 | 0 | 0 | 0 | 1 | The bookmark is not placed on the book and remains elsewhere on the desk. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 000 | 0.0 | 0 | 0 | 0 | 1 | The jar remains open with the lid on the table away from it, and all seven coffee beans are still outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 001 | 0.5 | 0 | 0 | 0 | 1 | At the end the jar is open with no lid on it and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 002 | 0.07143 | 0 | 0.5 | 0 | 1 | The lid is placed on the jar, but all seven coffee beans remain outside on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 003 | 0.42857 | 0 | 0.357143 | 0 | 1 | The lid is not on the jar, and only about five coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 004 | 0.5 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 005 | 0.0 | 0 | 0 | 0 | 1 | The jar remains open with the lid on the table and no coffee beans visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 006 | 0.0 | 0 | 0 | 0 | 1 | The lid is left on the table and the coffee beans remain outside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 007 | 0.0 | 0 | 0 | 0 | 1 | At the end the jar and lid are not visible on the table and no beans are visibly inside a jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 008 | 0.42857 | 0 | 0 | 0 | 1 | At the end, the lid is tilted and not properly on the jar, and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 009 | 0.0 | 0 | 0 | 0 | 1 | The lid remains on the table and multiple coffee beans are still outside the jar with none visibly inside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 010 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and the coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 011 | 0.35714 | 0 | 0 | 0 | 1 | The lid is tilted and not properly on the jar, and two beans remain on the table with no beans visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 012 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 013 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and no coffee beans are visible inside the jar; beans remain on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 014 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain outside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 015 | 0.42857 | 0 | 0 | 0 | 1 | The loose lid stays on the table rather than on the jar, and no coffee beans are clearly visible inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 016 | 1.0 | 1 | 0 | 0 | 0 | The lid is not on the jar and no coffee beans are visibly inside the jar at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 017 | 1.0 | 1 | 0.5 | 0 | 0 | The lid is not on the jar at the end, and all seven coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 018 | 1.0 | 1 | 0 | 0 | 0 | At the end the lid is not on the jar and no coffee beans are visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | collect_coffee_beans | 019 | 0.0 | 0 | 0 | 0 | 1 | The lid is not on the jar and all coffee beans remain on the table, with none visibly inside the jar. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 000 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are placed inside the basket, while the third (blue bottle) remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 001 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent bottle is visibly placed in the basket while the other two remain on the countertop. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 002 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed in the basket while one remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 003 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed inside the basket, while the blue bottle remains outside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 004 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent item is visibly placed in the basket while the other two remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 005 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 006 | 0.66667 | 0 | 0.333333 | 0 | 1 | Only one detergent bottle is visibly placed in the basket while the other detergent items remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 007 | 1.0 | 1 | 1 | 1 | 1 | All three detergent items are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 008 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only the blue detergent bottle is placed in the basket, while the other detergent items remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 009 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed inside the basket, while the blue bottle remains outside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 010 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed in the basket while the third blue spray bottle remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 011 | 0.0 | 0 | 0.333333 | 0 | 1 | Only one detergent item is visibly placed in the box while the other two remain on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 012 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed inside the basket while the third remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 013 | 0.33333 | 0 | 0.333333 | 0 | 1 | Only one detergent bottle is visibly placed in the basket, while the other two remain outside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 014 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles (blue spray, white spray, and blue OxiClean) are visibly placed inside the basket by the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 015 | 0.0 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed in the basket while one remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 016 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent bottles are visibly placed in the basket while one bottle remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 017 | 1.0 | 1 | 1 | 1 | 1 | All three detergent bottles are visibly placed inside the basket at the end. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 018 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed inside the basket while the third remains outside. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | detergent | 019 | 0.66667 | 0 | 0.666667 | 0 | 1 | Two detergent items are visibly placed in the basket, while the third remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 000 | 0.33333 | 0 | 0 | 0 | 1 | By the end, the glasses are outside the box with temples unfolded and the box open. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 001 | 0.33333 | 0 | 0 | 0 | 1 | At the end the glasses remain outside the box with temples unfolded, and the box is open. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 002 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses are on the table with temples unfolded, while the glasses box is closed and empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 003 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside the box with temples not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 004 | 0.0 | 0 | 0 | 0 | 1 | The box remains open, the glasses are outside the box, and the temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 005 | 0.0 | 0 | 0 | 0 | 1 | The glasses remain outside the box with temples unfolded and the box not visibly closed. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 006 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside with temples not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 007 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside and both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 008 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses appear placed inside the open box, but the box is not closed and both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 009 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses case is closed, but the glasses remain outside the box with temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 010 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses are outside the box with temples not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 011 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses case is closed, but the glasses remain outside on the table with temples unfolded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 012 | 1.0 | 1 | 0.666667 | 0 | 0 | The box is closed with the glasses inside, but both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 013 | 0.33333 | 0 | 0 | 0 | 1 | The glasses remain on the table with temples unfolded and the glasses box open, so none of the conditions are satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 014 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside with temples not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 015 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside with temples not both folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 016 | 0.66667 | 0 | 0 | 0 | 1 | The box remains open, the glasses are not inside the box, and both temples are not visibly folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 017 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside and the temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 018 | 0.33333 | 0 | 0.333333 | 0 | 1 | The glasses box is closed, but the glasses remain outside and their temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | put_glass_in_glassbox | 019 | 0.33333 | 0 | 0.333333 | 0 | 1 | The box lid is closed, but the glasses are not clearly inside and the temples are not folded. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 000 | 1.0 | 1 | 0.5 | 0 | 0 | The wooden spoon is on the holder, but the fork remains off the holder and in the gripper/on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 001 | 0.5 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visibly placed on the holder; the spoon lies on the drying rack and the fork is not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 002 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 003 | 0.5 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is placed on the circular holder; the spoon ends up on the dish rack and the fork remains on the counter. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 004 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is on the holder while the spoon remains on the counter, not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 005 | 0.5 | 0 | 0 | 0 | 1 | At the end, the spoon lies on the drying rack and the fork is in the gripper or on the table, with neither utensil visibly placed in the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 006 | 0.0 | 0 | 0 | 0 | 1 | By the end, neither the spoon nor the fork is on the holder; the holder is visibly empty. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 007 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 008 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visibly placed on the holder; both remain on the table near it. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 009 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork are placed on the holder; both remain on the table. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 010 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the countertop rather than on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 011 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is placed on the circular holder, while the fork remains on the table off the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 012 | 0.0 | 0 | 0 | 0 | 1 | Both the spoon and the fork remain on the table and are not placed on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 013 | 0.5 | 0 | 0 | 0 | 1 | The spoon rests on the drying rack tray and the fork remains on the countertop, not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 014 | 0.0 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visibly placed on the holder; both remain on the countertop. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 015 | 0.0 | 0 | 0 | 0 | 1 | The required final state is not visibly satisfied. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 016 | 0.5 | 0 | 0.5 | 0 | 1 | The fork is on the round holder while the spoon rests on the drying rack, not on the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 017 | 0.5 | 0 | 0.5 | 0 | 1 | The spoon is on the holder while the fork remains on the countertop. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 018 | 0.5 | 0 | 0 | 0 | 1 | Neither the spoon nor the fork is visibly on the holder at the end; the spoon rests on the drying rack and the fork remains off the holder. | 50 | 50 | 50 | synced_camera_composite |
| gpt-5 | utensils_to_holder | 019 | 0.0 | 0 | 0.5 | 0 | 1 | The spoon is visibly placed on the holder while the fork remains off the holder. | 50 | 50 | 50 | synced_camera_composite |

## Mismatches

- apple_to_fruit_bowl/006: sim_success=1, vlm_success=0, vlm_score=0.0
- apple_to_fruit_bowl/002: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/002: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/004: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/005: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/007: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/011: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/013: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/017: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/019: sim_success=1, vlm_success=0, vlm_score=0.0
- detergent/001: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- detergent/014: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/002: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/011: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/012: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/013: sim_success=1, vlm_success=0, vlm_score=0.3333333333
- put_glass_in_glassbox/016: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- put_glass_in_glassbox/018: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- bookmark_on_book/000: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/001: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/003: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/005: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/007: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/009: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/011: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/013: sim_success=1, vlm_success=0, vlm_score=0.0
- bookmark_on_book/017: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/016: sim_success=1, vlm_success=0, vlm_score=0.0
- collect_coffee_beans/017: sim_success=1, vlm_success=0, vlm_score=0.5
- collect_coffee_beans/018: sim_success=1, vlm_success=0, vlm_score=0.0
- put_glass_in_glassbox/012: sim_success=1, vlm_success=0, vlm_score=0.6666666667
- utensils_to_holder/000: sim_success=1, vlm_success=0, vlm_score=0.5
