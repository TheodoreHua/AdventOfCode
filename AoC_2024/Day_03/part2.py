# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import findall


def main(d: str, bar):
    s = 0
    do = True
    for i, j, k in findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", d):
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False
        elif do:
            s += int(j) * int(k)
        bar()
    return s
