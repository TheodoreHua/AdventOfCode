# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from json import load
from re import compile, split

def check_valid(passport, guidelines):
    passport_values = split(r"[\n ]", passport)
    for guideline in guidelines:
        g_re = compile(guideline)
        valid = False
        for value in passport_values:
            if g_re.search(value) is not None:
                valid = True
        if not valid:
            return False
    return True

def count_valid(passports, guidelines):
    valid_count = 0
    for passport in passports:
        if check_valid(passport, guidelines):
            valid_count += 1
    return valid_count


with open("data/input.txt", "r") as f:
    data = f.read()

with open("data/guidelines.json", "r") as f:
    guidelines = load(f)

data = data.split("\n\n")

print(count_valid(data, guidelines))
