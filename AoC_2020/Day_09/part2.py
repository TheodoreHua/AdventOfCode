# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2020.Day_09.common_functions import *


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


def main(d: list, bar):
    d = list(map(int, d))
    preamble_length = 25
    pointer = preamble_length
    while pointer < len(d) - 1:
        preamble = d[pointer - preamble_length:pointer]
        if not adds_together(preamble, d[pointer]):
            start = 0
            while True:
                rg = get_contiguous(d[start:], d[pointer])
                if rg is not False:
                    return min(rg) + max(rg)
                start += 1
        pointer += 1
        bar()
    return None
