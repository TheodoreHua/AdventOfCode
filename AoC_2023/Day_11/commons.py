# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from itertools import combinations

def get_col(grid, n):
    return [line[n] for line in grid]

def get_cols(grid):
    return [get_col(grid, i) for i in range(len(grid))]

def get_sum(d: list, N):
    # Create the universe, and a list of all galaxy coordinates
    grid = []
    galaxies = []
    for y, line in enumerate(d):
        grid.append([])
        for x, i in enumerate(line):
            ig = i == "#"
            grid[-1].append(ig)
            if ig:
                galaxies.append([x, y])

    # Calculate the new coordinates of each galaxy after expansion
    new_galaxies = [galaxy[:] for galaxy in galaxies]
    for y, line in enumerate(grid):
        if not any(line):
            for i, galaxy in enumerate(galaxies):
                if galaxy[1] > y:
                    new_galaxies[i][1] += N - 1
    for x, col in enumerate(get_cols(grid)):
        if not any(col):
            for i, galaxy in enumerate(galaxies):
                if galaxy[0] > x:
                    new_galaxies[i][0] += N - 1

    # Calculate the manhattan distances for each galaxy pair
    lengths = []
    for g1, g2 in combinations(new_galaxies, 2):
        lengths.append(abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]))

    # Return the sum
    return sum(lengths)

