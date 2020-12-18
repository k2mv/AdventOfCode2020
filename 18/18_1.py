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

def plus(left, right):
    new_left = left + right
    return (new_left)
def minus(left, right):
    new_left = left - right
    return (new_left)
def multiply(left, right):
    new_left = left * right
    return (new_left)
def divide(left, right):
    new_left = left / right
    return (new_left)

def operate(operator, left, right):
    if operator == '+':
        answer = left + right
        left = answer
        operator = None
        right = None
    if operator == '-':
        answer = left - right
        left = answer
        operator = None
        right = None
    if operator == '*':
        answer = left * right
        left = answer
        operator = None
        right = None
    if operator == '/':
        answer = left // right
        left = answer
        operator = None
        right = None
    return answer

def eval_line(line):
    buffer = []
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
                    answer = left + right
                    left = answer
                    operator = None
                    right = None
                if operator == '-':
                    right = int(chunk)
                    answer = left - right
                    left = answer
                    operator = None
                    right = None
                if operator == '*':
                    right = int(chunk)
                    answer = left * right
                    left = answer
                    operator = None
                    right = None
                if operator == '/':
                    right = int(chunk)
                    answer = left // right
                    left = answer
                    operator = None
                    right = None
        elif chunk.count('(') > 0:
            while chunk[0] == '(':
                buffer.append((left, operator))
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
            left = operate(operator, left, right)
            for _ in range(right_paren_count):
                right = left
                left, operator = buffer.pop()
                if operator is None:
                    left = right
                    operator = None
                    right = None
                else:
                    left = operate(operator, left, right)
                    operator = None
                    right = None
        elif chunk == '+':
            if right is None:
                operator = '+'
        elif chunk == '-':
            if right is None:
                operator = '-'
        elif chunk == '*':
            if right is None:
                operator = '*'
        elif chunk == '/':
            if right is None:
                operator = '/'
        #print(f'left={left}, operator={operator}')
    print(left)
    return left


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