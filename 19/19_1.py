file_input = open("input1219.txt", "r")
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
    total = 0
    rule_dict = {}
    phase = 0
    for l in lines:
        chunk = l.split()
        if phase == 0:
            if l != '\n':
                rules_buffer = []
                buffer = []
                index = (int(chunk[0][:-1]))
                for n in range(1,len(chunk)):
                    if chunk[n].isnumeric():
                        buffer.append(int(chunk[n]))
                    elif chunk[n] == '|':
                        rules_buffer.append(buffer)
                        buffer = []
                    elif chunk[n].startswith('"'):
                        buffer = chunk[n][1]
                rules_buffer.append(buffer)
                rule_dict[index] = rules_buffer
            else:
                phase = 1
                print(rule_dict)
        elif phase == 1:
            message = chunk[0]
            if satisfy(rule_dict, 0, message) == (True, ''):
                #print('hit')
                total += 1
            else:
                #print('miss')
                pass
    
    return total

def satisfy(rule_dict, rule_num, message):
    #print(f'satisfy(_, {rule_num}, {message})')
    satisfied = False
    remaining_message = message
    requirements = rule_dict[rule_num]
    if remaining_message == '':
        return False, ''
    if requirements[0] == 'a' or requirements[0] == 'b':
        if message[0] == requirements[0]:
            satisfied = True
            remaining_message = message[1:]
    else:
        saved_state = remaining_message
        for rule_list in requirements:
            rule_list_status = True
            for r_num in rule_list:
                response, remaining_message = satisfy(rule_dict, r_num, remaining_message)
                if not response:
                    rule_list_status = False
                    break
            if rule_list_status:
                satisfied = True
                break
            else:
                remaining_message = saved_state
    return satisfied, remaining_message


inp = process_input(lines)

print(inp)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

Part 1: Get to Rule 0 or fail

Verify each input against the list of rules
- We can't expand to every possible valid string, that's too much
- We build a tree search with linkages?
    - Depth first search

Rule format: max is "n: n n | n n" (on quick glance)

So my rule format is
[1, [[2, 3],[4,5]]]
Index followed by list of valid set(s) of rules
'''