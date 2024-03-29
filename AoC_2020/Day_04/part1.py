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


def main(d: list, bar):
    if d[-1] != '':
        d.append('')
    required = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    valid_count = 0
    passport = ""
    for l in d:
        if l == '':
            if check_valid(passport, required):
                valid_count += 1
            passport = ""
        else:
            passport += l + ' '
        bar()
    return valid_count
