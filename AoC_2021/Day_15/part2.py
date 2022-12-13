# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import networkx
import numpy as np
from itertools import product


def main(d: list, bar):
    grid_segment = np.zeros((len(d[0]), len(d)), dtype=int)
    grid = np.zeros((len(d[0]) * 5, len(d) * 5), dtype=int)
    bar.text("Parsing input")
    for y, row in enumerate(d):
        for x, value in enumerate(row):
            grid_segment[x][y] = int(value)
            bar()
    bar.text("Building grid")
    for row, col in product(range(len(grid_segment[0]) * 5), range(len(grid_segment) * 5)):
        grid[row][col] = grid_segment[row % len(grid_segment[0])][col % len(grid_segment)] + (row // len(grid_segment[0])) + (col // len(grid_segment))
        bar()
    bar.text("Checking grid")
    grid[grid > 9] -= 9

    bar.text("Graphing grid")
    G = networkx.grid_2d_graph(len(grid), len(grid[0]), create_using=networkx.DiGraph)
    bar.text("Weighing edges")
    for u, v in G.edges:
        G[u][v]['weight'] = grid[v[0]][v[1]]
        bar()

    bar.text("Finding shortest path")
    path = networkx.shortest_path(G, (0, 0), (grid.shape[0] - 1, grid.shape[1] - 1), weight='weight')
    bar.text("Calculating path cost")
    return sum([grid[x, y] for x, y in path[1:]])
