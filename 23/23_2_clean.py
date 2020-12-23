def setup_million():
    next_cups = []
    for n in range(1000000):
        next_cups.append((n+1) % 1000000)
    # hard code the first few cup 'nexts'
    # zero index the input: 643719258 -> 532608147 [9 10...]
    next_cups[999999] = 5
    next_cups[0] = 8
    next_cups[1] = 4
    next_cups[2] = 6
    next_cups[3] = 2
    next_cups[4] = 7
    next_cups[5] = 3
    next_cups[6] = 0
    next_cups[7] = 9
    next_cups[8] = 1
    return next_cups

def move2(next_cups, index):
    index_plus_1 = next_cups[index]
    index_plus_2 = next_cups[index_plus_1]
    index_plus_3 = next_cups[index_plus_2]
    index_plus_4 = next_cups[index_plus_3]
    target = (index - 1) % 1000000
    while target in (index_plus_1, index_plus_2, index_plus_3):
        target = (target - 1) % 1000000
    next_cups[index_plus_3] = next_cups[target]
    next_cups[target] = index_plus_1
    next_cups[index] = index_plus_4
    return next_cups, index_plus_4

next_cups = setup_million()
index = 5
for _ in range(10000000):
    next_cups, index = move2(next_cups, index)
print(f'1 {next_cups[0]+1} {next_cups[next_cups[0]]+1} = {(next_cups[0]+1) * (next_cups[next_cups[0]]+1)}')
