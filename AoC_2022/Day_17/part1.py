# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np

def move_rock(rock, grid, x_diff, y_diff):
    # If the rock would run into a wall, nothing happens
    # If the rock would run into another rock, nothing happens
    # If the rock would run into the bottom of the grid, nothing happens
    if min([x + x_diff for x, y in rock]) < 0:
        return rock, grid
    if max([x + x_diff for x, y in rock]) >= grid.shape[0] - 1:
        return rock, grid
    for x, y in rock:
        grid[x, y] = 0
    for x, y in rock:
        grid[x + x_diff, y + y_diff] = 1
    return [(x + x_diff, y + y_diff) for x, y in rock], grid

def simulate_rock_movement(rock, grid, jet_pattern):
    while True:
        # print("Simulating")
        for direction in jet_pattern:
            if direction == "<":
                rock, grid = move_rock(rock, grid, -1, 0)
            elif direction == ">":
                rock, grid = move_rock(rock, grid, 1, 0)
            # Check if rock hit the bottom or another rock
            if max([y for x, y in rock]) >= grid.shape[1] - 1:
                return grid
            for x, y in rock:
                if grid[x, y + 1] == 1:
                    return grid
        rock, grid = move_rock(rock, grid, 0, 1)

def get_tallest_rock_y(grid):
    # print("Searching")
    # print("getting tallest rock")
    # for i in range(grid.shape[1] - 1):
    #     if grid[: i,].sum() > 0:
    #         return i
    # return grid.shape[0] - 1
    # Get the first row that has a 1 in it
    for y in range(grid.shape[1]):
        if grid[:, y].sum() > 0:
            return y
    return grid.shape[1] - 1


def main(d: str, bar):
    """F[[2022]]"""
    jet_pattern = list(d.strip())
    grid = np.zeros((8, 5000), dtype=int)  # The maximum height of all rocks stacked is 4448. 5000 for buffer.
    for i in range(1, 2023):
        i_mod = i % 5
        spawn_y = get_tallest_rock_y(grid) - 4
        if i_mod == 1:
            rock = [  # -
                (2, spawn_y),
                (3, spawn_y),
                (4, spawn_y),
                (5, spawn_y),
            ]
        elif i_mod == 2:
            rock = [  # +
                (3, spawn_y - 2),
                (2, spawn_y - 1),
                (3, spawn_y - 1),
                (4, spawn_y - 1),
                (3, spawn_y),
            ]
        elif i_mod == 3:
            rock = [  # J
                (4, spawn_y - 2),
                (4, spawn_y - 1),
                (2, spawn_y),
                (3, spawn_y),
                (4, spawn_y),
            ]
        elif i_mod == 4:
            rock = [  # I
                (2, spawn_y - 3),
                (2, spawn_y - 2),
                (2, spawn_y - 1),
                (2, spawn_y),
            ]
        elif i_mod == 0:
            rock = [  # O
                (2, spawn_y - 1),
                (3, spawn_y - 1),
                (2, spawn_y),
                (3, spawn_y),
            ]
        else:
            raise Exception("This should never happen!")
        grid = simulate_rock_movement(rock, grid, jet_pattern)
        bar()

    for y in range(grid.shape[1]):
        for x in range(grid.shape[0]):
            print("#" if grid[x, y] == 1 else ".", end="")
        print()
    return grid.shape[1] - get_tallest_rock_y(grid)
