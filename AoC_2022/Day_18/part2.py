# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np

dirs = lambda x, y, z: {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}

def main(d: list, bar):
    """Credit to /u/4HbQ for this solution logic (flood fill and visited cubes)"""
    points = set()
    for line in d:
        points.add(tuple(int(x) for x in line.split(',')))
    grid = np.zeros((max([x[0] for x in points]) + 1, max([x[1] for x in points]) + 1, max([x[2] for x in points]) + 1), dtype=bool)
    for point in points:
        grid[point[0], point[1], point[2]] = True
    seen = set()
    to_parse = [(-1, -1, -1)]
    while to_parse:
        cube = to_parse.pop()
        # noinspection PyTypeChecker
        to_parse += [s for s in (dirs(*cube) - points - seen) if all(-1 <= i <= grid.shape[j] for j, i in enumerate(s))]
        seen |= {cube}
        bar()

    return sum((s in seen) for cube in points for s in dirs(*cube))
