file_input = open("input1217.txt", "r")
#file_input = open("test_input.txt", "r")
lines = file_input.readlines()

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

def eval_hypercell(active, hyperspace, hyperwidth, width, spa, pla, row, col):
    neighbors = 0
    if spa != len(hyperspace) - 1:
        neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, 1, True)
    if spa == 0:
        neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, 1, True)
    else:
        neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, -1, True)
    neighbors += eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, 0, False)
    if active == 1 and (neighbors < 2 or neighbors > 3):
        active = 0
    elif active == 0 and neighbors == 3:
        active = 1
    return active

def eval_flat_27(hyperspace, hyperwidth, width, spa, pla, row, col, spa_offset, check_center):
    neighbors = 0
    for p in (pla-1, pla, pla+1):
        if p >= 0 and p < hyperwidth:
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
    for spa in range(hyperwidth):
        for pla in range(hyperwidth):
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
        for r in range(width):
            for c in range(width):
                if hyperspace[sp][pl][r][c] == 1:
                    accum += hyperspace[sp][pl][r][c] * multiplier
    return accum

def count_hypercubes(hyperspace):
    accum = 0
    for sp in range(len(hyperspace)):
        accum += count_cubes(hyperspace, sp)
    return accum

hyperspace = process_input(lines)
hyperspace = [[hyperspace[0][0], new_zero_plane(hyperspace[0][0])]]
hyperspace = [hyperspace[0], new_zero_space(hyperspace[0])]

runtime = 6
iter = 0
while iter < runtime:
    iter += 1
    hyperspace = expand_hyperspace(hyperspace)
    hyperspace = process_hyperspace(hyperspace)
print(count_hypercubes(hyperspace))

file_input.close()