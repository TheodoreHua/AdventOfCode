# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile
from math import prod

ADJACENT = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
)
BEFORE_REGEX = compile(r"\d+$")
AFTER_REGEX = compile(r"^\d+")

def main(d: list, bar):
    grid = [i for i in d]
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            n = grid[r][c]
            if n.isdigit() or n == ".":
                bar()
                continue
            # Prevent duplicates from the same symbol (adj overlap) -- apparently duplicates across symbols are allowed
            visited = []
            found = []
            for ar, ac in ADJACENT:
                nr, nc = r + ar, c + ac
                try:
                    row = grid[nr]
                    n2 = row[nc]
                except IndexError:  # OOB
                    continue
                if not n2.isdigit():  # Not part of a number
                    continue

                # Get any digits before, including, and after the current digit
                before = BEFORE_REGEX.findall(row[:nc])
                after = AFTER_REGEX.findall(row[nc:])  # This includes current digit
                num = (before[0] if len(before) >= 1 else "") + (after[0] if len(after) >= 1 else "")
                num_coordinate = (nr, row.index(num))
                if num_coordinate in visited:
                    continue
                visited.append(num_coordinate)
                found.append(int(num))
            if len(found) == 2:
                total += prod(found)
            bar()

    return total

