file_input = open("input1209.txt", "r")
lines = file_input.readlines()

counter = 0 

target = 552655238

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

def width_search(num_list, target, search_width):
	ret = None
	for n in range(len(lines)-search_width):
		accum = 0
		for p in range(search_width):
			accum += num_list[n+p]
		if accum == target:
			print(f'search width {search_width}, base {n}')
			ret = num_list[n] + num_list[n+search_width-1]
	return ret

def generate_num_list(lines):
	num_list = []
	for line in lines:
		x = line.split()
		num_list.append(int(x[0]))
	#print(f'num_list length {len(num_list)}')
	return num_list

print(len(lines))

num_list = generate_num_list(lines)
'''
print(len(num_list))
for n in range(len(lines)-25):
	sum_list = generate_valid_sums(num_list, n)
	if num_list[n+25] not in sum_list:
		print(f'Not found: {num_list[n+25]}')
'''
'''
for n in range(2,len(num_list)):
	ret = 0
	ret = width_search(num_list, target, n)
	if ret != None:
		print(ret)

'''

print(num_list[500]+num_list[516])

k=[]
for n in range (500, 517):
	k.append(num_list[n])
k.sort()
print(k[0] + k[16])
file_input.close()

'''
SCRATCH PAD RIGHT HERE

sliding window
list of sums

'''