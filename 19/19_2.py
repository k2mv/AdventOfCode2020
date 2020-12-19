#file_input = open("input1219.txt", "r")
file_input = open("input1219_2.txt", "r")
#file_input = open("test_input2.txt", "r")
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
    total = 0
    rule_dict = {}
    chunk_dict = {}
    phase = 0
    for l in lines:
        chunk = l.split()
        if phase == 0:
            if l != '\n':
                rules_buffer = []
                buffer = []
                index = (int(chunk[0][:-1]))
                for n in range(1,len(chunk)):
                    if chunk[n].isnumeric():
                        buffer.append(int(chunk[n]))
                    elif chunk[n] == '|':
                        rules_buffer.append(buffer)
                        buffer = []
                    elif chunk[n].startswith('"'):
                        buffer = chunk[n][1]
                rules_buffer.append(buffer)
                rule_dict[index] = rules_buffer
            else:
                phase = 1
                #print(rule_dict)
                chunk_dict = build_chunk_dict(rule_dict)
                print(chunk_dict)
        elif phase == 1:
            message = chunk[0]
            if chunkwise_satisfy(message, chunk_dict):
                total += 1

            '''
            if satisfy(rule_dict, 0, message, '') == (True, ''):
                print('hit')
                total += 1
            else:
                print('miss')
                pass
            '''
            
            '''
            for n in range(1, len(message) - 1):
                eight_half = message[:-n]
                eleven_half = message[-n:]
                eight_result = satisfy(rule_dict, 8, eight_half, '') == (True, '')
                eleven_result = satisfy(rule_dict, 11, eleven_half, '') == (True, '')
                if eight_result and eleven_result:
                    print('hit')
                    total += 1
                    break
            if not (eight_result and eleven_result):
                print('miss')
                pass
                '''
    return total

def build_chunk_dict(rule_dict):
    chunk_dict = {}
    forty_two = False
    thirty_one = False
    for n in range(256): # hard coded for apparent chunk length of 8
        bin = f'{n:08b}'
        check_str = ''
        for ch in bin:
            if ch == '0':
                check_str = check_str + 'a'
            elif ch == '1':
                check_str = check_str + 'b'
        forty_two, _ = satisfy(rule_dict, 42, check_str, '')
        thirty_one, _ = satisfy(rule_dict, 31, check_str, '')
        if forty_two and not thirty_one:
            chunk_dict[check_str] = 42
        elif thirty_one and not forty_two:
            chunk_dict[check_str] = 31
    return chunk_dict

def chunkwise_satisfy(message, chunk_dict):
    accept = False
    sequence = []
    forty_two = 0
    thirty_one = 0
    phase = 0
    num_chunks = len(message) // 8
    if num_chunks >= 3:
        for n in range(num_chunks):
            chunk = message[n*8:(n*8)+8]
            if chunk in chunk_dict.keys():
                sequence.append(chunk_dict[chunk])
    print(sequence)
    for n in range(len(sequence)):
        if phase == 0:
            if sequence[n] == 42:
                forty_two += 1
                phase = 1
            else:
                phase = 4
        elif phase == 1:
            if sequence[n] == 42:
                forty_two += 1
                phase = 2
            else:
                phase = 4
        elif phase == 2:
            if sequence[n] == 42:
                forty_two += 1
            elif sequence[n] == 31:
                thirty_one += 1
                phase = 3
        elif phase == 3:
            if sequence[n] == 42:
                phase = 4 # There is no phase 4
            elif sequence[n] == 31:
                thirty_one += 1
    print(f'phase={phase}, thirty_one={thirty_one}, forty_two={forty_two}')
    accept = phase == 3 and thirty_one < forty_two
    return accept




def satisfy(rule_dict, rule_num, message, previous_8):
    satisfied = False
    remaining_message = message
    requirements = rule_dict[rule_num]
    if remaining_message == '':
        return False, ''
    if requirements[0] == 'a' or requirements[0] == 'b':
        if message[0] == requirements[0]:
            satisfied = True
            #print(f'Accept rule {rule_num}:\'{requirements[0]}\'')
            remaining_message = message[1:]
        else:
            #print(f'Reject rule {rule_num}: \'{message[0]}\' != \'{requirements[0]}\'')
           pass
    else:
        saved_state = remaining_message
        for rule_list in requirements:
            rule_list_status = True
            for r_num in rule_list:
                #print(f'Checking rule {r_num} inside rule {rule_num}:{rule_list}, \'{remaining_message}\'')
                if r_num == 8 and remaining_message == previous_8:
                    rule_list_status = False
                    break
                elif r_num == 8:
                    previous_8 = remaining_message
                response, remaining_message = satisfy(rule_dict, r_num, remaining_message, previous_8)
                if not response:  
                    rule_list_status = False
                    break
            if rule_list_status:
                satisfied = True
                #print(f'* Accept rule {rule_num}:{rule_list}')
                break
            else:
                #print(f'* Reject rule {rule_num}:{rule_list}')
                remaining_message = saved_state
    return satisfied, remaining_message


inp = process_input(lines)

print(inp)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

Part 1: Get to Rule 0 or fail

