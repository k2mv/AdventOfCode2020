file_input = open("input1216.txt", "r")
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

    fields = []
    nearby_tickets = []
    position = 0
    for l in lines:
        if position == 0:
            if l != '\n':
                quartet = []
                halves = l.split(':')
                ranges = halves[1].split(' or ')
                for r in ranges:
                    asdf = r.split('-')
                    quartet.append(int(asdf[0]))
                    quartet.append(int(asdf[1]))
                fields.append((halves[0], quartet))
            else:
                position = 1
        elif position == 1:
            if l.startswith('your'):
                pass
            elif l != '\n':
                your_ticket = []
                lsplit = l.split(',')
                for ls in lsplit:
                    your_ticket.append(int(ls))
            else:
                position = 2
        elif position == 2:
            if l.startswith('nearby'):
                pass
            else:
                other = []
                lsplit = l.split(',')
                for ls in lsplit:
                    other.append(int(ls))
                nearby_tickets.append(other)
            
    return (fields, your_ticket, nearby_tickets)

def do_it(fields, your_ticket, nearby_tickets):
    accum = 0
    for t in nearby_tickets:
        for num in t:
            if not validate_against_fields(fields, num):
                print(f'Invalid: {num}')
                accum += num
    print(f'accum = {accum}')


def validate_against_fields(fields, num):
    valid = False
    for f in fields:
        min = f[1][0]
        hole_lower = f[1][1]
        hole_upper = f[1][2]
        max = f[1][3]
        if not(num < min or (num > hole_lower and num < hole_upper) or num > max):
            valid = True
    return valid



inp = process_input(lines)
#print(inp)

do_it(inp[0], inp[1], inp[2])

file_input.close()

'''
SCRATCH PAD RIGHT HERE

Find out how many values are invalid for all fields

'''