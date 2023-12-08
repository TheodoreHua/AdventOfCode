# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

LINE_REGEX = compile(r"^(.+) = \((.+), (.+)\)$")
m = {}

def main(d: list, bar):
    instructions = [0 if i == "L" else 1 for i in d[0]]
    current = "AAA"
    for line in d[2:]:
        match = LINE_REGEX.fullmatch(line)
        m[match.group(1)] = (match.group(2), match.group(3))

    c = 0
    while True:
        for inst in instructions:
            if current == "ZZZ":
                return c
            current = m[current][inst]
            c += 1
            bar()
