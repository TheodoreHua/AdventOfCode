# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    count = 0
    for i in d:
        pair1, pair2 = i.split(",")
        range1, range2 = range(int(pair1.split("-")[0]), int(pair1.split("-")[1]) + 1), range(int(pair2.split("-")[0]), int(pair2.split("-")[1]) + 1)
        if all([x in range2 for x in range1]) or all([x in range1 for x in range2]):
            count += 1
        bar()

    return count
