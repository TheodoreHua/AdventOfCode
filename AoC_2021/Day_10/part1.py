# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

m = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
c = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def main(d: list, bar):
    error_score = 0
    for line in d:
        characters = []
        for char in line:
            if char in m.values():
                characters.append(char)
            else:
                o = m[char]
                if o != characters[-1]:
                    error_score += c[char]
                    break
                else:
                    del characters[-1]
        bar()

    return error_score
