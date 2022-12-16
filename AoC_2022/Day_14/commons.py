# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np


def parse_paths(d: list):
    paths = []
    for l in d:
        path = []
        for point in l.split(" -> "):
            path.append(tuple(map(int, point.split(","))))
        paths.append(path)
    return paths


def generate_grid(paths, min_x, max_x, max_y):
    grid = np.zeros((max_y + 1, max_x - min_x + 1), dtype=bool)
    for path in paths:
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            if x1 == x2:
                grid[min(y1, y2):max(y1, y2) + 1, x1 - min_x] = True
            else:
                grid[y1, min(x1, x2) - min_x:max(x1, x2) + 1 - min_x] = True
    return grid
