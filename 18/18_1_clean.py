file_input = open("input1218.txt", "r")
#file_input = open("test_input.txt", "r")
lines = file_input.readlines()

def process_input(lines):
    ret = []
    for l in lines:
        ret.append(l.split())
    return ret

def operate(operator, left, right):
    answer = None
    if operator == '+':
        answer = left + right
    elif operator == '*':
        answer = left * right
    return answer

def eval_line(line):
    buffer = []
    operator = None
    left = None
    right = None
    for chunk in line:
        if chunk.isnumeric():
            if left is None:
                left = int(chunk)
            else: # '+' or '#'
                left = operate(operator, left, int(chunk))
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
            operator = '+'
        elif chunk == '*':
            operator = '*'
    print(left)
    return left

inp = process_input(lines)
accum = 0
for eq in inp:
    accum += eval_line(eq)
print(accum)

file_input.close()