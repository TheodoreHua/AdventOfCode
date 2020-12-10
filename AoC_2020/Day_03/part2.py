# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import *
from math import prod
from json import load

def multiply_sets(lines, sets):
    set_results = []
    for s in sets:
        set_results.append(count_trees(duplicate_required(lines, right=s[0], down=s[1]), right=s[0], down=s[1]))
    return prod(set_results)


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

with open("data/sets.json", "r") as f:
    sets = load(f)

print(multiply_sets(data, sets))
