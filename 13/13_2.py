file_input = open("input1213.txt", "r")
#file_input = open("test_input.txt", "r")
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
for n in  range(len(bus_list)):
	if bus_list[n] != 'x':
		buses.append((int(bus_list[n]), n))

print(buses)

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

def do_it2(buses):
	mult = 0
	done = False
	de_base = buses[0][0]
	while not done:
		mult += 1
		base = de_base * mult
		flag = True
		for n in range(1, len(buses)):
			a = buses[n][0]
			b = buses[n][1]
			if a - (base % a) != b:
				flag = False
		if flag:
			done = True
			print(base)


def do_it3(base_magnitude, next_bus, next_bus_offset):
	base = base_magnitude[0]
	magnitude = base_magnitude[1]
	done = False
	mult = 0
	while not done:
		modulo = base % next_bus
		waiting = next_bus - modulo
		if waiting == next_bus_offset:
			done = True
			magnitude *= next_bus
		else:
			base += magnitude
	return (base, magnitude)

def do_it3a(original_base, base_magnitude, next_bus, next_bus_offset):
	base = base_magnitude[0]
	magnitude = base_magnitude[1]
	done = False
	mult = 0
	while not done:
		modulo = (base + next_bus_offset) % next_bus
		#waiting = next_bus - modulo
		if modulo == 0:
			done = True
			magnitude *= next_bus
		else:
			base += magnitude
	print(f'base {base}, magnitude {magnitude}')
	return (base, magnitude)

def do_it4(buses):
	product = 1
	for b in buses:
		product *= b[0]
	print(product)
	for n in range(1,product):
		n = product - n
		gottem = True
		for b in buses:
			bus_num = b[0]
			offset = b[1]
			check = (n+offset) % bus_num
			gottem = gottem and check == 0
		if gottem:
			print(f'Answer {n}')


#do_it4(buses)

original_base = buses[0][0]
base_magnitude = (buses[0][0], buses[0][0])
for n in range(1, len(buses)):
	#print(f'calling base_magnitude with {base_magnitude[0]}, {base_magnitude[1]}')
	base_magnitude = do_it3a(original_base, base_magnitude, buses[n][0], buses[n][1])

#print(base_magnitude[0], base_magnitude[1])
print(base_magnitude)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

Modulo arithmetic?

Wait time is... distance from timestamp % bus to...

part 2: ok something's going on here
the current code will work on a small data set but it runs forever on the big set

what can be done differently...

Find iterator that generates first two in the correct offset, then only run that 

How do you find the frequency(?) of two numbers appearing at a given offset?

SOLUTION:
Product of a and b is the magnitude of the offset
Find the first place where they line up correctly and that is your new base
inputs are 'base' and 'magnitude', 'bus2', 'bus2offset'
start with base 'bus' and magnitude 'bus' against 'bus2' with offset 'bus2offset'
start jumping 1 magnitude at a time and checking if wait time == offset
waiting = bus2 - modulo
modulo = base % bus2
once you find a match (waiting == offset) then 

next is?
multiply MAGNITUDE by bus2
base stays the same
so call it again with base the same, magnitude = magnitude * bus2, bus2, bus3offset

ok so that 1) seems to work inconsistently and 2) doesn't solve the running-forever problem


Wait can you just multiply all of them together up front?  We know that will be the final magnitude right
but we won't know where inside that big-ass number the base should be right?

Start at that number and work your way down?  Assuming that the convergence must be somewhere within that range
Wouldn't that... just do the same thing though?

TRICKY: You can't do straight on mods because some buses come more frequently than their offset
You sneaky devils

01:50 Still no luck - the product trick wasn't able to narrow anything down (the product is just too high)
So is there any other way to reduce the number of numbers we check?

Maybe do like
7/13
7/59
7/31
7/19?

I'm definitely sure the correct base is within the range of the product of all the numbers
and we know it is a multiple of the first bus

These are all probably prime numbers?



'''