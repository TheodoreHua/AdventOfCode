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
            return False
        if pointer == len(instructions):
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


def main(d: list, bar):
    for point, value in enumerate(d):
        new_instructions = d[:]
        if value.startswith("nop"):
            new_instructions[point] = "jmp " + value[4:]
        elif value.startswith("jmp"):
            new_instructions[point] = "nop " + value[4:]
        else:
            continue
        new_accum = infini_loop_accum(new_instructions)
        if new_accum is not False:
            return new_accum
        bar()
