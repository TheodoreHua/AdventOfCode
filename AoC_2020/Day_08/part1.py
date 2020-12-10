# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def infini_loop_accum(instructions):
    pointer = 0
    accumulator = 0
    checked = []
    while True:
        if pointer in checked:
            return accumulator
        checked.append(pointer)
        instruc = instructions[pointer]
        if instruc.startswith("nop"):
            pass
        elif instruc.startswith("acc"):
            accumulator += int(instruc[4:])
        elif instruc.startswith("jmp"):
            pointer += int(instruc[4:])
            continue
        pointer += 1


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(infini_loop_accum(data))
