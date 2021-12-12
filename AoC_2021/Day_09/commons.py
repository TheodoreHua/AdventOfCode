# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Heightmap:
    def __init__(self, board):
        self.board = [[int(j) for j in i] for i in board]
        self.height = len(self.board)
        self.width = len(self.board[0])

    def adjacent(self, x, y):
        for cx, cy in {(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)}:
            if cx < 0 or cy < 0 or cx > self.width - 1 or cy > self.height - 1:
                continue
            yield cx, cy

    def is_low(self, x, y):
        point = self.board[y][x]
        for cx, cy in self.adjacent(x, y):
            if self.board[cy][cx] <= point:
                return False

        return True

    def risk_level(self, x, y):
        return self.board[y][x] + 1
