# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile
from math import lcm

LINE_REGEX = compile(r"^(.+) = \((.+), (.+)\)$")
m = {}


def main(d: list, bar):
    instructions = [0 if i == "L" else 1 for i in d[0]]
    l = len(instructions)
    for line in d[2:]:
        match = LINE_REGEX.fullmatch(line)
        m[match.group(1)] = (match.group(2), match.group(3))

    curs = [i for i in m if i.endswith("A")]  # Create cursors, starting at each node ending in A
    cs = [0] * len(curs)  # Create another array, storing the shortest # of steps for each A node, to reach a Z node
    c = 0  # Count the number of steps
    while True:
        if all(cs):  # If we've found the shortest # of steps for every starting point, we're done, and can break
            break
        for i, j in enumerate(curs):  # Going through each cursor
            if cs[i] == 0:  # If we have not found the shortest # of steps
                curs[i] = m[j][instructions[c % l]]  # Update the current cursor position from the instructions
                if curs[i].endswith("Z"):  # If we're at a Z node, we've found the shortest # of steps for this cursor
                    cs[i] = c + 1  # Store the # of steps for this cursor, +1 as c does not include the current step
        c += 1  # Increment the # of steps
        bar()

    # Find the lowest common multiple of the shortest # of steps for each node, this will reveal the shortest # of steps
    #  until ALL nodes reach a Z
    return lcm(*cs)
