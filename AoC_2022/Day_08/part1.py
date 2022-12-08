# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def is_visible(grid, x, y):
    if grid[y][x] == 0:
        return False
    for i in range(1, x + 1):
        if grid[y][x - i] >= grid[y][x]:
            break
    else:
        return True
    for i in range(1, y + 1):
        if grid[y - i][x] >= grid[y][x]:
            break
    else:
        return True
    for i in range(1, len(grid[0]) - x):
        if grid[y][x + i] >= grid[y][x]:
            break
    else:
        return True
    for i in range(1, len(grid) - y):
        if grid[y + i][x] >= grid[y][x]:
            break
    else:
        return True
    return False

def main(d: list, bar):
    visible = len(d[0]) * 2 + len(d) * 2 - 4
    grid = [[int(c) for c in row] for row in d]
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if is_visible(grid, x, y):
                visible += 1
            bar()

    return visible
