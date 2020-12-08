file_input = open("input1208.txt", "r")
lines = file_input.readlines()

accum = 0 
curr_line = 0
answer = ('none', 'none')

a_list = []
# append(this), count(of_this)
# extend(iterable_to_append)
# index(of_first_this), insert(at_pos)
# pop() default: idx -1
# remove(first_of_this), reverse(), sort()

def have_i_been_here_before(line_list, curr_line): # put the important thing here and test it on input first?
	if curr_line in line_list:
		return True # i.e. halt
	return False

def run_program(lines):
	a_list = []
	accum = 0
	curr_line = 0
	halt = False
	eof_reached = False
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
		if curr_line == len(lines):
			halt = True
			eof_reached = True
			#print('End of file reached')
		pass #end while !halt
	return (eof_reached, accum)

for n in range(len(lines)):
	run_it = True
	lines_to_run = lines.copy()
	if lines[n].startswith('jmp'):
		lines_to_run[n] = 'nop' + lines_to_run[n][3:]
	elif lines[n].startswith('nop'):
		lines_to_run[n] = 'jmp' + lines_to_run[n][3:]
	elif lines[n].startswith('acc'):
		run_it = False
	if run_it:
		answer = run_program(lines_to_run)
		if answer[0]:
			print(answer[1])
	



file_input.close()

'''
SCRATCH PAD RIGHT HERE

Must keep track of each index (line number) visited

Part 2: Flip one jmp/nop at a time in the program and run it until it halts at EOF

'''