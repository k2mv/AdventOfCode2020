f = open("input1201.txt", "r")

lines = f.readlines()
seenList = []

for line in lines:
    num = int(line)
    if num in seenList:
        print(num)
        print(2020 - num)
        print(num * (2020 - num))
        break
    seenList.append(2020 - num)

f.close()