f = open("input1203.txt", "r")
lines = f.readlines()
'''
31 width

'''
counter = 0
pos = 0
adv = 1
alt = 0

for line in lines:
    
    if line[pos] == '#' and alt == 0:
        counter+= 1
    if alt == 0:
        pos = (pos + adv) % 31
    alt = (alt+1) % 2


print(counter)
f.close()