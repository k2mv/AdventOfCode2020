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
    for n in range(10,1000001):
        ret.append(n)
    return ret

def setup_million():
    cups = []
    next_cups = []
    # zero index the cups
    for n in range(1000000):
        cups.append(n)
        if n == 999999:
            next_cups.append(1)
        else:
            next_cups.append(n+1)
    # hard code the first few cup 'nexts'
    # 643719258 -> 532608147 [9 10...]
    next_cups[999999] = 5
    next_cups[0] = 8
    next_cups[1] = 4
    next_cups[2] = 6
    next_cups[3] = 2
    next_cups[4] = 7
    next_cups[5] = 3
    next_cups[6] = 0
    next_cups[7] = 9
    next_cups[8] = 1
    return cups, next_cups

def move2(cups, next_cups, index):
    index_plus_1 = next_cups[index]
    index_plus_2 = next_cups[index_plus_1]
    index_plus_3 = next_cups[index_plus_2]
    index_plus_4 = next_cups[index_plus_3]

    if index == 0:
        target = 999999
    else:
        target = index - 1
    while target in (index_plus_1, index_plus_2, index_plus_3):
        if target == 0:
            target = 999999
        else:
            target -= 1

    temp = next_cups[target]
    next_cups[target] = index_plus_1
    next_cups[index] = index_plus_4
    next_cups[index_plus_3] = temp

    return cups, next_cups, index_plus_4

def move(cups):
    held_cups = []
    current_cup = cups[0]
    #print(f'current_cup = {current_cup}')
    #print(f'State of cups: {cups}')
    #print(f'Current cup: {current_cup}')
    for _ in range(3):
        held_cups.append(cups.pop(1))
    #print(f'Held cups: {held_cups}')
    target = current_cup - 1
    if target == 0:
        target = 999999
    while target in held_cups:
        target_minus_one = target - 1
        target_minus_one = (target_minus_one - 1) % 1000000
        target = target_minus_one + 1
    #print(f'Destination: {target}')
    index_to_insert_at = cups.index(target) + 1
    while len(held_cups) > 0:
        cups.insert(index_to_insert_at, held_cups.pop())
    cups.append(cups.pop(0))
    return cups

cups, next_cups = setup_million()
index = 5
for _ in range(10000000):
    #print(f'current: {index}')
    cups, next_cups, index = move2(cups, next_cups, index)
print(f'1 {next_cups[0]+1} {next_cups[next_cups[0]]+1} = {(next_cups[0]+1) * (next_cups[next_cups[0]]+1)}')


#file_input.close()

'''
SCRATCH PAD RIGHT HERE

So we seem to have another 'don't set your computer on fire' problem

When 1 is sent to the back of the list, it doesn't move for a long while

But that only gets me to 114/118 which doesn't look right

There's a repeating pickup with n is followed by n-1

action on the beginning and the end and not much else

6 [4 3 7] 1 9 2 5 8

1 9 2 5 [4 3 7] 8 10 . . . 1000000 6

1 [9 2 5] 4 3 7 8 10

4 3 7 8 10 11 12 13 14 . . . 1000000 [9 2 5] 6 1

4 [3 7 8] 10 11 12 13 14

10 11 12 13 14 15 16 17 18 19 . . . 1000000 9 2 [3 7 8] 5 6 1 4

10 [11 12 13] 14 15 16 17 18 19

14 15 16 17 18 19 . . . 1000000 9 [11 12 13] 2 3 7 8 5 6 1 4 10

14 [15 16 17] 18 . . .

18 19 20 . . . 1000000 9 11 12 13 [15 16 17] 2 3 7 8 5 6 1 4 10 14

All these memory operations are burning time
Maybe there's a way to do it in place?

It looks completely chaotic once we get through 1000000 in some
arrangement on the first pass

Work in place... rewrite orders in a 1 million place array?
Hard to do when you have to do so many inserts at random places

Are there any shortcuts that you can skip over a few hundred thousand
iterations... and still keep accurate count?

Either efficiency or shortcuts, or both.

What will be the pickup when the iteration reaches 1?
1000010 would be at the end if it existed
1000006
1000002
 999998
so [999995 999996 999997] would be placed in the muck , then 999998 is new current
picks up [999999 1000000 9]
drops it next to 999997 in the muck
now 11 is current
[12 13 15] placed right of 10, 11 at end
16 is current
[17 2 3] picked up...

that doesn't seem to be going anywhere

Linked list?  One direction?

List 1 to 1000000, second parallel list saying which is next?

So can you simulate rearrangement with this?





'''