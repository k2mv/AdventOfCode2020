file_input = open("input1208.txt", "r")
lines = file_input.readlines()

accum = 0 
curr_line = 0
halt = False

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

def have_i_been_here_before(line_list, curr_line): # put the important thing here and test it on input first?
	if curr_line in line_list:
		return True # i.e. halt
	return False

while not halt:
	a_list.append(curr_line)
	i = lines[curr_line].split()
	oper, number = i[0], int(i[1])
	if oper == 'nop':
		curr_line += 1
	elif oper == 'acc':
		accum += number
		curr_line += 1
	elif oper == 'jmp':
		curr_line += int(number)
	# at this point curr_line represents the NEXT line to run
	halt = have_i_been_here_before(a_list, curr_line)
	# i.e. has the new destination line been run before, if so then quit now
	pass #end while !halt

print(accum)
file_input.close()

'''
SCRATCH PAD RIGHT HERE

Must keep track of each index (line number) visited

'''