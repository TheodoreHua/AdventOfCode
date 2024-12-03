# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import findall


def main(d: str, bar):
    s = 0
    for i, j in findall(r"mul\((\d{1,3}),(\d{1,3})\)", d):
        s += int(i) * int(j)
        bar()
    return s


def oneliner(d: str, bar):
    return sum(int(i) * int(j) for i, j in findall(r"mul\((\d{1,3}),(\d{1,3})\)", d))
