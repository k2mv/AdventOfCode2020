f = open("input1204.txt", "r")
lines = f.readlines()

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''


counter = 0
byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
# cid

def passValid(byr, iyr, eyr, hgt, hcl, ecl, pid):
    print(byr, iyr, eyr, hgt, hcl, ecl, pid)
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        return 1
    return 0

for line in lines:
    pass
    if line == '\n':
        print('empty line')
        counter += passValid(byr, iyr, eyr, hgt, hcl, ecl, pid)
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
    else:
        split_line = line.split()
        for things in split_line:
            crap = things.split(':')
            print(crap)
            if crap[0] == 'byr':
                byr = True
            elif crap[0] == 'iyr':
                iyr = True
            elif crap[0] == 'eyr':
                eyr = True
            elif crap[0] == 'hgt':
                hgt = True
            elif crap[0] == 'hct':
                hct = True
            elif crap[0] == 'hcl':
                hcl = True
            elif crap[0] == 'ecl':
                ecl = True
            elif crap[0] == 'pid':
                pid = True
counter += passValid(byr, iyr, eyr, hgt, hcl, ecl, pid) # clean up the last one


print(counter)

f.close()