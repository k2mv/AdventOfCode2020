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
    hyperspace = [[plane]]
    return hyperspace

def eval_plane(space):
    pass

def eval_cell(active, space, width, pla, row, col):
    neighbors = 0
    # above
    if pla != len(space) - 1:
        neighbors += eval_flat_nine(space, width, pla, row, col, 1, True)
    # below
    if pla == 0:
        neighbors += eval_flat_nine(space, width, pla, row, col, 1, True)
    else:
        neighbors += eval_flat_nine(space, width, pla, row, col, -1, True)
    # around self
    neighbors += eval_flat_nine(space, width, pla, row, col, 0, False)
    if active == 1 and (neighbors < 2 or neighbors > 3):
        active = 0
    elif active == 0 and neighbors == 3:
        active = 1
    return active

def eval_hypercell(active, hyperspace, hyperwidth, width, spa, pla, row, col):
    neighbors = 0
    # hyperabove
    if spa != len(hyperspace) - 1:
        #print(f'hyperabove: spa = {spa}')
        neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, 1, True)
    # hyperbelow
    if spa == 0:
        neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, 1, True)
    else:
        neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, -1, True)
    # hyperaround
    neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, 0, False)
    
    # TEST
    #if (spa == 2 and pla == 0):
    #if (spa == 0 and pla == 2):
        #print(f'spa={spa}, pla={pla}, row={row}, col={col}, neighbors={neighbors} active={active}')
    if active == 1 and (neighbors < 2 or neighbors > 3):
        active = 0
    elif active == 0 and neighbors == 3:
        active = 1
    #if spa == 2 and pla == 0 or (spa == 0 and pla == 2):
    #    print(f'new_active={active}')
    return active

def eval_flat_nine(space, width, pla, row, col, pla_offset, check_center):
    neighbors = 0
    for r in (row-1, row, row+1):
        if r >= 0 and r < width:
            for c in (col-1, col, col+1):
                if c >= 0 and c < width:
                    if check_center or r != row or c != col:
                        neighbors += space[pla+pla_offset][r][c]
    return neighbors

def eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, spa_offset, check_center):
    neighbors = 0
    for p in (pla-1, pla, pla+1):
        if p >= 0 and p < len(hyperspace):
            for r in (row-1, row, row+1):
                if r >= 0 and r < width:
                    for c in (col-1, col, col+1):
                        if c >= 0 and c < width:
                            if check_center or p != pla or r != row or c != col:
                                neighbors += hyperspace[spa+spa_offset][p][r][c]
        if p == -1:
            for r in (row-1, row, row+1):
                if r >= 0 and r < width:
                    for c in (col-1, col, col+1):
                        if c >= 0 and c < width:
                            if check_center or 1 != pla or r != row or c != col:
                                neighbors += hyperspace[spa+spa_offset][1][r][c]
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

def expand_hyperspace(hyperspace):
    for sp in range(len(hyperspace)):
        hyperspace[sp] = expand_space(hyperspace[sp])
    hyperspace.append(new_zero_space(hyperspace[sp]))
    
    return hyperspace

def new_zero_plane(plane):
    width = len(plane)
    new_plane = []
    for _ in range(width):
        new_row = []
        for _ in range(width):
            new_row.append(0)
        new_plane.append(new_row)
    return new_plane

def new_zero_space(space):
    hyperwidth = len(space)
    width = len(space[0])
    new_space = []
    for _ in range(hyperwidth):
        new_plane = []
        for _ in range(width):
            new_row = []
            for _ in range(width):
                new_row.append(0)
            new_plane.append(new_row)
        new_space.append(new_plane)
    return new_space


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

def process_hyperspace(hyperspace):
    new_hyperspace = []
    hyperwidth = len(hyperspace)
    width = len(hyperspace[0][0])
    for sp in range(len(hyperspace)):
        new_space = []
        for pl in range(hyperwidth):
            new_plane = []
            for r in range(width):
                new_row = []
                for c in range(width):
                    new_hypercube = eval_hypercell(hyperspace[sp][pl][r][c], hyperspace, hyperwidth, width, sp, pl, r, c)
                    new_row.append(new_hypercube)
                new_plane.append(new_row)
            new_space.append(new_plane)
        new_hyperspace.append(new_space)
    return new_hyperspace

def row_of_zeroes(length):
    ret = []
    for _ in range(length):
        ret.append(0)
    return ret

