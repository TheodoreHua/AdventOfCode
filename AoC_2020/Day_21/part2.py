# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

SEPARATION = compile(r"^([a-z ]*) \(contains ([a-z, ]*)\)$")

def sort_allergen_list(data):
    ps = {}
    for line in data:
        parsed_line = SEPARATION.findall(line)[0]
        ingredients, allergens = set(parsed_line[0].split(" ")), set(parsed_line[1].split(", "))
        for allergen in allergens:
            if allergen in ps:
                ps[allergen] &= ingredients
            else:
                ps[allergen] = ingredients.copy()
    taken = set()
    language_pairs = []
    while True:
        for allergens, ingredients in ps.items():
            if len(ingredients - taken) == 1:
                j = min(ingredients-taken)
                language_pairs.append((allergens, j))
                taken.add(j)
                break
        else:
            break
    return ",".join(x[1] for x in sorted(language_pairs))


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(sort_allergen_list(data))
