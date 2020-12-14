file_input = open("input1214.txt", "r")
#file_input = open("test_input2.txt", "r")
lines = file_input.readlines()

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

def process_input(lines):
    ret = []
    for l in lines:
        asdf = l.split()
        a = asdf[0]
        if a.startswith('mem'):
            # parse out mem address
            address = int( a[4:-1] )
            value = int( asdf[2] )
            ret.append(('mem', address, value))
        elif a.startswith('mask'):
            ret.append(('mask', asdf[2]))
    return ret

def set_mask(mask_text):
    x_list = []
    ones_mask = 0
    for n in range(len(mask_text)):
        if mask_text[n] == '0':
            pass
        elif mask_text[n] == '1':
            ones_mask |= 2 **(35-n)
        elif mask_text[n] == 'X':
            x_list.append(2 ** (35-n))
    return ones_mask, x_list

def do_it(inp):
    ones_mask = 0
    zeroes_mask = 2 ** 36 - 1
    x_list = []
    memory = {}
    for i in inp:
        if i[0] == 'mem':
            print(x_list)
            print(f'mem[{i[1]}] = {i[2]}')
            base_address = i[1]
            value = i[2]
            temp_mask = ones_mask
            
            x_mask_max = 2**len(x_list)
            for x_mask in range(x_mask_max):
                temp_mask = ones_mask
                zeroes_mask = 2 ** 36 - 1
                for idx in range(len(x_list)):
                    if x_mask & 2**idx > 0:
                        temp_mask |= x_list[idx]
                    else:
                        zeroes_mask &= (2 ** 36 - 1) - x_list[idx]
                memory_addr = (base_address | temp_mask) & zeroes_mask
                memory[memory_addr] = value
                print(f'memory[{memory_addr}] = {value}')

        elif i[0] == 'mask':
            ones_mask, x_list = set_mask(i[1])



    accum = 0
    for k in memory.keys():
        accum += memory[k]
    print(accum)

inp = process_input(lines)
do_it(inp)

#print(process_input(lines))
#print(2 ** 36 - 1)


file_input.close()

'''
SCRATCH PAD RIGHT HERE

36 bit working space

Bitmasking in this fashion with normal bitwise operators:
1. Bitwise | with the 1s in place and 0s otherwise
2. Bitwise & with the 0s in place and 1s otherwise

So need one-or-mask and zero-and-mask kept

PART 2

Now the mask uses 0/1 as part of a regular OR mask
but how do we handle Floating

Store the straight mask, 0s and 1s portion, as 0s and 1s in an initial-all-zero mask
then create a list of positions of Xes
When writing to memory,
iterate through ORing every possible combination of the X positions with 1s in the OR mask



'''