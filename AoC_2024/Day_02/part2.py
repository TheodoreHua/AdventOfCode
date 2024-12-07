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
        lp = list(map(int, l.split()))
        if is_safe(lp):
            safe += 1
        else:
            for i in range(len(lp)):
                lc = lp[:]
                lc.pop(i)
                if is_safe(lc):
                    safe += 1
                    break
        bar()

    return safe


def oneliner(d: list, bar):
    return sum(int(bool((lpf := list(map(int, l.split()))) and any(((lp in (sorted(lp), sorted(lp, reverse=True)) and all(1 <= abs(lp[i+1] - lp[i]) <= 3 for i in range(len(lp)-1))) for lp in [lpf] + [lpf[:i] + lpf[i+1:] for i in range(len(lpf))])))) for l in d)
