# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

shape_map = {
    0: "O",
    1: "-",
    2: "+",
    3: "J",
    4: "I",
}


class Rock:
    def __init__(self, bottom_y, shape):
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
                (3, bottom_y + 2),
                (2, bottom_y + 1),
                (3, bottom_y + 1),
                (4, bottom_y + 1),
                (3, bottom_y),
            ]
        elif shape == "J":
            self._rock = [
                (4, bottom_y + 2),
                (4, bottom_y + 1),
                (2, bottom_y),
                (3, bottom_y),
                (4, bottom_y),
            ]
        elif shape == "I":
            self._rock = [
                (2, bottom_y + 3),
                (2, bottom_y + 2),
                (2, bottom_y + 1),
                (2, bottom_y),
            ]
        elif shape == "O":
            self._rock = [
                (2, bottom_y + 1),
                (3, bottom_y + 1),
                (2, bottom_y),
                (3, bottom_y),
            ]
        else:
            raise ValueError("Invalid shape")

    def __repr__(self):
        return f"{self.shape} ({self._rock})"

    def __str__(self):
        return self.shape

    def can_move_down(self, depths):
        for x, y in self._rock:
            if y - 1 <= depths[x]:
                return False
        return True

    def can_move_lr(self, depths, direction):
        for x, y in self._rock:
            new_x = x + direction
            if new_x < 0 or new_x > len(depths) - 1:
                return False
            if y <= depths[new_x]:
                return False
        return True

    def update_depths(self, depths):
        for x, y in self._rock:
            if y > depths[x]:
                depths[x] = y
        return depths

    def move_down(self):
        for i, (x, y) in enumerate(self._rock):
            self._rock[i] = (x, y - 1)

    def move_lr(self, direction):
        for i, (x, y) in enumerate(self._rock):
            self._rock[i] = (x + direction, y)

    def simulate_movement(self, depths, jet_pattern, jet_index):
        while True:
            if self.can_move_lr(depths, jet_pattern[jet_index]):
                self.move_lr(jet_pattern[jet_index])
            jet_index = (jet_index + 1) % len(jet_pattern)
            if not self.can_move_down(depths):
                return jet_index
            self.move_down()


def main(d: str, bar):
    """F[[2022]]"""
    jet_pattern = [-1 if i == "<" else 1 for i in d.strip()]
    depths = [0 for i in range(7)]
    jet_index = 0
    top = 0
    for i in range(1, 2023):
        i_mod = i % 5
        rock = Rock(top + 3, shape_map[i_mod])
        jet_index = rock.simulate_movement(depths, jet_pattern, jet_index)
        depths = rock.update_depths(depths)
        top = max(depths) + 1
        bar()
        print(depths)
        if i == 2:
            break
    return max(depths)
