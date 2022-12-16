# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from itertools import chain

from .commons import *


def main(d: list, bar):
    paths = parse_paths(d)
    points = list(chain.from_iterable(paths))
    max_x, max_y = max(points, key=lambda i: i[0])[0], max(points, key=lambda i: i[1])[1]
    # This is technically not "infinite", but it's 0 to max_x + 500, which should be more than any reasonable input
    grid = generate_grid(paths, 0, max_x + 500, max_y + 2)
    grid[-1] = True

    count = 0
    while True:
        sand_x, sand_y = 500, 0
        while True:
            if not grid[sand_y + 1, sand_x]:
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
        if sand_x == 500 and sand_y == 0:
            return count
