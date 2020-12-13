# 13

&#x1F62C; *Hopefully you got a solution to this problem before peeking at this folder!* &#x1F62C;

Like most of you, I spent most of my time trying to figure out how to avoid setting my computer on fire.  It is possible! &#x1F62E;

I've created a special slimmed-down and cleaned-up version of my **Part 2** at `13_2_clean.py` so that you can see exactly how the final answer was reached.

How I arrived at my solution: (&#x1F6A8; _spoiler alert_ &#x1F6A8;)

For two prime numbers (these are all prime numbers in the examples/puzzle input) with no offset, they will line up for the first time at the product of the two numbers. 
* Buses 2 and 3 will first line up at time 6.  (Let's call it a "correct base point" when everything lines up.)

Those two numbers will keep lining up at intervals at the product of those two numbers. 
* Buses 2 and 3 will line up at 6, 12, 18...

When you put an offset on one of the numbers, the initial correct base point will move - but the next correct base point will still be the same distance away.
* If you want bus 3 to show up with an offset of 1 after bus 2, your first correct base point is now 2 (because 2 + 1 = 3).
* _(Note that when you add an offset, the initial correct base point can move backward!  &#x1F914;  Think about why.)_
* After 2, however, your next correct base point is 8 (8 + 1 = 9), and the next is 14 (14 + 1 = 15)...
* Your base points remain 6 apart (i.e. bus 2 times bus 3).

This means that if you want to start searching for a correct base point with your third bus after finding one with your first two buses:
* you can start searching at the correct base point you found earlier (since you won't be able to line up three buses anytime before the first two buses line up for the first time), and
* you can step forward in intervals of the product of the first two buses.

Keep doing that, and the steps will soon get *thicc* enough that the calculation will finish by Christmas.
