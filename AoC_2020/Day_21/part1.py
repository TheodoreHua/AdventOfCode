# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

SEPARATION = compile(r"^([a-z ]*) \(contains ([a-z, ]*)\)$")


def main(d: list, bar):
    parsed_data = []
    allergens = {}
    for line in d:
        ingredients, allergen = SEPARATION.findall(line)[0]
        parsed_data.append((ingredients.split(" "), allergen.split(", ")))
        for allergen in parsed_data[-1][1]:
            if allergen not in allergens.keys():
                allergens[allergen] = [len(parsed_data) - 1]
            else:
                allergens[allergen].append(len(parsed_data) - 1)
        bar()
    possible_allergens = []
    for i, dat in enumerate(parsed_data):
        ingredients, allergen = dat
        all_occur = []
        for a in allergen:
            for ingredient in ingredients:
                al = True
                for occurence in allergens[a]:
                    if ingredient not in parsed_data[occurence][0]:
                        al = False
                        break
                if al:
                    all_occur.append(ingredient)
        possible_allergens += [o for o in all_occur if o not in possible_allergens]
        bar()
    return len([j for i in parsed_data for j in i[0] if j not in possible_allergens])
