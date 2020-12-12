file_input = open("input1212.txt", "r")
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

def process_lines(lines):
	ret = []
	for n in range(len(lines)):
		lines[n] = lines[n].strip()
		ret.append((lines[n][0], int(lines[n][1:])))

	# then: split, convert, etc if needed
	return ret

def turn(facing, dir, deg):
	turns = deg / 90
	pos = None
	if facing == (1,0): # E
		pos = 0
	elif facing == (0,1): # N
		pos = 1
	elif facing == (-1,0): # W
		pos = 2
	elif facing == (0,-1): # S
		pos = 3
	if dir == 'L':
		pos = (pos + turns) % 4
	elif dir == 'R':
		pos = (pos - turns) % 4
	if pos == 0:
		facing = (1,0)
	elif pos == 1:
		facing = (0,1)
	elif pos == 2:
		facing = (-1,0)
	elif pos == 3:
		facing = (0,-1)
	return facing

def turn2(waypoint, dir, deg):
	turns = deg / 90
	base = 0
	x, y = waypoint[0], waypoint[1]

	if dir == 'L':
		base = (base + turns) % 4
	elif dir == 'R':
		base = (base - turns) % 4
	if base == 0:
		return waypoint
	elif base == 1:
		return (-y, x)
	elif base == 2:
		return (-x, -y)
	elif base == 3:
		return (y, -x)

def move(pos, dir, dist):
	a = pos[0] + dir[0] * dist
	b = pos[1] + dir[1] * dist
	return (a,b)

instr = process_lines(lines)
#print(process_lines(lines))

# coords (east, north) (X,Y)
pos = (0,0)
waypoint = (10,1)

for i in instr:
	dist = i[1]
	if i[0] == 'L' or i[0] == 'R':
		waypoint = turn2(waypoint, i[0], dist)
	else:
		if i[0] == 'F':
			pos = move(pos, waypoint, dist)
		elif i[0] == 'E':
			waypoint = move(waypoint, (1,0), dist)
		elif i[0] == 'N':
			waypoint = move(waypoint, (0,1), dist)
		elif i[0] == 'W':
			waypoint = move(waypoint, (-1,0), dist)
		elif i[0] == 'S':
			waypoint = move(waypoint, (0,-1), dist)
	print(f'EAST {pos[0]}, NORTH {pos[1]}, DISTANCE {abs(pos[0])+abs(pos[1])}')

print (abs(pos[0]) + abs(pos[1]))


file_input.close()

'''
SCRATCH PAD RIGHT HERE

The ship starts by facing east. 

'''