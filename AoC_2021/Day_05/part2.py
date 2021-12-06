# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2021.Day_05.commons import parse_input

def main(d:list, bar):
    lines = parse_input(d)
    lined_points = {}
    for line in lines:
        bar()
        points = []
        x1, y1 = line[0]
        x2, y2 = line[1]
        xs, ys = min(x1, x2), min(y1, y2)
        xl, yl = max(x1, x2), max(y1, y2)
        if x1 == x2:  # Check if line is vertical
            for y in range(ys, yl + 1):
                points.append((x1, y))
        elif y1 == y2:  # Check if line is horizontal
            for x in range(xs, xl + 1):
                points.append((x, y1))
        else:
            x = x1
            y = y1
            while True:
                points.append((x, y))
                if x == x2 or y == y2:
                    break
                x += 1 if x < x2 else -1
                y += 1 if y < y2 else -1
        for point in points:
            if point in lined_points.keys():
                lined_points[point] += 1
            else:
                lined_points[point] = 1

    return len([i for i in lined_points.values() if i > 1])
