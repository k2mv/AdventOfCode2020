file_input = open("input1216.txt", "r")
#file_input = open("test_input2.txt", "r")
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
    valid_ticket_list = []
    #valid_ticket = True
    for t in nearby_tickets:
        valid_ticket = True
        for num in t:
            if not validate_against_fields(fields, num):
                valid_ticket = False
        if valid_ticket:
            valid_ticket_list.append(t)
    return valid_ticket_list
    
def do_it2(fields, your_ticket, valid_tickets):
    num_fields = len(fields)
    big_grid = []
    for _ in range(num_fields):
        asdf = []
        for _ in range(num_fields):
            asdf.append(True)
        big_grid.append(asdf)
    for t in valid_tickets:
        for n in range(num_fields): # for each position on the ticket
            for f in range(num_fields): # for each field in list of fields
                if not validate_against_field(fields[f], t[n]):
                    big_grid[n][f] = False # this position cannot be this field
    return big_grid

def do_it3(fields, big_grid):
    big_dict = {}
    big_range = len(big_grid)
    for position in range(big_range):
        counter = 0
        selected_field = -1
        for field in range(big_range):
            if big_grid[position][field]:
                counter += 1
                selected_field = field
        if counter == 1:
            #big_dict[position] = selected_field
            big_dict[selected_field] = position
    #print(big_dict)

    return big_dict

def do_it4(fields, big_dict, big_grid):
    big_range = len(big_grid)
    for position in range(big_range):
        counter = 0
        selected_field = -1
        #if position not in big_dict.keys():
        if position not in big_dict.values():
            for field in range(big_range):
                #if field not in big_dict.values():
                if field not in big_dict.keys():
                    if big_grid[position][field]:
                        counter += 1
                        selected_field = field
        if counter == 1:
            #big_dict[position] = selected_field
            big_dict[selected_field] = position
    return big_dict, big_grid

def validate_against_fields(fields, num):
    valid = False
    for f in fields:
        min = f[1][0]
        hole_lower = f[1][1]
        hole_upper = f[1][2]
        max = f[1][3]
        if num >= min and num <= max and (num <= hole_lower or num >= hole_upper):
            valid = True
    return valid

def validate_against_field(f, num):
    valid = False
    min = f[1][0]
    hole_lower = f[1][1]
    hole_upper = f[1][2]
    max = f[1][3]
    #if not(num < min or (num > hole_lower and num < hole_upper) or num > max):
    if num >= min and num <= max and (num <= hole_lower or num >= hole_upper):
        valid = True
    return valid



inp = process_input(lines)
#print(inp)
fields, your_ticket, nearby_tickets = inp[0], inp[1], inp[2]
#print(fields)

valid_tickets = do_it(fields, your_ticket, nearby_tickets) # not working
#print(valid_tickets)
big_grid = do_it2(fields, your_ticket, valid_tickets) # not working yet?
#big_dict, new_grid = do_it3(inp[0], big_grid)
#print(big_grid)
big_dict = do_it3(fields, big_grid)
#print(big_dict)

while len(big_dict) < len(big_grid):
    do_it4(fields, big_dict, big_grid)
print(big_dict)
departures = 1

for f in range(len(fields)):
    if fields[f][0].startswith('departure'): # if field name starts w/departure
        # find the big_dict key that refers to this field
        pos = big_dict[f]
        departures *= your_ticket[pos] 
print(departures)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

Find out how many values are invalid for all fields

Part 2: 2 dimensional array - for each field position on the ticket, an array of T/F
for each field on our list of fields
For each ticket,
    For each field position on the ticket,
        For each field on list of fields,
            check if the number in this field position is invalid for this field
                If so, then flip to False

How do exclude things in the dict and continue finding things that resolve to one
possible field only?
'''