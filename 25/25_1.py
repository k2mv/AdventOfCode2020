file_input = open("input1225.txt", "r")
#file_input = open("test_input.txt", "r")
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
    keys = []
    for l in lines:
        l = l.split()
        keys.append(int(l[0]))
    return keys

def transform(subject, loops):
    value = 1
    for _ in range(loops):
        value *= subject
        value = value % 20201227
    return value

def investigate(subject, target):
    value = 1
    loop_count = 0
    done = False
    while not done:
        loop_count += 1
        value *= subject
        value = value % 20201227
        #print(value)
        if value == target:
            done = True
    return loop_count

def investigate2(subject):
    pass

keys = process_input(lines)
print(keys)
key1, key2 = keys[0], keys[1]
print(f'loop count 1: {investigate(7, keys[0])}')
print(f'loop count 2: {investigate(7, keys[1])}')
loops1 = investigate(7, keys[0])
loops2 = investigate(7, keys[1])

print(transform(key1, loops2))
print(transform(key2, loops1))

file_input.close()

'''
SCRATCH PAD RIGHT HERE


'''