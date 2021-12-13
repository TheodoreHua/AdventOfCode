# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Grid:
    def __init__(self, starting_coordinates):
        self.dots = starting_coordinates
        self.max_width = max(starting_coordinates)[0] + 1
        self.max_height = max(starting_coordinates, key=lambda i: i[1])[1] + 1

    def fold(self, axis, coord):
        new_dots = []
        for dot in self.dots:
            if dot[axis] > coord:
                diff = dot[axis] - coord
                dot = [coord - diff, dot[1]] if axis == 0 else [dot[0], coord - diff]
            if dot not in new_dots:
                new_dots.append(dot)
        self.dots = new_dots
        self.max_width = max(self.dots)[0] + 1
        self.max_height = max(self.dots, key=lambda i: i[1])[1] + 1

    def __str__(self):
        s = (lambda x=['.' for _ in range(self.max_width)]: [x[:] for _ in range(self.max_height)])()
        for dot in self.dots:
            s[dot[1]][dot[0]] = '#'

        return '\n'.join([''.join(i) for i in s])

    def __repr__(self):
        return self.__str__()


def parse_input(d):
    coordinates = []
    folds = []
    for line in d:
        if line == '':
            continue
        elif line.startswith('fold along '):
            v = line.lstrip('fold along ').split('=')
            folds.append((0 if v[0] == 'x' else 1, int(v[1])))
        else:
            coordinates.append([int(i) for i in line.split(',')])

    return Grid(coordinates), folds
