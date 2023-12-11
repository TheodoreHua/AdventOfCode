# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import Pipe

def main(d: list, bar):
    grid = []
    start = None
    for y, line in enumerate(d):
        grid.append([])
        for x, pipe in enumerate(line):
            if pipe == ".":
                grid[-1].append(None)
                continue
            grid[-1].append(Pipe(x, y, pipe))
            if pipe == "S":
                start = grid[-1][-1]
                start.distance = 0
    start.handle_s(grid)

    queue = [start]
    visited = set()
    while queue:
        pipe: Pipe = queue.pop(0)
        visited.add(pipe)
        for i in pipe.get_connecting_pipes(grid):
            if i not in visited:
                queue.append(i)

    c = 0
    for line in grid:
        for x, pipe in enumerate(line):
            if len(
                    [i for i in line[:x] if i is not None and i in visited and i.shape in "|JL"]
            ) % 2 == 1 and pipe not in visited:
                c += 1
            bar()

    return c
