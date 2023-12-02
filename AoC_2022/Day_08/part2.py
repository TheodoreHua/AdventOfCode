# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def get_scenic_score(grid, x, y):
    scenic_score = 1
    val = grid[y][x]
    j = 1
    for i in [(range(1, x + 1), lambda g, k: g[y][x - k]), (range(1, len(grid[0]) - x), lambda g, k: g[y][x + k]),
              (range(1, y + 1), lambda g, k: g[y - k][x]), (range(1, len(grid) - y), lambda g, k: g[y + k][x])]:
        for j in i[0]:
            if i[1](grid, j) >= val:
                break
        scenic_score *= j
    return scenic_score


def main(d: list, bar):
    grid = [[int(c) for c in row] for row in d]
    scenic_scores = []
    # This is just casually assuming the edges can't be the highest point. I'CUBE_MAX too lazy to fix it...
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            scenic_scores.append(get_scenic_score(grid, x, y))
            bar()

    return max(scenic_scores)
