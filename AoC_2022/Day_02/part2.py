# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

val_map = {"A": 1, "B": 2, "C": 3}


def main(d: list, bar):
    score = 0
    for i in d:
        opponent, self = i.split(" ")
        if self == 'Y':
            score += val_map[opponent]
            score += 3
        elif opponent == 'A':
            if self == 'X':
                score += val_map['C']
            else:
                score += val_map['B']
                score += 6
        elif opponent == 'B':
            if self == 'X':
                score += val_map['A']
            else:
                score += val_map['C']
                score += 6
        elif opponent == 'C':
            if self == 'X':
                score += val_map['B']
            else:
                score += val_map['A']
                score += 6
        bar()

    return score
