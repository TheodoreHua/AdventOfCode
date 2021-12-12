# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from numpy import prod

from AoC_2021.Day_09.commons import Heightmap

def count_basin(heightmap, x, y, done=None):
    if done is None:
        done = []
    done.append((x, y))
    count = 1
    for cx, cy in heightmap.adjacent(x, y):
        if (cx, cy) not in done and heightmap.board[cy][cx] < 9:
            done.append((cx, cy))
            count += count_basin(heightmap, cx, cy, done)
    return count

def main(d:list, bar):
    heightmap = Heightmap(d)
    basins = []
    for x in range(heightmap.width):
        for y in range(heightmap.height):
            if heightmap.is_low(x, y):
                basins.append(count_basin(heightmap, x, y))
            bar()

    return prod(sorted(basins, reverse=True)[:3])
