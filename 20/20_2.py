file_input = open("input1220.txt", "r")
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
    tiles = []
    tile_data = []
    internal_line = 0
    for l in lines:
        if internal_line == 0:
            asdf = l.split()
            tile_num = int(asdf[1][:-1])
            tile_grid = []
        elif internal_line >= 1 and internal_line <= 10:
            tile_grid.append(l.strip())
        elif internal_line == 11:
            tile_data = [tile_num, tile_grid]
            tiles.append(tile_data)
        internal_line = (internal_line + 1) % 12
    if internal_line == 11:
        tile_data = [tile_num, tile_grid]
        tiles.append(tile_data)
    for t in tiles:
        # scan edges clockwise
        tile_grid = t[1]
        edges = []
        buffer = ''
        edges.append(tile_grid[0]) # north side
        for line in tile_grid:
            buffer = buffer + line[-1]
        edges.append(buffer) # east side
        buffer = list(tile_grid[-1])
        buffer.reverse()
        buffer = ''.join(buffer)
        edges.append(buffer) # south side
        buffer = []
        for line in tile_grid:
            buffer.append(line[0])
        buffer.reverse()
        buffer = ''.join(buffer)
        edges.append(buffer) # west side
        t.append(edges)

    return tiles

def find_corners(tiles):
    corners = (3061, 3779, 3329, 2789)
    for tile in tiles:
        this_tile_num = tile[0]
        edges = tile[2]
        match_count = 0
        for e in range(len(edges)):
            target_edge1 = edges[e]
            buffer = list(edges[e])
            buffer.reverse()
            buffer = ''.join(buffer)
            target_edge2 = buffer
            for tile2 in tiles:
                tile2_num = tile2[0]
                edges2 = tile2[2]
                if tile2_num != this_tile_num:
                    for e2 in range(4):
                        if edges2[e2] == target_edge1:
                            if this_tile_num in corners:
                                print(f'Tile {this_tile_num} edge {e} / Tile {tile2_num} edge {e2}')
                            match_count += 1
                        elif edges2[e2] == target_edge2:
                            if this_tile_num in corners:
                                print(f'Tile {this_tile_num} edge {e} / Tile {tile2_num} edge {e2} via flip')
                            match_count += 1
        if match_count == 2:
            print(f'Tile {this_tile_num}: {match_count} edges matched')

def build_edge(tiles, tile_get, this_edge):
    # pick arbitrary corner to start, 2789/1 (east, noflip)
    #tile_get = 1187
    #tiles = []
    this_tile = None
    for t in tiles:
        if t[0] == tile_get:
            this_tile = t
            break
    #this_edge = 3
    live_edge = this_tile[2][this_edge]
    temp = list(live_edge)
    temp.reverse()
    live_edge_reverse = ''.join(temp)
    next_tile = None
    next_edge_to_match = None
    for tile2 in tiles:
        tile2_num = tile2[0]
        edges2 = tile2[2]
        if tile2_num != tile_get:
            for e2 in range(4):
                if edges2[e2] == live_edge:
                    #print(f'Tile {this_tile[0]} edge {this_edge} matches tile {tile2_num} edge {e2}')
                    next_tile = tile2_num
                    next_edge_to_match = (e2 + 2) % 4
                elif edges2[e2] == live_edge_reverse:
                    #print(f'Tile {this_tile[0]} edge {this_edge} matches tile {tile2_num} edge {e2} reverse')
                    next_tile = tile2_num
                    next_edge_to_match = (e2 + 2) % 4
    return next_tile, next_edge_to_match

def get_tile(tiles, tile_num):
    ret_tile = None
    for t in tiles:
        if t[0] == tile_num:
            ret_tile = t
            break
    return ret_tile



