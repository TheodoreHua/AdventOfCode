# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from itertools import product
from AoC_2020.Day_14.common_functions import MASK_REGEX, MEM_REGEX


def get_mem(mask: str, starting: str):
    starting = list(starting)
    floating_indices = []
    for index, char in enumerate(mask):
        if char != "X":
            if char == "1":
                starting[index] = char
        else:
            starting[index] = "X"
            floating_indices.append(index)
    possibilities = []
    combinations = product([0, 1], repeat=len(floating_indices))
    for tup in combinations:
        possible = starting
        for i, i2 in enumerate(floating_indices):
            possible[i2] = str(tup[i])
        possibilities.append("".join(possible))
    return possibilities


def main(d: list, bar):
    mem = {}
    for i, line in enumerate(d):
        if line.startswith("mask"):
            pointer = i + 1
            mask = MASK_REGEX.findall(line)[0]
            while pointer < len(d):
                l = d[pointer]
                if l.startswith("mem"):
                    ld = MEM_REGEX.findall(l)[0]
                    for m in get_mem(mask, "{:036b}".format(int(ld[0]))):
                        mem[int(m, 2)] = int(ld[1])
                else:
                    break
                pointer += 1
        bar()
    s = 0
    for val in mem.values():
        s += val
    return s
