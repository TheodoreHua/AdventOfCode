# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile, findall
from math import prod

GAME_ID = compile(r"Game (\d+)")
CUBES = compile(r"(\d+) (red|green|blue)")

def main(d: list, bar):
    total = 0
    for line in d:
        matches = CUBES.findall(line)
        largest = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for m in matches:
            n = int(m[0])
            t = m[1]
            if n > largest[t]:
                largest[t] = n
        total += prod(largest.values())
        bar()

    return total

def oneliner(d: list, bar):
    return sum(prod(max(map(int, findall(rf"(\d+) {t}", line))) for t in ("red", "green", "blue")) for line in d)