def build_col_orientation(tiles, tile_get, top_edge, orientation_grid):
    # going down the grid from top, getting this column tile in every row
    this_tile = get_tile(tiles, tile_get)
    this_tile_num = tile_get
    this_tile_edges = this_tile[2]
    this_coord = orientation_grid[this_tile_num][0]
    this_row = this_coord[0]
    this_col = this_coord[1]
    # match bottom live edge (opposite of top edge) with top edge of next tile
    flip_flag = orientation_grid[this_tile_num][2]
    live_edge_num = (top_edge + 2) % 4 # matches next edge if next tile is flipped from this
    live_edge = this_tile_edges[live_edge_num]
    temp = list(live_edge)
    temp.reverse()
    live_edge_reverse = ''.join(temp) # matches next edge if next tile is not flipped from this
    
    #if(flip_flag):
    #    live_edge, live_edge_reverse = live_edge_reverse, live_edge
    
    next_tile_num = None
    next_top_edge = None
    for tile2 in tiles:
        tile2_num = tile2[0]
        if tile2_num != this_tile_num:
            edges2 = tile2[2]
            for e2 in range(4):
                if edges2[e2] == live_edge_reverse:
                    #print(f'Tile {this_tile_num} edge {live_edge_num} matches tile {tile2_num} edge {e2}')
                    next_tile_num = tile2_num
                    next_top_edge = e2
                    orientation_grid[next_tile_num] = (this_row+1,this_col), e2, flip_flag
                elif edges2[e2] == live_edge:
                    #print(f'Tile {this_tile_num} edge {live_edge_num} matches tile {tile2_num} edge {e2} reverse')
                    next_tile_num = tile2_num
                    next_top_edge = e2
                    flip_flag = not flip_flag
                    orientation_grid[next_tile_num] = (this_row+1,this_col), e2, flip_flag
    return next_tile_num, next_top_edge, orientation_grid

def reverse_string(source_string):
    temp = list(source_string)
    temp.reverse()
    return ''.join(temp)

def print_tile_row(tiles, orientation_grid, row_num):
    tile_num = None
    #tile_top_edge = 
    #tile_flip_flag = 
    row_cells = []
    cells = orientation_grid.keys()
    for col in range(12):
        for cell_key in cells:
            if orientation_grid[cell_key][0][0] == row_num and orientation_grid[cell_key][0][1] == col:
                row_cells.append((cell_key, orientation_grid[cell_key]))
    for row_cell in row_cells:
        tile_num = row_cell[0]
        print_tile(tiles, tile_num)

def print_tile(tiles, tile_num):
    this_tile = get_tile(tiles, tile_num)
    tile_grid = this_tile[1]
    print(f'Tile {tile_num}:')
    for n in range(len(tile_grid)):
        print(tile_grid[n])
    print('')

def print_raw_grid(tile_grid):
    for n in range(len(tile_grid)):
        print(tile_grid[n])
    print('')

def get_tile_by_coords(tiles, orientation_grid, row, col):
    cell_keys = orientation_grid.keys()
    ret_tile_num = None
    for ck in cell_keys:
        if orientation_grid[ck][0][0] == row and orientation_grid[ck][0][1] == col:
            ret_tile_num = ck
            break
    return ret_tile_num

def print_row_with_nums(tiles, orientation_grid, row_num, row_length):
    row_grid_list = []
    for col in range(row_length):
        #print(f'adding tile at row={row_num}, col={col}')
        tile_num = get_tile_by_coords(tiles, orientation_grid, row_num, col)
        top_edge = orientation_grid[tile_num][1]
        is_flipped = orientation_grid[tile_num][2]
        add_grid = rotate_and_flip_grid(tiles, tile_num, top_edge, is_flipped)
        row_grid_list.append(add_grid)
    for grid_row in range(len(add_grid)):
        line = ''
        #print(f'grid_row = {grid_row}')
        for grid_num in range(len(row_grid_list)):
            #print(f'grid_num = {grid_num}')
            line = line + row_grid_list[grid_num][grid_row]
            line = line + ' ' # TEST!!!!!!!!!!!!!
        print(line)


