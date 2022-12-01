# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    calories = []
    first = True
    for i in d:
        if i == "":
            first = True
        elif first:
            calories.append(int(i))
            first = False
        else:
            calories[-1] += int(i)
        bar()

    return max(calories)
