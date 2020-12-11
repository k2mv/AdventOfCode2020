file_input = open("input1211.txt", "r")
#file_input = open("test_input.txt", "r")
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

def iterate(lines):
	ret_lines = []
	#occupied_count = 0
	changed = False
	total_changed = 0
	total_occupied = 0
	for row in range(len(lines)):
		row_to_add = ""
		for col in range(len(lines[0])):
			asdf = process(lines, row, col)
			#row_to_add.append(asdf[0])
			row_to_add += asdf[0]
			if asdf[0] == '#':
				total_occupied += 1
			if asdf[1]:
				total_changed += 1
		ret_lines.append(row_to_add)
			
	return (ret_lines, total_occupied, total_changed)

def process(lines, row, col):
	max_row = len(lines) - 1
	max_col = len(lines[0]) - 1
	if  lines[row][col] == '\n':
		return ('\n', False)
	this_char = lines[row][col]
	#print(f'max_row = {max_row}, max_col = {max_col}')
	adj_count = 0
	result = '.'
	changed = False
	#print(f'row = {row}, col = {col}, len_row = {len(lines[row])}')
	if row > 0:
		if col > 0 and lines[row-1][col-1] == '#':
			adj_count += 1
		if lines[row-1][col] == '#':
			adj_count += 1
		if col < max_col and lines[row-1][col+1] == '#':
			adj_count += 1

	if col > 0 and lines[row][col-1] == '#':
		adj_count += 1
	if col < max_col  and lines[row][col+1] == '#':
		adj_count += 1

	if row < max_row:
		if col > 0 and lines[row+1][col-1] == '#':
			adj_count += 1
		if lines[row+1][col] == '#':
			adj_count += 1 # NEEDS FIXING?
		if col < max_col  and lines[row+1][col+1] == '#':
			adj_count += 1
	if this_char == 'L':
		if adj_count == 0:
			result = '#'
			changed = True
		else:
			result = 'L'
			changed = False
	elif this_char == '#':
		if adj_count >= 4:
			result = 'L'
			changed = True
		else:
			result = '#'
			changed = False
	return (result, changed)



#line_len = len(lines[0])
#lines = iterate(lines)
for n in range(len(lines)):
	lines[n] = lines[n].strip()

print(len(lines[0]))
#for n in range(len(lines[0])-1):
#	print(process(lines, 0, n))
#print(len(lines))
#print(len(lines[0]))


#iterate() returns tuple (lines, total_changed)
lines_in = (lines, 0, -1)
while lines_in[2] != 0:
	lines_in = iterate(lines_in[0])
#lines_in = iterate(lines_in[0])

#lines = iterate(lines)
for l in lines_in[0]:
	print(l)
print(f'total_occupied = {lines_in[1]}, total_changed = {lines_in[2]}')


file_input.close()

'''
SCRATCH PAD RIGHT HERE

Rule 1: if L and no L adjacent, convert to #
Rule 2: if # and 4 or more adjacent #, then convert to L
Rule 3: . doesn't change

Keep a buffer of 2? lines before writing results to the original array
so that you don't interfere with the calculations

13:09 Running into mysterious string index out of range near the end but I can't find any
place where the index is out of bounds when I check

91 lines (indexed 0-90)
96 columns (indexed 0-95)

'''
