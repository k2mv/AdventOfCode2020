# 19

&#x1F630;&#x1F630;&#x1F630; *Lord have mercy* &#x1F630;&#x1F630;&#x1F630;

> _(Remember, **you only need to handle the rules you have**; building a solution that could handle any hypothetical combination of rules would be significantly more difficult.)_

I was able to get away with 'any hypothetical combination of rules' in **Part 1**, but any attempt to make that code work in **Part 2** (with the potentially infinitely looping rules) didn't accept everything it should have, no matter how much duct tape and lookback I tried to implement.

## Part 2a: The bird's eye level solution

In the end, I started going through the second block of test input `test_input2.txt` and started re-analyzing the set of rules from the beginning.

* Rule 0 is fixed at `8 11`.
* Rule 8 is satisfied with 1 or more consecutive instances of Rule 42.
* Rule 11 is satisfied with 1 or more consecutive instances of Rule 42, followed by an equal number of instances of Rule 31.

Taken together, we can say that, in general, Rule 0 is satisfied by:
* 2 or more consecutive instances of Rule 42
* followed by 1 or more consecutive instances of Rule 31, but strictly fewer than the preceding number of instances of Rule 42

The shortest valid answer, for example, is therefore `42 42 31`.

## Part 2b: Patterns revealed

That's all well and good, but both 42 and 31 need to be expanded several levels down before we can evaluate whether a valid 42 or 31 even exists in the input... you can't just do that by hand every time, right?

&#x1F914;

If you start at the rules that resolve directly to 1 (`"a"`) and/or 14 (`"b"`) or some combination thereof, you can start constructing the list of all possible strings that satisfy each rule.  Once you have the list of strings for a given rule, you can combine those strings to create a new list of longer strings for other rules.

You can see my full handcrafted chart in the notes at the bottom of `19_2.py`, but here's a short example, using the example data in `test_input2.txt`.

* Rule 16 is `15 1 | 14 14`.  Since 1 is `a` and 14 is `b`, that translates to `15 a | b b`.
* Rule 15 is `1 | 14` which is satisfied by `a` or `b`.
* Therefore, you can say that Rule 16 can be satisfied by `aa` or `ba` on the left side, or `bb` on the right side.

Follow this up the chain, and you find that both 42 and 31 each resolve to sets of five-character strings.

```
42: babbb baabb bbaab bbabb bbbab bbbbb abbbb aabbb aaaab aaabb,
    aaaba ababa bbbba aaaaa baaaa bbaaa

31: bbaba bbbaa, ababb abaab abbab aabab aabaa aabba
```

So every 42 and every 31 resolves to five character chunks...

...and every one of the input strings has a length that's a multiple of 5...

&#x1F914;&#x1F914;

## Part 2c: Taking it home

It turns out that the two sets of 5-character strings are mutually exclusive.  So if I read the string 5 characters at a time, I can 'translate' each one to either a `42` or a `31` and then follow the counting process from Part 2a above.  (Normally you'd have to check for input strings that are the wrong length or have sections that don't show up in either set, but I guessed correctly that the example input (and the puzzle input) doesn't throw any of those at you.)

I can't do this whole thing by hand for the huge number of rules in the **Part 2** input `input1219_2.txt`, but I do notice right off the bat that all of the input strings have lengths in multiples of eight.

&#x1F914;&#x1F62E;

For a string of length 8, there are 256 possible ways to construct it out of `a`s and `b`s.  I still have my traditional solver code from **Part 1**, which can evaluate from scratch whether a given string satisfies a given rule.

So the first part of the solution is to generate every possible eight-character string, from `aaaaaaaa`, `aaaaaaab`... through to `bbbbbbbb`.  For each one of those, I ran it through the traditional solver for both rule 42 and rule 31, and added the string as a key in the new dictionary `chunk_dict` with either `42` or `31` as the value, depending on which rule (if any) accepted the string.

Then, I chewed each input line into eight-character chunks, translated each eight-character chunk into either `42` or `31` using `chunk_dict`, and verified the (very short) chain of `42`s and `31`s using the counting process from part 2a above.

If you run either `19_2.py` or `19_2_clean.py`, you'll see the actual lists, e.g. `[42, 42, 42, 42, 42, 31, 31]` that I assembled from each input string.

## Afterword

I'm confident that there are many quicker and cleaner ways to get today's answer, and I look forward to checking some of them out as soon as I upload this writeup and lift my spoiler embargo.

Good luck to everyone out there taking a crack at AoC this month! &#x1F44B;