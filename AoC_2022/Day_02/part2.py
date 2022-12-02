# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

val_map = {"A": 1, "B": 2, "C": 3}
win_map = {"A": "B", "B": "C", "C": "A"}


def main(d: list, bar):
    score = 0
    for i in d:
        opponent, self = i.split(" ")
        if self == 'Y':
            score += val_map[opponent] + 3
        elif self == 'X':
            score += val_map["ABC".replace(opponent, "").replace(win_map[opponent], "")]
        elif self == 'Z':
            score += val_map[win_map[opponent]] + 6
        bar()

    return score
