# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def get_scenic_score(grid, x, y):
    scenic_score = 1
    i = 1
    for i in range(1, x + 1):
        if grid[y][x - i] >= grid[y][x]:
            break
    scenic_score *= i
    for i in range(1, y + 1):
        if grid[y - i][x] >= grid[y][x]:
            break
    scenic_score *= i
    for i in range(1, len(grid[0]) - x):
        if grid[y][x + i] >= grid[y][x]:
            break
    scenic_score *= i
    for i in range(1, len(grid) - y):
        if grid[y + i][x] >= grid[y][x]:
            break
    scenic_score *= i
    return scenic_score

def main(d: list, bar):
    grid = [[int(c) for c in row] for row in d]
    scenic_scores = []
    # This is just casually assuming the edges can't be the highest point. I'm too lazy to fix it...
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            scenic_scores.append(get_scenic_score(grid, x, y))
            bar()

    return max(scenic_scores)
