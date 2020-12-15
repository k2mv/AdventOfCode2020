#file_input = open("input1215.txt", "r")
#file_input = open("test_input.txt", "r")
#lines = file_input.readlines()

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
        pass
    return ret

def do_it(inp, target):
    history = {}
    last = -1
    n = 0 # 1-index this sequence
    for i in range(len(inp)):
        n += 1
        if inp[i] not in history.keys():
            diff = 0
            last = inp[i]
        else:
            diff = n - history[inp[i]]
            last = inp[i]
        history[inp[i]] = n
        #print(f'history[{inp[i]}] = {n}')
    while n < target:
        n += 1
        last = diff
        if diff not in history.keys():
            diff = 0
            #print(f'history[{last}] = {n}')
        else:
            diff = n - history[diff]
        history[last] = n
        #print(f'history[{last}] = {n}')
    print(f'last = {last}')




inp = [18,8,0,5,4,1,20]

test_input = [0,3,6]
#inp = test_input

do_it(inp, 30000000)

#file_input.close()

'''
SCRATCH PAD RIGHT HERE

dictionary, key is number and value is last position used

Part 2: there must be some kind of pattern I can collapse to avoid iterating straight

Record every new number found (yielding 0) - is there a pattern/measurement?

'''