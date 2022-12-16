# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

INPUT_REGEX = compile(
    r"Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)")


def main(d: list, bar, max_bound=4000000):
    """Credit to /u/nthistle & /u/i_have_no_biscuits for the idea of looking for diagonal intersections."""
    max_bound = int(max_bound)  # Convert the maximum bound to an int -- when passed in via runner it's a string
    manhattans = {}  # Store all manhattan distances for each sensor
    bar.text("Creating manhattans")
    for i in d:  # Parse the input and add manhattan distances to the dict
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, INPUT_REGEX.match(i).groups())
        manhattans[(sensor_x, sensor_y)] = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        bar()

    lines_l = set()  # Store all diagonals on the left side of the sensor
    lines_r = set()  # Store all diagonals on the right side of the sensor
    bar.text("Creating lines")
    for ((x, y), manhattan) in manhattans.items():  # Calculate the boundary lines for each sensor
        # All manhattan distances are increased by 1, so we get the boundaries of each "no beacon zone", rather than the edges
        manhattan_i, manhattan_d = manhattan + 1, manhattan - 1
        lines_l.add(-x + y + manhattan_i)
        lines_l.add(-x - y - manhattan_d)
        lines_r.add(x + y + manhattan_i)
        lines_r.add(x + y - manhattan_d)
        bar()

    for l in lines_l:
        for r in lines_r:
            intersect_x, intersect_y = (r - l) // 2, (r + l) // 2  # Calculate the intersection point
            bar.text("Checking intersection at {}, {} for distress beacon".format(intersect_x, intersect_y))
            bar()
            # Check if the intersection is within the bounds of the beacon
            if 0 < intersect_x < max_bound and 0 < intersect_y < max_bound:
                # Check that the intersection is not inside a "no beacon zone". (manhattan distance between the
                # intersection and the sensor is greater than that of the sensor and beacon)
                if all(abs(intersect_x - k[0]) + abs(intersect_y - k[1]) > v for k, v in manhattans.items()):
                    return intersect_x * 4000000 + intersect_y  # Calculate the tuning frequency
