# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *

def main(d: list, bar):
    grid, start, end = generate_grid(d)
    G = generate_graph(grid)

    return len(networkx.shortest_path(G, start, end)) - 1