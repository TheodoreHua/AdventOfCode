# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from itertools import product
from .commons import *


def main(d: list, bar):
    blocked, sr, sc = parse_input(d)
    cnt = 0
    for br, bc in product(range(len(blocked)), range(len(blocked[0]))):
        if blocked[br][bc]:
            bar()
            continue
        blocked[br][bc] = True

        track = set()
        for k in guard_path(blocked, sr, sc, include_cdi=True):
            if k in track:
                cnt += 1
                break
            track.add(k)

        blocked[br][bc] = False
        bar()

    return cnt
