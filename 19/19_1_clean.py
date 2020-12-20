file_input = open("input1219.txt", "r")
#file_input = open("test_input.txt", "r")
lines = file_input.readlines()

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
                total += 1 
    return total

def satisfy(rule_dict, rule_num, message):
    satisfied = False
    remaining_message = message
    requirements = rule_dict[rule_num]
    if remaining_message == '':
        satisfied, remaining_message = False, ''
    elif requirements[0] == 'a' or requirements[0] == 'b':
        if message[0] == requirements[0]:
            satisfied, remaining_message = True, message[1:]
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