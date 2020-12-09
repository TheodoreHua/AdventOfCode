# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import *

def get_contiguous(sequence, target):
    pointer = 1
    while pointer < len(sequence):
        sm = sum(sequence[0:pointer])
        if sm == target:
            return sequence[0:pointer - 1]
        if sm > target:
            return False
        pointer += 1
    return False

def find_contiguous_sum(preamble_length, xmas_nums):
    pointer = preamble_length
    while pointer < len(xmas_nums) - 1:
        preamble = xmas_nums[pointer - preamble_length:pointer]
        if not adds_together(preamble, xmas_nums[pointer]):
            start = 0
            while True:
                rg = get_contiguous(xmas_nums[start:], xmas_nums[pointer])
                if rg is not False:
                    return min(rg) + max(rg)
                start += 1
        pointer += 1
    return None


with open("data/input.txt", "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

print(find_contiguous_sum(25, data))
