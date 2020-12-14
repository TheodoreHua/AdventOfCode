# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import MASK_REGEX, MEM_REGEX

def apply_mask(mask:str, val:str):
    val = list(val)
    for index, char in enumerate(mask):
        if char != "X":
            val[index] = char
    return "".join(val)

def sum_val(data):
    mem = {}
    for i, line in enumerate(data):
        if line.startswith("mask"):
            pointer = i + 1
            mask = MASK_REGEX.findall(line)[0]
            while pointer < len(data):
                l = data[pointer]
                if l.startswith("mem"):
                    ld = MEM_REGEX.findall(l)[0]
                    mem[ld[0]] = apply_mask(mask, "{:036b}".format(int(ld[1])))
                else:
                    break
                pointer += 1
    s = 0
    for val in mem.values():
        s += int(val, 2)
    return s


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(sum_val(data))
