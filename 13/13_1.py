file_input = open("input1213.txt", "r")
file_input = open("test_input.txt", "r")
lines = file_input.readlines()

counter = 0

# LIST METHODS
# append(this), count(of_this)
# extend(iterable_to_append)
# index(of_first_this), insert(at_pos)
# pop() default: idx -1
# remove(first_of_this), reverse(), sort()

# DICT METHODS
# assignment: a_dict[key] = value
# get(key), keys() returns list, values() returns list
# pop(key_to_delete), returns deleted value

# STRING METHODS
# str.strip() returns (DOESN'T MODIFY) str with leading/trailing whitespace removed
# str.count("x", start=0) returns the number of times "x" appears in str
# str.find("pat") returns the index of the first occurrence of the specified pattern
# str.startswith(), str.endswith() returns Bool
# str.split("c") returns list of strings split by separator (default: any whitespace)

timestamp = int(lines[0].strip())
bus_list = lines[1].strip().split(',')



buses = []
for b in bus_list:
	if b != 'x':
		buses.append(int(b))

def do_it(timestamp, buses):
	lowest = -1
	the_bus = -1
	rem = -1
	for bus in buses:
		modulo = timestamp % bus
		waiting = bus - modulo
		if waiting < lowest or lowest == -1:
			lowest = waiting
			the_bus = bus
	print(f'answer {lowest * the_bus}')

do_it(timestamp, buses)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

Modulo arithmetic?

Wait time is... distance from timestamp % bus to...

'''