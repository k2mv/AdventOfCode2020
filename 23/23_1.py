#file_input = open("input1223.txt", "r")
#file_input = open("test_input.txt", "r")
#lines = file_input.readlines()

# LIST METHODS
# append(this), count(of_this)
# extend(iterable_to_append)
# index(of_first_this), insert(index, element)
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

def process_input(string_in):
    ret = []
    for ch in range(len(string_in)):
        ret.append(int(string_in[ch]))
    return ret

def move(cups):
    held_cups = []
    current_cup = cups[0]
    print(f'State of cups: {cups}')
    print(f'Current cup: {current_cup}')
    for _ in range(3):
        held_cups.append(cups.pop(1))
    print(f'Held cups: {held_cups}')
    target = current_cup - 1
    if target == 0:
        target = 9
    while target in held_cups:
        target_minus_one = target - 1
        target_minus_one = (target_minus_one - 1) % 9
        target = target_minus_one + 1
    print(f'Destination: {target}')
    index_to_insert_at = cups.index(target) + 1
    while len(held_cups) > 0:
        cups.insert(index_to_insert_at, held_cups.pop())
    cups.append(cups.pop(0))
    return cups

test_input = '389125467'
input = '643719258'

#cups = process_input(test_input)
cups = process_input(input)
print(cups)
for n in range(100):
    print(f'move {n+1}')
    cups = move(cups)
    print()

print(f'Final: {cups}')

#file_input.close()

'''
SCRATCH PAD RIGHT HERE


'''