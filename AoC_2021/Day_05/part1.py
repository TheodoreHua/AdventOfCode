# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d:list, bar):
    lines = [[(int(k) for k in j.split(',')) for j in i.split(" -> ")] for i in d]
    lined_points = {}
    for line in lines:
        bar()
        points = []
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 == x2:  # Check if line is vertical
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x1, y))
        elif y1 == y2:  # Check if line is horizontal
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points.append((x, y1))
        else:
            continue
        for point in points:
            if point in lined_points.keys():
                lined_points[point] += 1
            else:
                lined_points[point] = 1

    return len([i for i in lined_points.values() if i > 1])
