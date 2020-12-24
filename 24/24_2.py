file_input = open("input1224.txt", "r")
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

def end_coordinates(input_line):
    east_axis = 0
    northeast_axis = 0
    state = 0
    '''
    0: null
    1: 'n' read, waiting for following 'w'/'e'
    2: 's' read, waiting for following 'w'/'e'
    '''
    for ch in input_line:
        if state == 0:
            if ch == 'e':
                east_axis += 1
            elif ch == 'w':
                east_axis -= 1
            elif ch == 'n':
                state = 1
            elif ch == 's':
                state = 2
        elif state == 1: # 'n'
            if ch == 'e':
                northeast_axis += 1
                state = 0
            elif ch == 'w':
                east_axis -= 1
                northeast_axis += 1
                state = 0
        elif state == 2: # 's'
            if ch == 'e':
                east_axis += 1
                northeast_axis -= 1
                state = 0
            elif ch == 'w':
                northeast_axis -= 1
                state = 0
    print(f'Coordinates: E {east_axis}, NE {northeast_axis}')
    return (east_axis, northeast_axis)

def iterate_tiles(flipped_tiles):
    new_flipped_tiles = []
    black_tiles = {}
    white_tiles = {}
    directions = ((1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1))
    for b_tile in flipped_tiles:
        black_tiles[b_tile] = 0
    for b_tile in flipped_tiles:
        e = b_tile[0]
        ne = b_tile[1]
        for d in directions:
            de, dne = d[0], d[1]
            target_tile = (e+de, ne+dne)
            if target_tile in black_tiles.keys():
                black_tiles[target_tile] += 1
            elif target_tile in white_tiles.keys():
                white_tiles[target_tile] += 1
            else:
                white_tiles[target_tile] = 1
    for bt in black_tiles.keys():
        if black_tiles[bt] == 1 or black_tiles[bt] == 2:
            new_flipped_tiles.append(bt)
    for wt in white_tiles.keys():
        if white_tiles[wt] == 2:
            new_flipped_tiles.append(wt)
    return new_flipped_tiles


flipped_tiles = []
#inp = process_input(lines)
for input_line in lines:
    tile_to_flip = end_coordinates(input_line)
    if tile_to_flip in flipped_tiles:
        flipped_tiles.remove(tile_to_flip)
    else:
        flipped_tiles.append(tile_to_flip)

print(len(flipped_tiles))

for d in range(100):
    flipped_tiles = iterate_tiles(flipped_tiles)
    print(f'Day {d+1}: {len(flipped_tiles)}')

#print(len(flipped_tiles))


file_input.close()

'''
SCRATCH PAD RIGHT HERE

Hex grid

E SE SW W NW NE

So this means we can simulate the field with a square grid with assumed offsets
based on odd/even rows?

'Slanted axis' coordinate system

NE is +1 on 'y axis'
E is +1 on 'x axis'

Part 2

Keeping track of adjacent tiles is harder than keeping track of
only the ones that are flipped

Feels suspiciously like the conway cubes problem, can we get away with
just automatically enlarging the field every round?

For each black tile, calculate the 6 surrounding tiles and:
- if it's white, put it in the list of white tiles and increment a counter
of 'black tiles adjacent'
- if it's black, increment a counter of 'black tiles adjacent' as well
'''