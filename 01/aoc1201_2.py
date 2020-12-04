f = open("input1201.txt", "r")

lines = f.readlines()
smallList = []
twoSmallDict = {}
bigList = []
seenList = []

for line in lines:
    num = int(line)
    if num < 1000:
        smallList.append(num)
    else:
        bigList.append(num)


for a in range(len(smallList) - 1):
    for b in range(a + 1, len(smallList)):
        sum = smallList[a] + smallList[b]
        if sum not in twoSmallDict.keys():
            twoSmallDict[sum] = (smallList[a], smallList[b])

#for c in twoSmallDict.keys():
#    print(str(c) + ' ' +  str(twoSmallDict[c][0]) + ' ' + str(twoSmallDict[c][1]))

for big in bigList:
    small_candidate = 2020 - big;
    if small_candidate in twoSmallDict.keys():
        print(str(big) + ' ' + str(twoSmallDict[small_candidate][0]) + ' ' + str(twoSmallDict[small_candidate][1]))
        print (big * twoSmallDict[small_candidate][0] * twoSmallDict[small_candidate][1])
        break 

f.close()