def rotate_and_flip_grid(tiles, tile_num, top_edge, is_flipped):
    this_tile = get_tile(tiles, tile_num)
    grid = this_tile[1] # assume source grid comes in at top edge 0
    new_grid = grid
    if top_edge == 1:
        new_grid = []
        for col in range(len(grid)):
            new_row = ''
            for row in range(len(grid)):
                ch = grid[row][col]
                new_row = new_row + ch
            #new_row = reverse_string(new_row)
            new_grid.append(new_row)
        new_grid.reverse()
        grid = new_grid
    if top_edge == 2:
        new_grid = []
        for n in range(len(grid)):
            new_grid.append(reverse_string(grid[n]))
        new_grid.reverse()
        grid = new_grid
    if top_edge == 3:
        new_grid = []
        for col in range(len(grid)):
            new_row = ''
            for row in range(len(grid)):
                ch = grid[row][col]
                new_row = new_row + ch
            new_row = reverse_string(new_row)
            new_grid.append(new_row)
        grid = new_grid
    if is_flipped:
        new_grid = []
        for n in range(len(grid)):
            new_grid.append(reverse_string(grid[n]))
        grid = new_grid
    return new_grid

def assemble_master_image(tiles, orientation_grid, row_length, tile_length):
    master_image = []
    for row_num in range(row_length): # orientation grid row
        row_grid_list = []
        for col in range(row_length): # orientation grid column
            tile_num = get_tile_by_coords(tiles, orientation_grid, row_num, col)
            top_edge = orientation_grid[tile_num][1]
            is_flipped = orientation_grid[tile_num][2]
            add_grid = rotate_and_flip_grid(tiles, tile_num, top_edge, is_flipped)
            row_grid_list.append(add_grid) # add 12 grids to row_grid_list
        for grid_row in range(tile_length): # for each "row of a single tile"
            line = ''
            for grid_num in range(len(row_grid_list)): # for each "tile in row list"
                '''
                if grid_num == 0:
                    line = line + row_grid_list[grid_num][grid_row]
                else:
                    line = line + row_grid_list[grid_num][grid_row][1:]
                '''
                # append line grid_row from grid_list member #grid_num
                line = line + row_grid_list[grid_num][grid_row][1:-1]
            if grid_row > 0 and grid_row < 9:
                master_image.append(line)
    return master_image
'''
sea monster:
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

(0,18), 
(1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19), 
(2,1), (2,4), (2,7), (2,10), (2,13), (2,16)
'''
def check_for_sea_monster(original_master_image, reduced_master_image_in, row, col):
    #master_image_copy = master_image.copy()
    reduced_master_image = reduced_master_image_in.copy()
    max_row = len(original_master_image) - 1
    max_col = len(original_master_image[0]) - 1
    count = 0
    coords = [(0,18), (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19), (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)]
    if row + 2 <= max_row and col + 19 <= max_col:
        for coord in coords:
            row_offset = coord[0]
            col_offset = coord[1]
            if original_master_image[row+row_offset][col+col_offset] == '#':
                count += 1
        if count == len(coords):
            print(f'Sea monster starting at ({row}, {col})')
            for coord in coords:
                row_offset = coord[0]
                col_offset = coord[1]
                asdf = reduced_master_image[row+row_offset]
                #print(f'Old row: {asdf}')
                asdf = list(asdf)
                asdf[col+col_offset] = 'O'
                asdf = ''.join(asdf)
                reduced_master_image[row+row_offset] = asdf
                #print(f'New row: {asdf}')
    return original_master_image, reduced_master_image

def rotate_master_grid_cw(master_grid):
    new_grid = []
    for col in range(len(master_grid[0])):
        new_row = ''
        for row in range(len(master_grid)):
            ch = master_grid[row][col]
            new_row = new_row + ch
        new_row = reverse_string(new_row)
        new_grid.append(new_row)
    return new_grid

def flip_master_grid(master_grid):
    new_grid = []
    for row in range(len(master_grid)):
        temp = reverse_string(master_grid[row])
        new_grid.append(temp)
    return new_grid

def count_pounds(master_grid):
    count = 0
    for row in range(len(master_grid)):
        count += master_grid[row].count('#')
    return count


tiles = process_input(lines)

'''
tile fields:
0: tile number
1: grid (2 dimensional list of n-length strings)
2: edges (four n-length strings clockwise from top when unflipped)
'''

