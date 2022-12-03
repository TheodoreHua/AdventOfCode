# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from string import ascii_letters


def main(d: list, bar):
    s = 0
    for i in d:
        first, second = i[:len(i) // 2], i[len(i) // 2:]
        char = next(j for j in first if j in second)
        s += ascii_letters.index(char) + 1
        bar()

    return s
