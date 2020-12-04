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
            #print(crap)
            if crap[0] == 'byr':
                #byr = True
                year = int(crap[1])
                if year >= 1920 and year <= 2002:
                    byr = True
            elif crap[0] == 'iyr':
                #iyr = True
                year = int(crap[1])
                if year >= 2010 and year <= 2020:
                    iyr = True
            elif crap[0] == 'eyr':
                #eyr = True
                year = int(crap[1])
                if year >= 2020 and year <= 2030:
                    eyr = True
            elif crap[0] == 'hgt':
                #hgt = True
                suff = crap[1][-2:]
                numb = crap[1][:-2]
                #print('suff = ' + suff + ', numb = ' + numb)
                if (suff == 'cm' and int(numb) >= 150 and int(numb) <= 193):
                    hgt = True
                elif (suff == 'in' and int(numb) >= 59 and int(numb) <= 76):
                    hgt = True
            elif crap[0] == 'hct':
                hct = True
            elif crap[0] == 'hcl':
                #hcl = True
                test = True
                #print(crap)
                if crap[1][0] == '#' and len(crap[1]) == 7:
                    for n in range(6):
                        ch = crap[1][n+1]
                        ordch = ord(ch)
                        a = ord('a')
                        ff = ord('f')
                        zero = ord('0')
                        nine = ord('9')
                        if (ordch >= a and ordch <= ff) or (ordch >= zero and ordch <= nine):
                            pass
                        else:
                            test = False
                            print ('#\n#\n#\n#\n#\n#\n#\n###hcl false')
                    hcl = test
                    #print('hcl = ' + str(hcl))
            elif crap[0] == 'ecl':
                #ecl = True
                if crap[1] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    ecl = True
            elif crap[0] == 'pid':
                if len(crap[1]) == 9 and int(crap[1]) <= 999999999:
                    pid = True
                #pid = True
counter += passValid(byr, iyr, eyr, hgt, hcl, ecl, pid) # clean up the last one


print(counter)

f.close()