# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from statistics import median

m = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
c = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def get_by_value(dc, value):
    for k, v in dc.items():
        if v == value:
            return k


def main(d: list, bar):
    error_scores = []
    for line in d:
        characters = []
        co = True
        for char in line:
            if char in m.values():
                characters.append(char)
            else:
                if m[char] != characters[-1]:
                    co = False
                    break
                else:
                    del characters[-1]
        if co:
            error_scores.append(0)
            for opening in reversed(characters):
                error_scores[-1] *= 5
                error_scores[-1] += c[get_by_value(m, opening)]
        bar()

    return median(error_scores)
