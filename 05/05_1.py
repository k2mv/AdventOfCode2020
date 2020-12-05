import re

file_input = open("input1205.txt", "r")
lines = file_input.readlines()

counter = 0 # THE MAX
a_list = []
a_dict = {}

for line in lines:
	pass
	# split_line = line.split()
	# for things in split_line:
	score = 0;
	fb = line[:7]
	rl = line[7:]
	#print(f'{fb} {rl}')

	for chidx in (0,1,2,3,4,5,6,7,8,9):
		if line[chidx] in ('R','B'):
			place = 2 ** (9 - chidx)
			score += place

	print(score)
	if score > counter:
		counter = score

	# END for line in lines:

print(counter)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

so it's binary
FB: 0x 000 0000
where F is 0 and 1 is B

RL: R is 1 and L is 0

FBFBBFFRLR = 0x 010 1100, 0x 101


'''