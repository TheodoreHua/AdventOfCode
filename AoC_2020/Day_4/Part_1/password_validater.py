# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def check_valid(passport, required):
    for require_field in required:
        if require_field not in passport:
            return False
    return True

def count_valid(passports, required):
    valid_count = 0
    for passport in passports:
        if check_valid(passport, required):
            valid_count += 1
    return valid_count


with open("../data/input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")

print(count_valid(data, ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]))
