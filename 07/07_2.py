file_input = open("input1207.txt", "r")
lines = file_input.readlines()

counter = 0 

a_list = []
# append(this), count(of_this)
# extend(iterable_to_append)
# index(of_first_this), insert(at_pos)
# pop() default: idx -1
# remove(first_of_this), reverse(), sort()

a_dict = {}
b_dict = {}
# assignment: a_dict[key] = value
# get(key), keys() returns list, values() returns list
# pop(key_to_delete), returns deleted value

def recursive_dive(a_dict, current_bag_type, target_bag_type):
	#print(f'recursive_dive({current_bag_type})')
	ret = False
	if current_bag_type == target_bag_type:
		return True
	else:
		for bag_entry in a_dict[current_bag_type]:
			ret = ret or recursive_dive(a_dict, bag_entry[1], target_bag_type)
	return ret

def recursive_dive_2(a_dict, current_bag_type):
	if a_dict[current_bag_type] == []:
		return 1
	else:
		ret = 0
		for bag_entry in a_dict[current_bag_type]:
			ret += bag_entry[0] * recursive_dive_2(a_dict, bag_entry[1])
		return 1 + ret


for line in lines:
	wd = line.split()
	bag_primary = (wd[0], wd[1])
	bag_ref = []
	if wd[4] != 'no':
		idx = 4
		has_next = True
		while has_next:
			bag_ref.append((int(wd[idx]), (wd[idx+1], wd[idx+2])))
			# add tuple (1, ('light', 'red')) to list bag_ref
			if wd[idx+3].endswith(','):
				idx += 4
			else:
				has_next = False
	a_dict[bag_primary] = bag_ref
	pass # end
#print(a_dict)

target_bag_type = ('shiny','gold')

counter = recursive_dive_2(a_dict, target_bag_type)
counter -= 1 # not counting the bag everything else 'is inside'
print(counter)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

idea:
FIRST PASS read in "ADJ COL" of each line to create indexes of a dict
then can search the dict for each ADJ COL following to create linkages




'''