#print(len(tiles))
#print(tiles[0])
#print(tiles[1])
#find_corners(tiles)
#tile_get, this_edge = 2789, 2
#while tile_get is not None:
#    tile_get, this_edge = build_edge(tiles, tile_get, this_edge)

'''
orientation_grid cells:
key: tile_num
value: tuple
    0: coordinate: (row, col) i.e. (y, x) with y going down and x going right
        0 0: row
        0 1: col
    1: upward_edge: int
    2: flipped: bool
'''

orientation_grid = {}
orientation_grid[2789] = ((0,0), 0, False)
orientation_grid[1187] = ((0,1), 0, True)
orientation_grid[2591] = ((0,2), 0, False)
orientation_grid[1747] = ((0,3), 2, True)
orientation_grid[1667] = ((0,4), 3, False)
orientation_grid[2039] = ((0,5), 2, False)
orientation_grid[1931] = ((0,6), 2, True)
orientation_grid[1453] = ((0,7), 3, True)
orientation_grid[2351] = ((0,8), 2, False)
orientation_grid[2503] = ((0,9), 2, True)
orientation_grid[3853] = ((0,10), 3, False)
orientation_grid[3329] = ((0,11), 3, True)
next_tile_num = 2789
next_top_edge = 0

top_tiles = [(2789,0),(1187,0),(2591,0),(1747,2),(1667,3),(2039,2),(1931,2),(1453,3),(2351,2),(2503,2),(3853,3),(3329,3)]
for tt in range(len(top_tiles)):
    next_tile_num = top_tiles[tt][0]
    next_top_edge = top_tiles[tt][1]
    while next_tile_num is not None:
        #print(f'next_tile_num={next_tile_num} next_top_edge={next_top_edge}')
        next_tile_num, next_top_edge, orientation_grid = build_col_orientation(tiles, next_tile_num, next_top_edge, orientation_grid)

# def build_col_orientation(tiles, tile_get, top_edge, orientation_grid):


for n in range(12):
    print_row_with_nums(tiles, orientation_grid, n, 12)
    print('') # TEST!!!!!!!

master_image = assemble_master_image(tiles, orientation_grid, 12, 10)
for line in master_image:
    print(line)
print('')
master_image_2 = rotate_master_grid_cw(master_image)
#master_image_2 = flip_master_grid(master_image)
for line in master_image_2:
    print(line)

num_pounds = count_pounds(master_image_2)
print(num_pounds)
master_image = rotate_master_grid_cw(master_image)
reduced_master_image = master_image.copy()
for r in range(len(master_image)):
    for c in range(len(master_image[0])):
        master_image, reduced_master_image = check_for_sea_monster(master_image, reduced_master_image, r, c)

for line in reduced_master_image:
    print(line)

num_pounds = count_pounds(reduced_master_image)
print(num_pounds)
'''
for turn in range(4):
    print(f'Unflipped master image, rotation {turn}')
    for r in range(len(master_image)):
        for c in range(len(master_image[0])):
            #print(f'Check: ({r}, {c})')
            check_for_sea_monster(master_image, r, c)
    master_image = rotate_master_grid_cw(master_image)
master_image = flip_master_grid(master_image)
for turn in range(4):
    print(f'Flipped master image, rotation {turn}')
    for r in range(len(master_image)):
        for c in range(len(master_image[0])):
            #print(f'Check: ({r}, {c})')
            check_for_sea_monster(master_image, r, c)
    master_image = rotate_master_grid_cw(master_image)
'''
file_input.close()

