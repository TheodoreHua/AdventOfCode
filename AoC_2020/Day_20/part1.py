# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import floor

class Tile:
    def __init__(self, id, rows):
        self.id = id
        self.row_count = len(rows)
        self.column_count = len(rows[0])
        self.grid = [list(row) for row in rows]

    def rotate(self):
        """Rotate right 90°"""
        rotated = [[""]*self.row_count for i in range(self.column_count)]
        for row in range(self.row_count):
            for column in range(self.column_count):
                rotated[column][-row - 1] = self.grid[row][column]
        self.row_count, self.column_count = self.column_count, self.row_count
        self.grid = rotated

    def flip(self, direction):
        if direction == "horizontal":
            for row in self.grid:
                row.reverse()
        elif direction == "vertical":
            for i in range(floor(self.row_count/2)):
                self.grid[i] = self.grid[-i-1]
                self.grid[-i-1] = self.grid[i]
        else:
            raise ValueError("Invalid Direction \"{}\"".format(direction))

    def get_border(self, direction):
        if direction == "top":
            return self.grid[0]
        elif direction == "right":
            return [self.grid[i][0] for i in range(self.column_count)]
        elif direction == "bottom":
            return self.grid[-1]
        elif direction == "left":
            return [self.grid[i][0] for i in range(self.column_count)]
        else:
            raise ValueError("Invalid Direction \"{}\"".format(direction))

    def __str__(self):
        return "Tile {}\n{}".format(self.id, "\n".join(["".join(row) for row in self.grid])).replace("\n\n","\n")
