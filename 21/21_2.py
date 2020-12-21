file_input = open("input1221.txt", "r")
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
    foods = []
    ingredients = []
    allergens = []
    for l in lines:
        ing_list = []
        allergen_list = []
        ings = l.split()
        phase = 0
        for i in ings:
            if phase == 0:
                if i != '(contains':
                    ing_list.append(i)
                    if i not in ingredients:
                        ingredients.append(i)
                else:
                    phase = 1
            elif phase == 1:
                the_allergen = i[:-1]
                allergen_list.append(the_allergen)
                if the_allergen not in allergens:
                    allergens.append(the_allergen)

        foods.append((ing_list, allergen_list))
    return foods, ingredients, allergens

def allergen_test(ing_allerg_dict, foods, ingredients, allergens, test_allergen):
    test_dict = {}
    counter = 0
    for f in foods:
        if test_allergen in f[1]:
            counter += 1
            for ingr in f[0]:
                if ingr not in test_dict.keys():
                    test_dict[ingr] = 1
                else:
                    test_dict[ingr] += 1
    for ingr in test_dict.keys():
        if test_dict[ingr] == counter:
            print(f'Allergen {test_allergen}: ingredient {ingr}')
            if ingr not in ing_allerg_dict.keys():
                ing_allerg_dict[ingr] = [test_allergen]
            else:
                ing_allerg_dict[ingr].append(test_allergen)

foods, ingredients, allergens = process_input(lines)
print(foods)
print(ingredients)
print(allergens)

ing_allerg_dict = {}

for allerg in allergens:
    allergen_test(ing_allerg_dict, foods, ingredients, allergens, allerg)

print(ing_allerg_dict)

allergy_solution_dict = {}

while len(allergy_solution_dict) < len(allergens):
    key_list = list(ing_allerg_dict.keys())
    for ingr in key_list:
        if ingr in ing_allerg_dict.keys() and len(ing_allerg_dict[ingr]) == 1:
            allergen_found = ing_allerg_dict[ingr][0]
            allergy_solution_dict[allergen_found] = ingr
            for ingr2 in key_list:
                if allergen_found in ing_allerg_dict[ingr2]:
                    temp = ing_allerg_dict[ingr2]
                    temp.remove(allergen_found)
                    ing_allerg_dict[ingr2] = temp



print(allergy_solution_dict)

allergens.sort()
print(allergens)

final_ans = ''
for a in allergens:
    temp = allergy_solution_dict[a] + ','
    final_ans = final_ans + temp
final_ans = final_ans[:-1]

print(final_ans)

file_input.close()

'''
SCRATCH PAD RIGHT HERE

How do you determine which foods cannot have any allergen?

We can try to isolate the one ingredient with an allergen by checking all
ingredient lists with the allergen flagged and seeing if any one ingredient
is present in all of them - maybe have candidates if there is none isolated

FOODS have INGREDIENTS and ALLERGEN_FLAGS


'''