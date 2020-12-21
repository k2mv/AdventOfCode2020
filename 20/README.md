# 20

Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa &#x1F62D;

**Part 1** was a matter of matching every tile side against every other tile side and flagging the four tiles that only had two sides that matched any other tile side.  So you didn't even really have to assemble the picture at all (and I didn't).

**Part 2** was kind of a fevered blur of scribbling rotations and reflections and reversed strings in a notepad and trying to string them together on the computer screen.

I ended up in a big rut around 6pm, because I had successfully assembled an image of the right size, and I was able to find several sea monsters, but the resulting final answer wasn't accepted by the entry form.

I eventually broke down and looked at the subreddit for photos of what the sea monster image actually looked like:

https://www.reddit.com/r/adventofcode/comments/kgo01p/2020_day_20_solutions/

*(As far as I can tell, the actual numerical solutions aren't posted there)*

That led me to look back at the source tiles that I had arranged (the waffle-like grid at the beginning of the output of `20_2.py`) and finally noticed that, while all the tiles were in their correct places, a significant portion of them appeared to be flipped horizontally from their correct orientation.

I tracked the error down to a *single line* in my rotation code in `rotate_and_flip_grid()` (it's commented out now) that was adding an unnecessary flip to certain tiles during the process of stitching together all the tiles into a master image.

The erroneously flipped tiles had corrupted about half of the sea monsters, but the other half survived.  That's what led me to believe initially that I had come upon a correct map when I actually hadn't.  (For a bit of fun, uncomment that line in `rotate_and_flip_grid()` and watch half of the sea monsters magically disappear.  &#x1F605;)

I feel a little guilty for peeking before I had the final answer, but I wouldn't have been able to benefit from peeking if the other 99% of my code wasn't already working.  Whatever lets you sleep at night, I suppose.  &#x1F937;