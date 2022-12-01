# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: str, bar):
    calories = []
    for i in d.split("\n\n"):
        s = 0
        for j in i.split("\n"):
            s += int(j)
        calories.append(s)

    return sum(sorted(calories, reverse=True)[0:3])


def oneliner(d: str, bar):
    return sorted([sum([int(j) for j in i.split("\n")]) for i in d.split("\n\n")], reverse=True)[0:3]