def print_hyperspace(hyperspace):
    hyperwidth = len(hyperspace)
    #width = len(hyperspace[0][0])
    for spa in range(hyperwidth):
        for pla in range(len(hyperspace[0])):
            print_plane(hyperspace, spa, pla)

def print_plane(hyperspace, spa, pla):
    print(f'z={pla}, w={spa}')
    width = len(hyperspace[0][0])
    for r in range(width):
        string = ''
        for c in range(width):
            chr = '?'
            if hyperspace[spa][pla][r][c] == 0:
                chr = '.'
            elif hyperspace[spa][pla][r][c] == 1:
                chr = '#'
            string = string + chr
        print(string)

def count_cubes(hyperspace, sp):
    accum = 0
    space = hyperspace[sp]
    width = len(space[0])
    for pl in range(len(space)):
        multiplier = 1
        if pl > 0:
            multiplier *= 2
        if sp > 0:
            multiplier *= 2
        #print(f'z={pl}, w={sp} multiplier={multiplier}')
        #print(f'sp = {sp}, pl = {pl}, multiplier = {multiplier}')
        for r in range(width):
            for c in range(width):
                if hyperspace[sp][pl][r][c] == 1:
                    #print('hit')
                    accum += hyperspace[sp][pl][r][c] * multiplier
    #print(f'count_cubes_accum = {accum}\n')
    return accum

def count_hypercubes(hyperspace):
    accum = 0
    for sp in range(len(hyperspace)):
        count_in_cube = count_cubes(hyperspace, sp)
        #print(f'count_cubes(hyperspace, {sp}) = {count_in_cube}')
        #print(f'hypercube_accum = {accum} + {count_in_cube}')
        accum += count_in_cube
        #print(f'hypercube_accum = {accum}\n\n')
    return accum


hyperspace = process_input(lines)
hyperspace = [[hyperspace[0][0], new_zero_plane(hyperspace[0][0])]]
#print(hyperspace)
hyperspace = [hyperspace[0], new_zero_space(hyperspace[0])]
#print(hyperspace)

runtime = 6
iter = 0
while iter < runtime:
    iter += 1
    hyperspace = expand_hyperspace(hyperspace)
    hyperspace = process_hyperspace(hyperspace)

#print_hyperspace(hyperspace)

print(count_hypercubes(hyperspace))



'''
plane = process_input(lines)
space = [plane, new_zero_plane(plane)] # plane is index 0
#print_space(space)
'''
'''
space = expand_space(space)
space = process_space(space)
space = expand_space(space)
space = process_space(space)
print_space(space)
'''

'''
runtime = 6
iter = 0
while iter < runtime:
    iter += 1
    space = expand_space(space)
    space = process_space(space)
print(f'Total cubes = {count_cubes(space)}')
'''


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
ANSWER: needed to expand before running - 'window' of result is shifted one down
(example was rather non-obvious at communicating this)
> (and the frame of view follows the active cells in each cycle):

Part 2: Hyperspace

Uhhhhh

BIGGEST QUESTION: What is the symmetry in hyperspace, i.e. how any cubes do I
*actually* need to keep track of in order to be able to reconstruct the true
state of the hyperspace for purposes of simulating and counting?

After one run:
- the original
- 8x same as 'the one above'

After two runs:
- the original (z0 w0)
- 4x two straight out from any direction (z0w+-2 z+-2w0)
- 4x two out diagonal (z+-2w+-2)
- 18x nothing

02:33 So maybe...  instead of 'one half rounded up' we have
'one half rounded up squared?'

Instead of having each plane away from the center count double...
We're doing absolute value symmetry
so we're still having 4 dimensions...  wow

4 dimensions = 2 dimensional grid as cells inside 2 dimensional grid?
Yeah should work

Eighty boxes to check
26 boxes in the cube around yourself in your current space
27 boxes in the cube corresponding to yourself in next space
27 boxes in cube corresponding to yourself in previous space

11:55 Row x col is locked at nxn
Space x plane is also locked at nxn but with a different starting point (1x1)
1 Hyperspace (locked)
    1 space
        1 plane
            3 rows
                3 columns
Expand:
1 Hyperspace (locked)
    3 space (as 2 spaces)
        3 planes (as 2 planes)
            5 rows
                5 columns

Because the start grid only varies in 2 dimensions, we can reflect the output
over the z and w dimensions and just 'bounce back' from zero on every edge
when calculating neighbors
'''