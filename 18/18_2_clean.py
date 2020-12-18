file_input = open("input1218.txt", "r")
#file_input = open("test_input.txt", "r")
lines = file_input.readlines()

def process_input(lines):
    ret = []
    for l in lines:
        ret.append(l.split())
    return ret

def eval_line(line):
    buffer = []
    mult_buffer = []
    operator = None
    left = None
    right = None
    for chunk in line:
        if chunk.isnumeric():
            if left is None:
                left = int(chunk)
            else:
                if operator == '+':
                    right = int(chunk)
                    left = left + right
                    operator = None
                    right = None
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
            for _ in range(right_paren_count):
                mult_buffer.append(right)
                right = mult_dump(mult_buffer)
                left, operator, mult_buffer = buffer.pop()
                if operator == '+':
                    right = left + right
            left = right
            operator = None
            right = None
        elif chunk == '+':
            operator = '+'
        elif chunk == '*':
            mult_buffer.append(left)
            left = None
            operator = None
            right = None
    mult_buffer.append(left)
    left = mult_dump(mult_buffer)
    return left

def mult_dump(mult_buffer):
    accum = 1
    for item in mult_buffer:
        accum *= item
    return accum

inp = process_input(lines)
accum = 0
for eq in inp:
    accum += eval_line(eq)
print(accum)

file_input.close()