Verify each input against the list of rules
- We can't expand to every possible valid string, that's too much
- We build a tree search with linkages?
    - Depth first search

Rule format: max is "n: n n | n n" (on quick glance)

So my rule format is
[1, [[2, 3],[4,5]]]
Index followed by list of valid set(s) of rules

Part 2:
How does the introduction of loops change evaluation?
Short circuiting is no longer always correct
You could pass the first, continue, then fail, but back up and try the next one
Actually: Depth first recursion therefore disappears down a hole instantly

Detect a loop by recording the last string passed into a given rule number...
a dict of {rule_num: last_string_passed} going down (perhaps saved state too)
and if it detects that you're calling the same remaining string on the same
rule number earlier in the dive, it will reject and call it False so that you
can move on to the next rule or fail
???

In test_input2
List of rules consisting only of 1 (a) and 14 (b)

1: "a"
4: 1 1 aa
5: 1 14 | 15 1 ab aa ba
6: 14 14 | 1 14 bb ab
14: "b"
15: 1 | 14 a b
19: 14 1 | 14 14 ba bb
20: 14 14 | 1 15 bb aa ab
21: 14 1 | 1 14 ba ab
22: 14 14 bb
24: 14 1 ba
25: 1 1 | 1 14 aa ab

2: 1 24 | 14 4 aba baa

Constant rules:
1: "a"
4: 1 1 "aa"
14: "b"
22: 14 14 "bb"
24: 14 1 "ba"

What does "which rules always match the same set of values" mean?
> Which rules do not have 8 or 11 in their parse trees

> Who does call 8 or 11?
0: 8 11
8: 42 | 42 8
> 42, 42 42, 42 42 42...
11: 42 31 | 42 11 31
> 42 31, 42 42 31 31, 42 42 42 31 31 31

What is the full tree of 42?
42: 9 14 | 10 1 babbb baabb bbaab bbabb bbbab bbbbb abbbb aabbb aaaab aaabb,
                aaaba ababa bbbba aaaaa baaaa bbaaa
9: 14 27 | 1 26 babb baab bbaa bbab bbba bbbb, abbb aabb aaaa aaab
27: 1 6 | 14 18 abb aab, baa bab bba bbb
18: 15 15 aa ab ba bb
26: 14 22 | 1 20 bbb, abb aaa aab
10: 23 14 | 28 1 aaab abab bbbb, aaaa baaa bbaa
23: 25 1 | 22 14 aaa aba, bbb
28: 16 1 aaa baa bba
16: 15 1 | 14 14 aa ba, bb

What is the full tree of 31?
31: 14 17 | 1 13 bbaba bbbaa, ababb abaab abbab aabab aabaa aabba
17: 14 2 | 1 7 baba bbaa
7: 14 5 | 1 21  bab baa bba, aba aab
13: 14 3 | 1 12 babb baab bbab, abab abaa abba
12: 24 14 | 19 1 bab, baa bba
3: 5 14 | 16 1 abb aab bab, aaa baa bba
16: 15 1 | 14 14 aa ba, bb

We found and stopped infinite looping on rule 8
Is there infinite looping on rule 11?
    Or is it an issue with keep track of how many 31s to check at the end?
    What is the problem?

Normally: if a rule_list is satisfied, you are done with it and you no longer
have to remember it anymore (back up only the beginning of a rule_list that
failed mid-evaluation))

Now: We may need to retroactively reject an rule_list that actually passed
and try again with a second rule_list that entirely incorporates the rule_list
that we accepted and then retroactively rejected
- Previously if we had a rejection after accepting and progressing past a level,
that was an automatic rejection
- Now, we need memory of the last call(s) of [42 11 31] so that when [42 11 31]
succeeds, we don't just proceed?  Is that what happens now?

The prompt suggests we need a bespoke handler of rule 11

Just freakin hard code the combos of 42 and 31?

Both 42 and 31 yield possible combinations of five characters
For conversion of a=0 and b=1 with binary representations, we have the following
reverse dictionary for 5 letter chunks:
42: 0 1 2 3 7 10 15 16 19 23 24 25 27 29 30 31
31: 4 5 6 9 11 13 26 28

so for handling 8
- at least 15 chars left in the remaining message
- see how many consecutive 3 character chunks match the rule 42 set
- Reject if 0 chunks found
- Starting at the longest streak, check for matching that and see if 11 completes next
- If 11 fails, go back one chunk and process that with 11

=== But the tree is much larger in the official input
The input strings in the puzzle input actually appear to be in chunks of 8
-> up to 256 possible patterns, possibly mutually exclusively distributed
    between the sets of 42 and 31

Solving machine:
from 0 to 255:
    construct 8 character test string with a=0 and b=1
    run satisfy(42) and satisfy(31), no more than one should accept
    if exactly one accepts, add that *string* to dict as key with value "42" or "31"

Then with chunk_dict filled,
scan each input string 8 characters at a time
every chunk must map to either 42 or 31 or else the string must be rejected

next, the acceptable format is
2 or more 42
+ a number of 31s that is nonzero and strictly less than the number of 42

minimum: 42 42 31



'''