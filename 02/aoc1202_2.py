f = open("input1202.txt", "r")
lines = f.readlines()

valid_count = 0

for line in lines:
    split_line = line.split()
    minmax = split_line[0].split('-')
    pos1 = int(minmax[0]) - 1
    pos2 = int(minmax[1]) - 1
    #print(min + ' ' + max)
    char = split_line[1][0]
    #print(char)
    test_string = split_line[2]
    #print(test_string)
    '''
    char_count = 0
    for ch in test_string:
        if ch == char:
            char_count += 1
    if char_count >= min and char_count <= max:
        print('Valid')
        valid_count += 1
    else:
        print('Not valid')
    '''
    # NOTE: bool != bool is XOR
    if (test_string[pos1] == char) != (test_string[pos2] == char):
        print('Valid')
        valid_count += 1
    else:
        print ('Not valid')
    

print('valid_count = ' + str(valid_count))
    

f.close()