# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import *

def find_invalid(preamble_length, xmas_nums):
    pointer = preamble_length
    while pointer < len(xmas_nums) - 1:
        preamble = xmas_nums[pointer - preamble_length:pointer]
        if not adds_together(preamble, xmas_nums[pointer]):
            return xmas_nums[pointer]
        pointer += 1
    return None


with open("data/input.txt", "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

print(find_invalid(25, data))
