# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *

def main(d: list, bar):
    grid, _, end = generate_grid(d)
    G = generate_graph(grid)

    paths = []
    for x, y in np.argwhere(grid == 1):
        paths.append(networkx.shortest_path_length(G, (x, y), end) + 1)
        bar()

    return min(paths)
