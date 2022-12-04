# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    count = 0
    for i in d:
        pair1, pair2 = i.split(",")
        lower1, upper1 = map(int, pair1.split("-"))
        lower2, upper2 = map(int, pair2.split("-"))
        ab = set(range(lower1, upper1 + 1))
        cd = set(range(lower2, upper2 + 1))
        if ab <= cd or cd <= ab:
            count += 1

    return count
