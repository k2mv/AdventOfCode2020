file_input = open("input1210.txt", "r")
lines = file_input.readlines()

counter = 0 

a_list = []
b_list = []
# append(this), count(of_this)
# extend(iterable_to_append)
# index(of_first_this), insert(at_pos)
# pop() default: idx -1
# remove(first_of_this), reverse(), sort()

a_dict = {}
# assignment: a_dict[key] = value
# get(key), keys() returns list, values() returns list
# pop(key_to_delete), returns deleted value

def process_input(lines):
	a_list = []
	for line in lines:
		a_list.append(int(line.strip()))
	a_list.sort()
	return a_list

def construct(a_list, idx, valid_lists):
	print(f'construct idx = {idx}')
	if idx >= len(a_list): # nothing left to add
		return valid_lists
	else:
		v_copy = valid_lists.copy()
		for v in valid_lists:
			v.append(a_list[idx]) # guaranteed ok
		for v in v_copy:
			v.pop()
			v.append(a_list[idx])
			if validate_list(v):
				valid_lists.append(v)
	return construct(a_list, idx+1, valid_lists)

def construct2(a_list):
	valid_lists = [[0,a_list[0]]]
	temp_lists = []
	for n in range(1,len(a_list)):
		print(f'for n = {n}')
		num = a_list[n]
		for v in valid_lists:
			v.append(num)
		temp_lists = valid_lists.copy()
		for t in temp_lists:
			t.pop(-2)
			if validate_list(t):
				valid_lists.append(t)	
	return valid_lists
	
def construct3(a_list):
	valid_lists = [[0,a_list[0]]]
	for n in range(1,len(a_list)):
		temp_lists = []
		print(f'for n = {n}')
		num = a_list[n]
		for v in valid_lists:
			temp_lists.append([v[1],num])
			if num - v[0] <= 3:
				temp_lists.append([v[0],num])
		valid_lists = temp_lists
	return valid_lists


def construct4(a_list):
	three_behind = 0
	two_behind = 0
	one_behind = 0
	a = a_list[0]
	if a == 1:
		one_behind = 1
	elif a == 2:
		two_behind = 1
	elif a == 3:
		three_behind = 1
	for n in range(1, len(a_list)):
		diff = a_list[n] - a_list[n-1]
		if diff == 1:
			new_three = two_behind
			new_two = one_behind
			new_one = one_behind + two_behind + three_behind
			three_behind = new_three
			two_behind = new_two
			one_behind = new_one
		elif diff == 2:
			new_three = one_behind
			new_two = two_behind + three_behind + one_behind
			new_one = 0
			three_behind = new_three
			two_behind = new_two
			one_behind = new_one
		elif diff == 3:
			new_three = three_behind + two_behind + one_behind
			new_two = 0
			new_one = 0
			three_behind = new_three
			two_behind = new_two
			one_behind = new_one
	print(f'Total arrangements: {three_behind+two_behind+one_behind}')

def validate_list(a_list):
	
	ret = False
	if a_list[-1] - a_list[-2] <= 3:
		ret = True
	#print(f'validate_list: {ret}')
	return ret


a_list = process_input(lines)
b_list = [[0,a_list[0]]]

c_list = construct4(a_list)
#print(len(c_list))

file_input.close()

