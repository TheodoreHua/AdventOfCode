# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

GAME_ID = compile(r"Game (\d+)")
CUBES = compile(r"((\d+) (red|green|blue))")
CUBE_MAX = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def main(d: list, bar):
    total = 0
    for line in d:
        id = int(GAME_ID.findall(line)[0])
        for m in CUBES.findall(line):
            if int(m[1]) > CUBE_MAX[m[2]]:
                break
        else:
            total += id
        bar()

    return total
