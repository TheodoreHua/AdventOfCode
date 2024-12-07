# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import is_safe


def main(d: list, bar):
    """F[[D-LEN]]"""
    safe = 0
    for l in d:
        if is_safe(list(map(int, l.split()))):
            safe += 1
        bar()

    return safe


def oneliner(d: list, bar):
    return sum(int(((lp := list(map(int, l.split()))) in (sorted(lp), sorted(lp, reverse=True)) and all(1 <= abs(lp[i+1] - lp[i]) <= 3 for i in range(len(lp)-1)))) for l in d)
