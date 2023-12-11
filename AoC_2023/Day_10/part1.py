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
    md = float('-inf')
    while queue:
        pipe: Pipe = queue.pop(0)
        visited.add(pipe)
        for i in pipe.get_connecting_pipes(grid):
            if i not in visited:
                i.distance = pipe.distance + 1
                if i.distance > md:
                    md = i.distance
                queue.append(i)

    return md
