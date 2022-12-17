# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np

shape_map = {
    0: "O",
    1: "-",
    2: "+",
    3: "J",
    4: "I",
}


class Rock:
    def __init__(self, bottom_y, shape, grid):
        self.bottom_y = bottom_y
        self.shape = shape
        if shape == "-":
            self._rock = [
                (2, bottom_y),
                (3, bottom_y),
                (4, bottom_y),
                (5, bottom_y),
            ]
        elif shape == "+":
            self._rock = [
                (3, bottom_y - 2),
                (2, bottom_y - 1),
                (3, bottom_y - 1),
                (4, bottom_y - 1),
                (3, bottom_y),
            ]
        elif shape == "J":
            self._rock = [
                (4, bottom_y - 2),
                (4, bottom_y - 1),
                (2, bottom_y),
                (3, bottom_y),
                (4, bottom_y),
            ]
        elif shape == "I":
            self._rock = [
                (2, bottom_y - 3),
                (2, bottom_y - 2),
                (2, bottom_y - 1),
                (2, bottom_y),
            ]
        elif shape == "O":
            self._rock = [
                (2, bottom_y - 1),
                (3, bottom_y - 1),
                (2, bottom_y),
                (3, bottom_y),
            ]
        else:
            raise ValueError("Invalid shape")
        for x, y in self._rock:
            grid[y, x] = True

    def __repr__(self):
        return f"{self.shape} ({self._rock})"

    def __str__(self):
        return self.shape

    def get_tallest_point(self):
        return min(y for x, y in self._rock)

    def can_move_down(self, grid):
        for x, y in self._rock:
            new_y = y + 1
            if not 0 <= new_y <= grid.shape[0] - 1:
                return False
            if grid[new_y, x] and (x, new_y) not in self._rock:
                return False
        return True

    def can_move_lr(self, grid, direction):
        for x, y in self._rock:
            new_x = x + direction
            if not 0 <= new_x <= grid.shape[1] - 1:
                return False
            if grid[y, new_x] and (new_x, y) not in self._rock:
                return False
        return True

    def move_down(self, grid):
        self.bottom_y += 1
        for i, (x, y) in enumerate(self._rock):
            self._rock[i] = (x, y + 1)
            grid[y, x] = False
        for x, y in self._rock:
            grid[y, x] = True

    def move_lr(self, grid, direction):
        for i, (x, y) in enumerate(self._rock):
            self._rock[i] = (x + direction, y)
            grid[y, x] = False
        for x, y in self._rock:
            grid[y, x] = True

    def simulate_movement(self, grid, jet_pattern, jet_index):
        while True:
            if self.can_move_lr(grid, jet_pattern[jet_index]):
                self.move_lr(grid, jet_pattern[jet_index])
            jet_index = (jet_index + 1) % len(jet_pattern)
            if not self.can_move_down(grid):
                return jet_index
            self.move_down(grid)


def main(d: str, bar):
    """F[[2022]]"""
    jet_pattern = [-1 if i == "<" else 1 for i in d.strip()]
    grid = np.zeros((5000, 7), dtype=bool)  # The maximum height of all rocks stacked is 4448. 5000 for buffer.
    jet_index = 0
    top = grid.shape[0] - 1
    for i in range(1, 2023):
        i_mod = i % 5
        rock = Rock(top - 3, shape_map[i_mod], grid)
        jet_index = rock.simulate_movement(grid, jet_pattern, jet_index)
        rock_tallest = rock.get_tallest_point() - 1
        if rock_tallest < top:
            top = rock_tallest
        bar()
        for y in range(-10, 0):
            for x in range(7):
                print("#" if grid[y, x] else ".", end="")
            print()
        if i == 2:
            break
    return grid.shape[0] - 1 - top
