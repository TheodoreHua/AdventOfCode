# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import networkx
import numpy as np


def main(d: list, bar):
    grid = np.zeros((len(d[0]), len(d)), dtype=int)
    bar.text("Parsing input")
    for y, row in enumerate(d):
        for x, value in enumerate(row):
            grid[x][y] = int(value)

    bar.text("graphing grid")
    G = networkx.grid_2d_graph(len(grid), len(grid[0]), create_using=networkx.DiGraph)
    bar.text("Weighing edges")
    for u, v in G.edges:
        G[u][v]['weight'] = grid[v[0]][v[1]]
        bar()

    bar.text("Finding shortest path")
    path = networkx.shortest_path(G, (0, 0), (len(d[0]) - 1, len(d) - 1), weight='weight')
    bar.text("Calculating path cost")
    return sum([grid[x, y] for x, y in path[1:]])
