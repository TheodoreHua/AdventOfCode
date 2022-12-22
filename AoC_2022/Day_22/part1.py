# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np

def parse_input(d: str):
    """
    :param d: Input data to parse

    :return: Numpy array of the grid (0 is the void, 1 is open space, 2 is a wall. Then a str of the directions
    """
    raw_grid = []
    parsing_grid = True
    directions = None
    for i in d.splitlines():
        if len(i) == 0:
            parsing_grid = False
        elif parsing_grid:
            raw_grid.append(list(i))
        else:
            directions = i
            break

    grid = np.zeros((max(len(i) for i in raw_grid), len(raw_grid)), dtype=np.int8)
    for y, row in enumerate(raw_grid):
        for x, point in enumerate(row):
            if point == ' ':
                grid[x, y] = 0
            elif point == '.':
                grid[x, y] = 1
            elif point == '#':
                grid[x, y] = 2

    assert directions is not None
    parsed_directions = []
    current_number = ""
    for i in directions:
        if i.isdigit():
            current_number += i
        else:
            if len(current_number) > 0:
                parsed_directions.append(int(current_number))
                current_number = ""
            parsed_directions.append(i)

    return grid, parsed_directions

def get_first_nonvoid(arr):
    return np.where(arr != 0)[0][0]

def print_grid(grid):
    for y in range(grid.shape[1]):
        row = ""
        for x in range(grid.shape[0]):
            i = grid[x, y]
            if i == 0:
                row += " "
            elif i == 1:
                row += "."
            elif i == 2:
                row += "#"
        print(repr(row))

def main(d: str, bar):
    grid, directions = parse_input(d)  # 0 = void, 1 = open space, 2 = wall
    curx = np.where(grid[:, 0] == 1)[0][0]
    cury = 0
    facing = 0  # 0 is right, 1 is down, 2 is left, 3 is up
    for i in directions:
        if i == 'R':
            facing = (facing + 1) % 4
        elif i == 'L':
            facing = (facing - 1) % 4
        elif isinstance(i, int):
            pass
        else:
            raise ValueError("Invalid direction")
