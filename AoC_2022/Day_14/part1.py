# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *
from itertools import chain

def main(d: list, bar):
    paths = parse_paths(d)
    points = list(chain.from_iterable(paths))
    min_x = min(points, key=lambda i: i[0])[0]
    max_x, max_y = max(points, key=lambda i: i[0])[0], max(points, key=lambda i: i[1])[1]
    grid = generate_grid(paths, min_x, max_x, max_y)

    count = 0
    while True:
        sand_x, sand_y = 500 - min_x, 0
        while True:
            if sand_y >= max_y:
                return count
            elif not grid[sand_y + 1, sand_x]:
                sand_y += 1
            elif not grid[sand_y + 1, sand_x - 1]:
                sand_x -= 1
                sand_y += 1
            elif not grid[sand_y + 1, sand_x + 1]:
                sand_x += 1
                sand_y += 1
            else:
                grid[sand_y, sand_x] = True
                break
        count += 1
        bar()
