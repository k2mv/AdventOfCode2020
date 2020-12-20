#file_input = open("input1219.txt", "r")
file_input = open("input1219_2.txt", "r")
#file_input = open("test_input2.txt", "r")
lines = file_input.readlines()

def process_input(lines):
    total = 0
    rule_dict = {}
    chunk_dict = {}
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
                chunk_dict = build_chunk_dict(rule_dict)
                print(chunk_dict)
        elif phase == 1:
            message = chunk[0]
            if chunkwise_satisfy(message, chunk_dict):
                total += 1
    return total

def build_chunk_dict(rule_dict):
    chunk_dict = {}
    forty_two = False
    thirty_one = False
    for n in range(256): # hard coded for apparent chunk length of 8
        bin = f'{n:08b}' # e.g. '00000000', '00000001' etc.
        check_str = ''
        for ch in bin: # e.g. 'aaaaaaaa', 'aaaaaaab' etc.
            if ch == '0':
                check_str = check_str + 'a'
            elif ch == '1':
                check_str = check_str + 'b'
        forty_two, _ = satisfy(rule_dict, 42, check_str)
        thirty_one, _ = satisfy(rule_dict, 31, check_str)
        if forty_two and not thirty_one:
            chunk_dict[check_str] = 42
        elif thirty_one and not forty_two:
            chunk_dict[check_str] = 31
    return chunk_dict

def chunkwise_satisfy(message, chunk_dict):
    accept = False
    sequence = []
    forty_two = 0
    thirty_one = 0
    phase = 0
    num_chunks = len(message) // 8
    if num_chunks >= 3:
        for n in range(num_chunks):
            chunk = message[n*8:(n*8)+8]
            if chunk in chunk_dict.keys():
                sequence.append(chunk_dict[chunk])
    print(sequence) # e.g. [42, 42, 42, 42, 31, 31]
    '''
    Enforce format:
    - at least two consecutive 42s, followed by
    - at least one consecutive 31 but strictly fewer than the # of 42s
    '''
    for n in range(len(sequence)):
        if phase == 0:
            if sequence[n] == 42:
                forty_two += 1
                phase = 1
            else:
                phase = 4  # There is no phase 4
        elif phase == 1:
            if sequence[n] == 42:
                forty_two += 1
                phase = 2
            else:
                phase = 4
        elif phase == 2:
            if sequence[n] == 42:
                forty_two += 1
            elif sequence[n] == 31:
                thirty_one += 1
                phase = 3
        elif phase == 3:
            if sequence[n] == 42:
                phase = 4
            elif sequence[n] == 31:
                thirty_one += 1
    print(f'phase={phase}, thirty_one={thirty_one}, forty_two={forty_two}')
    accept = phase == 3 and thirty_one < forty_two
    return accept

def satisfy(rule_dict, rule_num, message):
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