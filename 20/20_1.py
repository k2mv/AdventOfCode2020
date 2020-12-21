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
                    for e2 in range(len(edges2)):
                        if edges2[e2] == target_edge1:
                            #print(f'Tile {this_tile_num} edge {e} / Tile {tile2_num} edge {e2}')
                            match_count += 1
                        elif edges2[e2] == target_edge2:
                            #print(f'Tile {this_tile_num} edge {e} / Tile {tile2_num} edge {e2} via flip')
                            match_count += 1
        if match_count < 3:
            print(f'Tile {this_tile_num}: {match_count} edges matched')

tiles = process_input(lines)

print(len(tiles))
print(tiles[0])
print(tiles[1])
find_corners(tiles)

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

'''