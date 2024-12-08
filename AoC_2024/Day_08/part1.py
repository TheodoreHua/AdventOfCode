# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *


def main(d: list, bar):
    antennas = parse_input(d)

    ans = set()
    for p in grid_traverse(len(d), len(d[0])):
        for _, an1, an2 in antenna_pairs(antennas):
            if not point_on_line(p, an1, an2):
                continue
            dist_an1 = manhattan_distance(p, an1)
            dist_an2 = manhattan_distance(p, an2)
            if (dist_an2 and dist_an1/dist_an2 == 2) or (dist_an1 and dist_an2/dist_an1 == 2):
                ans.add(p)
                break
        bar()

    return len(ans)
