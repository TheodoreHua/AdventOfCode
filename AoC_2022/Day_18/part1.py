# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np

dirs = lambda x, y, z: {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}

def main(d: list, bar):
    points = []
    for line in d:
        points.append([int(x) for x in line.split(',')])
    grid = np.zeros((max([x[0] for x in points]) + 1, max([x[1] for x in points]) + 1, max([x[2] for x in points]) + 1), dtype=bool)
    for point in points:
        grid[point[0], point[1], point[2]] = True
    uncovered_sides = 0
    for x, y, z in points:
        for d in dirs(x, y, z):
            if d[0] < 0 or d[1] < 0 or d[2] < 0:
                uncovered_sides += 1
            elif d[0] > grid.shape[0] - 1 or d[1] > grid.shape[1] - 1 or d[2] > grid.shape[2] - 1:
                uncovered_sides += 1
            elif not grid[d]:
                uncovered_sides += 1
        bar()

    return uncovered_sides
