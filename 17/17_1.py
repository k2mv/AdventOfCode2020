file_input = open("input1217.txt", "r")
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
    plane = []
    for l in lines:
        l = l.strip()
        row = []
        for ch in l:
            if ch == '#':
                row.append(1)
            else:
                row.append(0)
        plane.append(row)
    return plane

def eval_plane(space):
    pass

def eval_cell(active, space, width, pla, row, col):
    neighbors = 0
    neighbors += eval_above(space, width, pla, row, col)
    neighbors += eval_below(space, width, pla, row, col)
    neighbors += eval_eight_around(space, width, pla, row, col)
    #print(f'space[{pla}][{row}][{col}] curr={active} neighbors={neighbors}')
    if active == 1 and (neighbors < 2 or neighbors > 3):
        active = 0
    elif active == 0 and neighbors == 3:
        active = 1
    #print(f'new={active}')
    return active

def eval_above(space, width, pla, row, col):
    neighbors = 0
    if pla != len(space) - 1: # not top plane
        neighbors += eval_flat_nine(space, width, pla+1, row, col, True)
    return neighbors

def eval_below(space, width, pla, row, col):
    neighbors = 0
    if pla == 0:
        neighbors += eval_flat_nine(space, width, pla+1, row, col, True)
    else:
        neighbors += eval_flat_nine(space, width, pla-1, row, col, True)
    return neighbors

def eval_eight_around(space, width, pla, row, col):
    neighbors = 0
    neighbors += eval_flat_nine(space, width, pla, row, col, False)
    return neighbors

def eval_flat_nine(space, width, pla, row, col, check_center):
    neighbors = 0
    for r in (row-1, row, row+1):
        if r >= 0 and r < width:
            for c in (col-1, col, col+1):
                if c >= 0 and c < width:
                    if check_center or r != row or c != col:
                        neighbors += space[pla][r][c]
    return neighbors

def expand_space(space):
    new_space = []
    width = len(space[0])
    for pl in range(len(space)):
        new_plane = []
        new_plane.append(row_of_zeroes(width+2))
        for n in range(width):
            row = [0]
            row.extend(space[pl][n])
            row.append(0)
            new_plane.append(row)
        new_plane.append(row_of_zeroes(width+2))
        new_space.append(new_plane)
    # add new plane on top
    new_plane = []
    for _ in range(width+2):
        new_plane.append(row_of_zeroes(width+2))
    new_space.append(new_plane)
    return new_space

def new_blank_plane_above(plane):
    width = len(plane)
    new_plane = []
    for _ in range(width):
        new_row = []
        for _ in range(width):
            new_row.append(0)
        new_plane.append(new_row)
    return new_plane

def process_space(space):
    new_space = []
    width = len(space[0])
    for pl in range(len(space)):
        new_plane = []
        for r in range(width):
            new_row = []
            #print(f'new_row, pl={pl} r={r}')
            for c in range(width):
                new_cube = eval_cell(space[pl][r][c], space, width, pl, r, c)
                new_row.append(new_cube)
            new_plane.append(new_row)
        new_space.append(new_plane)
    return new_space

def row_of_zeroes(length):
    ret = []
    for _ in range(length):
        ret.append(0)
    return ret

def print_space(space):
    for pl in range(len(space)):
        print_plane(pl, space[pl])

def print_plane(index, plane):
    print(f'z={index}')
    for r in range(len(plane)):
        string = ''
        for c in range(len(plane)):
            chr = '?'
            if plane[r][c] == 0:
                chr = '.'
            elif plane[r][c] == 1:
                chr = '#'
            string = string + chr
        print(string)

def count_cubes(space):
    accum = 0
    width = len(space[0])
    for pl in range(len(space)):
        if pl == 0:
            multiplier = 1
        else:
            multiplier = 2
        for r in range(width):
            for c in range(width):
                accum += space[pl][r][c] * multiplier
    return accum


plane = process_input(lines)
space = [plane, new_blank_plane_above(plane)] # plane is index 0
#print_space(space)
'''
space = expand_space(space)
space = process_space(space)
space = expand_space(space)
space = process_space(space)
print_space(space)
'''

runtime = 6
iter = 0
while iter < runtime:
    iter += 1
    space = expand_space(space)
    space = process_space(space)
print(f'Total cubes = {count_cubes(space)}')



file_input.close()

'''
SCRATCH PAD RIGHT HERE

How to search a 3-dimensional space?
Six cycles - how many layers (max layers?) do we have to project
(on top of the layer we have now)

Is the dimension always symmetric going up and down? (It appears so)

So maybe we only have to track 'half' the dimensions?  And just count the +1
dimension twice when reckoning the zero layer

Always keep an eye on the 'edge' of every plane (highest main plane, first/last row,
beginning/end of each row)

Keep an empty layer above the current top layer
Keep an empty row before and after the known row
Keep an empty 'endcap' before and after the ends of the known row
Or... just search a '-1' and 'len' coordinate, they don't exist now but
if any of them become active, we get to expand our space

Just expand space every round regardless
For input of grid n x n:
- sandwich each row between zeroes (new len n+2)
- sandwich rows between rows of n+2 zeroes
- create new n+2 x n+2 plane on top

Twenty-six boxes to check
* n +- 1 x n +- 1 above and below (above twice if this is plane 0)
* n +- 1 x n +- 1 in a donut around yourself


01:47 I'm having a consistent issue where process_space() shifts all the results
down one row (leaving all x on the top row) and I can't figure out why

'''