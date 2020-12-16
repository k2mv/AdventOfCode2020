file_input = open("input1216.txt", "r")
#file_input = open("test_input2.txt", "r")
lines = file_input.readlines()

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
                for ls in l.split(','):
                    other.append(int(ls))
                nearby_tickets.append(other)
            
    return (fields, your_ticket, nearby_tickets)

def filter_valid(fields, nearby_tickets):
    valid_ticket_list = []
    for t in nearby_tickets:
        valid_ticket = True
        for num in t:
            if not validate_against_fields(fields, num):
                valid_ticket = False
        if valid_ticket:
            valid_ticket_list.append(t)
    return valid_ticket_list
    
def create_valid_field_grid(fields, valid_tickets):
    num_fields = len(fields)
    valid_field_grid = []
    for _ in range(num_fields):
        asdf = []
        for _ in range(num_fields):
            asdf.append(True)
        valid_field_grid.append(asdf)
    for t in valid_tickets:
        for n in range(num_fields): # for each position on the ticket
            for f in range(num_fields): # for each field in list of fields
                if not validate_against_field(fields[f], t[n]):
                    valid_field_grid[n][f] = False # this position cannot be this field
    return valid_field_grid

def build_field_dict(fields, valid_field_grid):
    big_range = len(valid_field_grid)
    field_dict = {}
    while len(field_dict) < big_range:
        for position in range(big_range):
            counter = 0
            selected_field = -1
            if position not in field_dict.values():
                for field in range(big_range):
                    if field not in field_dict.keys():
                        if valid_field_grid[position][field]:
                            counter += 1
                            selected_field = field
            if counter == 1: # deduced that this position can only be one field
                field_dict[selected_field] = position
    return field_dict

def validate_against_fields(fields, num):
    valid = False
    for f in fields:
        valid = valid or validate_against_field(f, num)
    return valid

def validate_against_field(f, num):
    valid = False
    min, hole_lower, hole_upper, max = f[1]
    if num >= min and num <= max and (num <= hole_lower or num >= hole_upper):
        valid = True
    return valid

fields, your_ticket, nearby_tickets = process_input(lines)
valid_tickets = filter_valid(fields, nearby_tickets)
valid_field_grid = create_valid_field_grid(fields, valid_tickets)
field_dict = build_field_dict(fields, valid_field_grid)
print(field_dict)

departures = 1
for f in range(len(fields)):
    if fields[f][0].startswith('departure'): # if field name starts w/departure
        pos = field_dict[f] # get the actual ticket position corresponding to this field
        departures *= your_ticket[pos] 
print(departures)

file_input.close()
