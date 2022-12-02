# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

val_map = {"X": 1, "Y": 2, "Z": 3}
conv_map = {"X": "A", "Y": "B", "Z": "C"}
win_map = {"A": "Y", "B": "Z", "C": "X"}


def main(d: list, bar):
    score = 0
    for i in d:
        opponent, self = i.split(" ")
        score += val_map[self]
        if opponent == conv_map[self]:
            score += 3
        elif self == win_map[opponent]:
            score += 6
        bar()

    return score
