# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np
import networkx
from string import ascii_lowercase


def generate_grid(d: list):
    grid = np.zeros((len(d), len(d[0])), dtype=np.int8)
    start, end = None, None
    for i, line in enumerate(d):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                grid[i, j] = 0
            elif c == 'E':
                end = (i, j)
                grid[i, j] = 25
            else:
                grid[i, j] = ascii_lowercase.index(c)

    assert start is not None and end is not None
    return grid, start, end


def generate_graph(grid: np.array):
    G = networkx.DiGraph()
    for x, y in np.ndindex(grid.shape):
        if grid[x, y] == -1:
            continue
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                if grid[nx, ny] - grid[x, y] <= 1:
                    G.add_edge((x, y), (nx, ny))

    return G
