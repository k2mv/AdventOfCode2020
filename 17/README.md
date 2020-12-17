# 17

This will take a while to clean up.

I noticed some symmetry in the results, so I decided to only track "half-ish" (for **Part 1**) or "a quarter-ish" (for **Part 2**) of the data, and simulate reading the 'invisible neighbors' at the edges and 'double/quadruple counting' each cell depending on position.

In **Part 2** lost track of neighbor-counting in the third dimension in `eval_flat_27()`, and that put me in a world of hurt until I caught it and threw in the `if p == -1` section in the second half as a band-aid.