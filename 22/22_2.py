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

def past_hands_string(deck1, deck2):
    ret = ''
    for c in deck1:
        ret = ret + str(c) + 'A'
    for c in deck2:
        ret = ret + str(c) + 'B'
    return ret

def play_recursive(deck1, deck2):
    past_hands = []
    winner = None
    card1 = None
    card2 = None
    score = 0
    #print(f'Deck 1: {deck1}')
    #print(f'Deck 2: {deck2}')
    while winner is None:
        this_state = past_hands_string(deck1, deck2)
        if this_state in past_hands:
            #print(f'BOOTED FROM LOOP len(past_hands) = {len(past_hands)}')
            winner = 1
            score = calc_score(deck1)
        else:
            #print(f'Deck 1: {deck1}')
            #print(f'Deck 2: {deck2}')
            past_hands.append(past_hands_string(deck1, deck2))
            card1 = deck1.pop(0)
            card2 = deck2.pop(0)
            #print(f'P1 plays {card1} ({len(deck1)}), P2 plays {card2} ({len(deck2)})')
            if len(deck1) < card1 or len(deck2) < card2:
                if card1 > card2:
                    #print('P1 wins hand')
                    deck1.append(card1)
                    deck1.append(card2)
                else:
                    #print('P2 wins hand')
                    deck2.append(card2)
                    deck2.append(card1)
                if len(deck1) == 0:
                    winner = 2
                    score = calc_score(deck2)
                elif len(deck2) == 0:
                    winner = 1
                    score = calc_score(deck2)
            else:
                #print('Recursive call >>>')
                sub_winner, _ = play_recursive(deck1[:card1], deck2[:card2])
                if sub_winner == 1:
                    #print('P1 wins recursive call')
                    deck1.append(card1)
                    deck1.append(card2)
                else:
                    #print('P2 wins recursive call')
                    deck2.append(card2)
                    deck2.append(card1)
            if len(deck1) == 0:
                #print('P2 wins game!')
                winner = 2
                score = calc_score(deck2)
            elif len(deck2) == 0:
                #print('P1 wins game!')
                winner = 1
                score = calc_score(deck1)
    return winner, score


deck1, deck2 = process_input(lines)
deck1_win = False
deck2_win = False
past_hands = []

print(deck1)
print(deck2)

winner, score = play_recursive(deck1,deck2)

print(f'Score = {score}')

file_input.close()

'''
SCRATCH PAD RIGHT HERE

01:08 Having trouble understanding how to match current state of the hands
versus saved past states of hands to know when to reject and award victory to P1



'''