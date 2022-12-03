# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from string import ascii_letters


def main(d: list, bar):
    segments = [d[i:i + 3] for i in range(0, len(d), 3)]
    s = 0
    for i in segments:
        for j in i[0]:
            if j in i[1] and j in i[2]:
                s += ascii_letters.index(j) + 1
                break
        bar()

    return s
