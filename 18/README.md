# 18

This was kind of a ride; it was pretty clear what needed to happen, and maybe 80% of it was simple to translate into code, but the parentheses provided most of the difficulty in getting the specific sequence of actions right to nest and de-nest the state of the equation correctly in all situations.

Tracing my code and the state of `left`, `operator`, and `right` to debug the operation of the right-parentheses handler `for _ in range(right_paren_count):` (which is where about half of my effort was spent in **Part 2**) reminded me of the feeling of going through assembly code with colored pens to figure out what was going on in the registers.

Notes to self:
* Check the problem and the input carefully before writing out an entire skeleton solution; I didn't realize until finishing **Part 1** that I didn't need to handle subtraction or division.