'''
SCRATCH PAD RIGHT HERE

10x10 tiles, 10 'bits' per side
Say '.' = 0 and '#' = 1

I'm assuming all we need is the edges
Edges overlap at the corners
Need to make a convention; let's say
"Reading left to right when viewing from the center of the tile"

Note that in order for two tiles to match the pattern must be reversed
So the match of 1110010101 would be 1010100111 on the other side

Problem says the final image is a giant square
Problem says the outer edges will not align with any other tiles

To do:
- Can we just... find the four tiles with exactly two sides that
don't match anything? :thinking:

Tiles have 4 digit IDs
12 line cycle

144 tiles = 12x12 square

Tiles generated and matching algo written, but...
didn't realize that tiles could also be flipped D:

There are 1024 possible ways to construct an edge with 10 spaces
144 x 4 x 2 = 1152 (probably  less due to symmetry etc) possible
edges including flips

Part 2:

Tile 3061: 2 edges matched
Tile 3779: 2 edges matched
Tile 3329: 2 edges matched
Tile 2789: 2 edges matched

Those are the corners, that's all I really figured out, I should
likely actually try to see how to actually assemble the image

How many squares have 3 matches (edge tiles)?
answer: 40
Good!  With 4 sides and 4 endcaps in a 12x12 grid, that's exactly
the number we need

Next: Assemble the border of the image from the 4 corners and 40 edges

Sub-tasks:
- Find out which two adjacent sides of each corner are 'live' (matchable)
- Match a row of 10 edge tiles to a 'live' corner (in right orientation)
- 'Cap' the row with the 'live' edge of another corner
- Repeat until done

Interestingly the image could be constituted in either flipped or non-flipped
orientation, because no tile has an enforced right-side-up state.
(Does that affect the answer?)
answer: Yes; you may need to rotate/flip to be able to find sea monsters

Tile 3061 edge 0 / Tile 2897 edge 0
Tile 3061 edge 3 / Tile 1783 edge 3 via flip
Tile 3061: 2 edges matched
Tile 3779 edge 1 / Tile 2521 edge 1
Tile 3779 edge 2 / Tile 3541 edge 0 via flip
Tile 3779: 2 edges matched
Tile 3329 edge 0 / Tile 3853 edge 0
Tile 3329 edge 1 / Tile 1289 edge 0 via flip
Tile 3329: 2 edges matched
Tile 2789 edge 1 / Tile 1187 edge 1
Tile 2789 edge 2 / Tile 3761 edge 2 via flip
Tile 2789: 2 edges matched

Noticing that there's a perfect number of matches even accounting for
flips across all sides - so we just need to find a single match

Tile 2789 edge 1 matches tile 1187 edge 1
Tile 1187 edge 3 matches tile 2591 edge 3
Tile 2591 edge 1 matches tile 1747 edge 3
Tile 1747 edge 1 matches tile 1667 edge 2
Tile 1667 edge 0 matches tile 2039 edge 1 reverse
Tile 2039 edge 3 matches tile 1931 edge 3
Tile 1931 edge 1 matches tile 1453 edge 0 reverse
Tile 1453 edge 2 matches tile 2351 edge 1
Tile 2351 edge 3 matches tile 2503 edge 3
Tile 2503 edge 1 matches tile 3853 edge 2
Tile 3853 edge 0 matches tile 3329 edge 0

3329 has live edges 0 and 1 so next live edge is 3329 edge 1

Tile 3329 edge 1 matches tile 1289 edge 0 reverse
Tile 1289 edge 2 matches tile 1889 edge 0
Tile 1889 edge 2 matches tile 2857 edge 2 reverse
Tile 2857 edge 0 matches tile 3191 edge 1
Tile 3191 edge 3 matches tile 2441 edge 1 reverse
Tile 2441 edge 3 matches tile 1777 edge 0
Tile 1777 edge 2 matches tile 3547 edge 0 reverse
Tile 3547 edge 2 matches tile 1093 edge 3 reverse
Tile 1093 edge 1 matches tile 2239 edge 3
Tile 2239 edge 1 matches tile 2521 edge 3
Tile 2521 edge 1 matches tile 3779 edge 1

3779 has live edge 1 and 2 so next live edge is 3779 edge 2

Tile 3779 edge 2 matches tile 3541 edge 0 reverse
Tile 3541 edge 2 matches tile 2551 edge 1
Tile 2551 edge 3 matches tile 1297 edge 3 reverse
Tile 1297 edge 1 matches tile 2843 edge 1 reverse
Tile 2843 edge 3 matches tile 1657 edge 3
Tile 1657 edge 1 matches tile 3041 edge 2 reverse
Tile 3041 edge 0 matches tile 3371 edge 1 reverse
Tile 3371 edge 3 matches tile 3631 edge 0
Tile 3631 edge 2 matches tile 2221 edge 0
Tile 2221 edge 2 matches tile 1783 edge 1 reverse
Tile 1783 edge 3 matches tile 3061 edge 3 reverse

3061 has live edges 0 and 3 so next live edge is 3061 edge 0
and final match should be with the last unmatched edge which is
...2789 edge 2

Tile 3061 edge 0 matches tile 2897 edge 0
Tile 2897 edge 2 matches tile 1217 edge 0 reverse
Tile 1217 edge 2 matches tile 1979 edge 0 reverse
Tile 1979 edge 2 matches tile 2003 edge 3
Tile 2003 edge 1 matches tile 3067 edge 1
Tile 3067 edge 3 matches tile 1237 edge 2
Tile 1237 edge 0 matches tile 3389 edge 0 reverse
Tile 3389 edge 2 matches tile 2647 edge 1
Tile 2647 edge 3 matches tile 1597 edge 2
Tile 1597 edge 0 matches tile 3761 edge 0
Tile 3761 edge 2 matches tile 2789 edge 2 reverse

Paydirt!

Now, next is to assign each tile an orientation, based on:
2789 with 0 north, 1 east, and 2 south in the upper left corner (0,0)
Need to mark:
- coordinate in the grid up to (11,11)
- which edge (source side) faces up
- whether tile is flipped from source

Oh heck: Flipping from source also reverses the placement of each edge
going around the tile, so edge 1 would be clockwise of edge 0 in
'unflipped', while edge 1 would be counter-clockwise of edge 0 in
'flipped'.  Hngggggg

02:07: Going to bed now, but I think we have a good place to start.

To do after sleeping:
- Either find out how to assign (coord, up_edge, flipped) to each tile
    - or do it by hand
- Stitch together the master image
- Methods to flip/rotate
- Method to find sea monsters
- And that should be it

Idea: if a matching tile matches over a flip, toggle a flag
The just-matched tile will get flagged as reverse and have the orientation assigned
accordingly
The next match will keep the flip flag if not matching over a reverse
> Check: Did I program straight match (reverse of edge) or reverse match (edge)
into the edge matcher?
and toggle the flip flag again (to 'unflipped' if matching over a reverse if reversed)

17:52 Stuck with an answer that seems to be right but is not accepted
After removing borders and connecting tiles, we have a 96x96 grid (12 x 8)
There are 2125 # in the 96x96 grid, and 15 sea monsters in the orientation that has them
Sea monsters are 18 # that are to be excluded, x 15 = 270
Even accounting for possible overlap (I didn't see any), that takes the number down
to 1855, but that isn't accepted by the website

18:13 Have the feeling I'm going to be locked out if I keep entering 1855 over and over
Locked out for 10 minutes (18:23)

Sea monster starting at (1, 10)
Sea monster starting at (2, 53)
Sea monster starting at (25, 5)
Sea monster starting at (30, 9)
Sea monster starting at (34, 66)
Sea monster starting at (35, 1)
Sea monster starting at (37, 40)
Sea monster starting at (42, 32)
Sea monster starting at (46, 6)
Sea monster starting at (49, 65)
Sea monster starting at (51, 15)
Sea monster starting at (57, 10)
Sea monster starting at (59, 33)
Sea monster starting at (61, 56)
Sea monster starting at (76, 16)
Sea monster starting at (78, 71)
Sea monster starting at (83, 69)
Sea monster starting at (89, 10)

The master image is the right size and seems to correspond to the correct format
of joining the middle 8x8 grid of each tile when placed in the proper position

There is exactly one rotation that yields any sea monster sightings

18 sea monsters are reported in this orientation, none of them overlap

Subtracting the sea monster # from the # in the original (calculated 2 ways now)
yields 1855

But 1855 is not accepted as the right answer

What's wrong?

After peeking at solution images:
Noticed that my grid is actually not aligned on all edges - many in the interior are flipped

Either something in build_col_orientation is broken or the big grid builder is broken
Or both

'''