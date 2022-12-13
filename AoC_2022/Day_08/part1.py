# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np


def is_visible(grid, x, y):
    val, row, col = grid[y][x], grid[y, :], grid[:, x]
    return not (max(row[:x]) >= val and max(row[x + 1:]) >= val and max(col[:y]) >= val and max(col[y + 1:]) >= val)


def main(d: list, bar):
    visible = len(d[0]) * 2 + len(d) * 2 - 4
    grid = np.array([[int(c) for c in row] for row in d])
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if is_visible(grid, x, y):
                visible += 1
            bar()

    return visible
