# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Pipe:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.distance = None
        self.connections = []
        if shape == "|":  # N-S
            self.connections.append((x, y-1))
            self.connections.append((x, y+1))
        elif shape == "-":  # E-W
            self.connections.append((x-1, y))
            self.connections.append((x+1, y))
        elif shape == "L":  # N-E
            self.connections.append((x, y-1))
            self.connections.append((x+1, y))
        elif shape == "J":  # N-W
            self.connections.append((x, y-1))
            self.connections.append((x-1, y))
        elif shape == "7":  # S-W
            self.connections.append((x, y+1))
            self.connections.append((x-1, y))
        elif shape == "F":  # S-E
            self.connections.append((x, y+1))
            self.connections.append((x+1, y))
        elif shape == "S":  # all?
            # Connections need to be handled via .handle_s(grid) when all other pipes have been prepped
            pass
        elif shape == ".":  # non-pipe
            raise ValueError("It is expected that non-pipes be represented as a 'None'")

    def get_connecting_pipes(self, grid):
        if self.shape == "S":  # If already found, shape would no longer be S
            raise ValueError("Connections for an S pipe must be found via .handle_s(grid) prior to getting connecting pipes")
        pipes = []
        for x, y in self.connections:
            if x < 0 or y < 0:
                continue
            try:
                pipe = grid[y][x]
                if pipe is not None:
                    pipes.append(pipe)
            except IndexError:
                pass

        return pipes

    def handle_s(self, grid):
        for nx, ny in (
                (self.x, self.y-1),
                (self.x, self.y+1),
                (self.x-1, self.y),
                (self.x+1, self.y)
        ):
            if nx < 0 or ny < 0:
                continue
            nn = grid[ny][nx]
            if nn is not None and self in nn.get_connecting_pipes(grid):
                self.connections.append((nx, ny))
        if len(self.connections) != 2:
            raise ValueError("Connections for starting point should always be 2")
        x1, y1 = self.connections[0]
        x2, y2 = self.connections[1]
        if x1 == x2:  # same column, must be vertical pipe
            self.shape = "|"
        elif y1 == y2:  # same row, must be horizontal pipe
            self.shape = "-"
        # The coordinates being checked are simplified because we know the order of changes (y first, then x) from
        #  the for loop. This logic will stop working if the for loop order is changed.
        elif y1 == self.y - 1:  # a pipe facing up
            self.shape = "L" if x2 == self.x + 1 else "J"
        elif y1 == self.y + 1:  # pipe facing down
            self.shape = "F" if x2 == self.x + 1 else "7"

    def __repr__(self):
        return self.shape
