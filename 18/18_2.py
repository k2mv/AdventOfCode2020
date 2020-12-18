file_input = open("input1218.txt", "r")
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
    ret = []
    for l in lines:
        ret.append(l.split())
    return ret

def operate(operator, left, right):
    if operator == '+':
        answer = left + right
        left = answer
        operator = None
        right = None
    if operator == '*':
        answer = left * right
        left = answer
        operator = None
        right = None
    return answer

def eval_line(line):
    buffer = []
    mult_buffer = []
    operator = None
    left = None
    right = None
    for chunk in line:
        if chunk.isnumeric():
            chunknum = int(chunk)
            if left is None:
                left = chunknum
            else:
                if operator == '+':
                    right = int(chunk)
                    left = left + right
                    operator = None
                    right = None
                #if operator == '*':
        elif chunk.count('(') > 0:
            while chunk[0] == '(':
                buffer.append((left, operator, mult_buffer))
                mult_buffer = []
                left = None
                operator = None
                chunk = chunk[1:]
            left = int(chunk)
        elif chunk.count(')') > 0:
            right_paren_count = 0
            while chunk[-1] == ')':
                right_paren_count += 1
                chunk = chunk[:-1]
            right = int(chunk)
            if operator == '+':
                right = left + right
            else:
                pass
            for _ in range(right_paren_count):
                mult_buffer.append(right)
                right = mult_dump(mult_buffer)
                left, operator, mult_buffer = buffer.pop()
                if operator == '+':
                    right = left + right
            #print(f'XXX left={left}, operator={operator}, mult_buffer={mult_buffer}, buffer={buffer}')
            left = right
            operator = None
            right = None
            '''
            left = operate(operator, left, right)
            for _ in range(right_paren_count):
                right = left
                left, operator, mult_buffer = buffer.pop()
                if operator is None:
                    left = right
                    operator = None
                    right = None
                else:
                    left = operate(operator, left, right)
                    operator = None
                    right = None
            '''
        elif chunk == '+':
            operator = '+'
        elif chunk == '*':
            mult_buffer.append(left)
            left = None
            operator = None
            right = None
        #print(f'left={left}, operator={operator}, mult_buffer={mult_buffer}, buffer={buffer}')
    mult_buffer.append(left)
    if len(mult_buffer) > 0:
        left = mult_dump(mult_buffer)
    #print(left)
    return left

def mult_dump(mult_buffer):
    accum = 1
    for item in mult_buffer:
        accum *= item
    return accum

inp = process_input(lines)
accum = 0
#eval_line(inp[0])
for eq in inp:
    accum += eval_line(eq)
print(accum)

file_input.close()

'''
SCRATCH PAD RIGHT HERE


'''