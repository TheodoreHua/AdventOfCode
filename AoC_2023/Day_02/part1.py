# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

CUBES = compile(r"(\d+) (red|green|blue)")
CUBE_MAX = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def main(d: list, bar):
    total = 0
    for id_, line in enumerate(d, start=1):
        for m in CUBES.findall(line):
            if int(m[0]) > CUBE_MAX[m[1]]:
                break
        else:
            total += id_
        bar()

    return total

def oneliner(d: list, bar):
    return sum(id_ for id_, line in enumerate(d, start=1) if not any(int(m[0]) > CUBE_MAX[m[1]] for m in CUBES.findall(line)))
