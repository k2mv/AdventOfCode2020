import re

file_input = open("input1206.txt", "r")
lines = file_input.readlines()

counter = 0 # ACCUMULATOR
line_count = 0
total = 0
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

def func(): # put the important thing here and test it on input first?
	pass # end

for line in lines:
	if line == '\n':
		#print('break')
		#total = len(a_dict.keys())
		#print('break ' + str(total))
		#counter += total
		for letter in a_dict.keys():
			if a_dict[letter] == line_count:
				total += 1
		counter += total
		a_dict = {}
		line_count = 0
		total = 0
		pass
	else:
		#print(line)
		line_count += 1
		for ch in line:
			if ch.isalnum():
				#a_dict[ch] = "butt"
				if ch not in a_dict.keys():
					a_dict[ch] = 1
				else:
					temp = a_dict[ch]
					a_dict[ch] = temp + 1
		pass
	pass # end
# one more verify after the last line
#total = len(a_dict.keys())
#print('break ' + str(total))
for letter in a_dict.keys():
	if a_dict[letter] == line_count:
		total += 1
counter += total
print(counter)

file_input.close()

'''
SCRATCH PAD RIGHT HERE



'''