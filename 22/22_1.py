file_input = open("input1222.txt", "r")
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
    deck1, deck2 = [], []
    phase = 0
    for l in lines:
        if phase == 0:
            if l != '\n':
                if l.strip().isnumeric():
                    temp = l.strip()
                    deck1.append(int(temp))
            else:
                phase = 1
        elif phase == 1:
            if l != '\n':
                if l.strip().isnumeric():
                    temp = l.strip()
                    deck2.append(int(temp))
    return deck1, deck2

def play_hand(deck1, deck2):

    if deck1[0] > deck2[0]:
        temp = deck1.pop(0)
        deck1.append(temp)
        temp = deck2.pop(0)
        deck1.append(temp)
    else:
        temp = deck2.pop(0)
        deck2.append(temp)
        temp = deck1.pop(0)
        deck2.append(temp)
    return deck1, deck2

def calc_score(deck):
    score = 0
    max_mult = len(deck)
    for card in range(len(deck)):
        score += deck[card] * (max_mult - card)
    return score

deck1, deck2 = process_input(lines)

print(deck1)
print(deck2)

while len(deck1) > 0 and len(deck2) > 0:
    play_hand(deck1,deck2)

print(deck1)
print(deck2)

if len(deck1) == 0:
    score = calc_score(deck2)
else:
    score = calc_score(deck1)

print(f'Score = {score}')

file_input.close()

'''
SCRATCH PAD RIGHT HERE


'''