'''
SCRATCH PAD RIGHT HERE

diff from 0 to first adapter = first adapter
diff from last adapter to device = always 3

Part 2: how do we know how many intervals are skippable?
We have optional deletions
Distance from previous and next values?

a 1 b 1 c  b can be removed
a 1 b 2 c  b can be removed
a 1 b 3 c  b required
a 2 b 1 c  b can be removed
a 2 b 2 c  b required
a 2 b 3 c  b required
a 3 b 1 c  b required
a 3 b 2 c  b required
a 3 b 3 c  b required

For runs of four:
Gap runs of 1-1-1: can remove either or both
1-2-1: can remove one but not the other
1-1-1-1: can remove any one, any two, or all three
2-1-2: can remove one but not the other

Is there any way to use the 1-gap and 3-gap data to find the answer to Part 2?

Is there any way to tell how many ways a given number can contribute to the number of answers by
checking the distance to and from previous/following entries?

Keep all the 'required' ones and iterate through combinations of the rest?

Runs of 1-1 sequences seem to add 2 

How many times can each number be skipped over?

Are 'twos' involved at all?

If there's a 3 on either side, the number can't be removed

Adding differences looking back and forward?  Sums of differences?

How can I let the computer do the hard part?

Possible answer: Starting at 0, add an 'arrangement' for every entry after the 'next' one that can be skipped to from this entry
if a_list[n+2] - this <= 3 then add 1
if a_list...

Count of number of times each number can be skipped by a previous number? Squares?

Is there a simpler answer or is there a point where you need to brute force after reaching a certain point?

Does this require combinatorics?

Is this something that can be counted with some kind of accumulator?  Multiple accumulators?
How would you multiply/add them together?

Just iterate through a 101-bit number in binary and verify ?

Are we assessing islands of 'combinability' and then multiplying them against each other to represent their independence?

Islands terminated by anything other than a consecutive 1-1 or 1-2 or 2-1

Can't seem to calculate that cleanly with an arbitrary number of 1-1 in an island itself

Referring to table of possible arrangements at subset of length n-1?
Do you add or multiply?  Both?
Adding one more value to the window doesn't seem to give a clear recursive mathematical progression
When you add a value to the end it seems to multiply the remaining combinations by some large factor
because previous skipped numbers can be skipped independently

10:58 Realized now that specifically a 1-gap followed by a 1-gap doubles the number of combinations
Hypothesis: 1-1 gap = x2 + 1 combinations; 1-2 or 2-1 gap = +1 combination
Doesn't seem to work on the small example

Judging sequences of gaps between numbers appears to be a dead end

Do we need to check a larger window (2 before, 2 after)?  How do you account for the results of
previous steps while also allowing for independent combinations of parts of previous steps?

Every step includes all the valid exclusion patterns from the previous step and only adds more
- and then adds additional exclusion patterns unlocked by the next step
- but also is multiplied by all the exclusion patterns from previous steps that can be stacked
  on top of any of the newly unlocked exclusion patterns
- except when the new pattern can 'merge' with a pattern sitting at the end, after which
  the number of resulting patterns is hard to determine

Divide and conquer?  Split in half and combine coming back up the tree?

12:04 At each step, compare each valid answer from the previous step with "with the penultimate number"
and "without the penultimate number" and see if each respects the principle; add it to the
list of lists if it does

12:11 If you have a sequence with a known number of combos, you automatically carry over the same
number of combos with the next number added because it's guaranteed to be a valid sequence
So you only have to check all the previous lists with the penultimate number missing (given that
the penultimate number was locked in last time and the new number is locked in this time)
- add new number to end (guaranteed to work)
- read in each resulting sequence, delete penultimate number, test if gap between last two numbers
  is greater than 3
- reject if not, add to list of lists if valid
Do we need to reach back two steps?  Quick paper test seems to say no

18:01 Straight recursive approach too slow to complete in a reasonable amount of time
Need to try a looping approach instead of straight recursion

18:18 Initial looping approach runs overlong in the high 20s again
Need to figure out how to minimize memory operations, or decrease complexity by discarding
whatever parts are unnecessary to cut down on processing time

18:26 Only need the last layer of calculation - 

18:39 Still not reducing complexity enough to progress beyond the high 20s, trying again
- Probably need to avoid storing the lists themselves and keep a separate counter?
- Gap between the three crucial components (last two plus new) can only be one of a few
arrangements - keep a table of how many entries exist with those gaps and process that way,
keeping track only of the last number in order to assess distance from...
- The last number is always present in every entry that survives the step, so we're tallying:

[n-3, n] never survives the next round
[n-2, n] survives next round as [n-3, n] when next number is n+1
[n-1, n] survives next round as [n-3, n] when next n+2, as [n-2, n] when next n+1

So for each round
if next is n+3: no new lists created, all current lists converted to [n-3, n]
if next is n+2:
	[n-3, n] total: moved to [n-2, n] total
	[n-2, n] total: no operation
	[n-1, n] total: moved to [n-3, n] and also added to [n-2, n] total
	new [n-3, n]: [n-1, n] total
	new [n-2, n]: existing [n-2, n] total + [n-3, n] total + [n-1, n] total
	new [n-1, n]: 0
if next is n+1:
	[n-3, n] total: moved to [n-1, n] total
	[n-2, n] total: move to both [n-3, n] and [n-1, n]
	[n-1, n] total: keep and also add to [n-2, n] total
	new [n-3, n]: [n-2, n] total
	new [n-2, n]: [n-1, n] total
	new [n-1, n]: existing [n-1, n] total + [n-2, n] total + [n-3, n] total
'''