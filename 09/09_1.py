file_input = open("input1209.txt", "r")
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

def generate_valid_sums(num_list, starting_index): # put the important thing here and test it on input first?
	valid_adder_list = []
	valid_sum_list = []
	valid_range = range(starting_index, starting_index+25)
	for n in valid_range:
		valid_adder_list.append(num_list[n])
	for v in range(25):
		for w in range(25):
			if v != w:
				valid_sum_list.append(valid_adder_list[v] + valid_adder_list[w])
	return valid_sum_list

def func2():

	return None

def generate_num_list(lines):
	num_list = []
	for line in lines:
		x = line.split()
		num_list.append(int(x[0]))
	print(f'num_list length {len(num_list)}')
	return num_list

print(len(lines))

num_list = generate_num_list(lines)

print(len(num_list))
for n in range(len(lines)-25):
	sum_list = generate_valid_sums(num_list, n)
	if num_list[n+25] not in sum_list:
		print(f'Not found: {num_list[n+25]}')


file_input.close()

'''
SCRATCH PAD RIGHT HERE

sliding window
list of sums

'''