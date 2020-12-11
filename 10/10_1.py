file_input = open("input1210.txt", "r")
lines = file_input.readlines()

counter = 0 

a_list = []
# append(this), count(of_this)
# extend(iterable_to_append)
# index(of_first_this), insert(at_pos)
# pop() default: idx -1
# remove(first_of_this), reverse(), sort()

a_dict = {}
# assignment: a_dict[key] = value
# get(key), keys() returns list, values() returns list
# pop(key_to_delete), returns deleted value

def asdf(lines):
	a_list = []
	for line in lines:
		a_list.append(int(line.strip()))
	#print(a_list)
	a_list.sort()
	#print(a_list)
	ones = 0
	threes = 0
	current_joltage = 0
	for n in range(len(a_list)):
		diff = a_list[n] - current_joltage
		if diff == 1:
			ones += 1
		elif diff == 3:
			threes += 1
		current_joltage = a_list[n]
	threes += 1
	print(f'Ones: {ones} Threes: {threes} Product: {ones * threes}')



asdf(lines)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

diff from 0 to first adapter = first adapter
diff from last adapter to device = always 3

'''