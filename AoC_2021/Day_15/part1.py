# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Grid:
    def __init__(self, data):
        self._grid = [list(map(int, list(i))) for i in data]
        self.goal = (len(self._grid[0]) - 1, len(self._grid) - 1)

    def reached_goal(self, x, y):
        return x == self.goal[0] and y == self.goal[1]

    def get_adjacent(self, x, y, passed=None):
        for cx, cy in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if passed is None or (cx, cy) not in passed:
                if cx < 0 or cy < 0 or cx > self.goal[0] or cy > self.goal[1]:
                    continue
                yield cx, cy

    def get_risk(self, x, y):
        return self._grid[y][x]

    def rep_path(self, path):
        s = ""
        for y, l in enumerate(self._grid):
            for x, i in enumerate(l):
                if (x, y) in path:
                    s += 'X'
                else:
                    s += str(i)
            s += '\n'

        return s.strip()

    def __repr__(self):
        s = ""
        for l in self._grid:
            s += ''.join(map(str, l)) + '\n'

        return s.strip()

    def __str__(self):
        return self.__repr__()


def create_score(x: int, y: int, nx: int, ny: int, risk: int):
    """Generate weight score for a potential path point

    :param x: Current x location of cursor
    :param y: Current y location of cursor
    :param nx: X location to calculate score of
    :param ny: Y location to calculate score of
    :param risk: Risk value of calculator coordinate
    """
    multiplier = 1
    if nx < x:
        multiplier += 1
    if ny < y:
        multiplier += 1
    if nx == x:
        multiplier += 0.3
    if ny == y:
        multiplier += 0.3
    return risk * multiplier


def main(d: list, bar):
    grid = Grid(d)
    path = [(0, 0)]
    x = 0
    y = 0
    while True:
        best = (None, float('inf'))
        for px, py in grid.get_adjacent(x, y, path):
            if grid.reached_goal(px, py):
                best = ((px, py), float('inf'))
                break
            s = create_score(x, y, px, py, grid.get_risk(px, py))
            if s < best[1]:
                best = ((px, py), s)
        x, y = best[0]
        path.append((x, y))
        if grid.reached_goal(x, y):
            break
        print(grid)
        print(grid.rep_path(path))
        bar()

    return sum([grid.get_risk(x, y) for x, y in path])
