# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

INPUT_REGEX = compile(
    r"Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)")


def main(d: list, bar, row=2000000):
    # Actually commenting the code this time so future me can figure out what the heck is going on
    row = int(row)  # Convert the row to an int -- when passed in via runner it's a string
    beacon_xs = set()  # Set of all beacon x coordinates, it is a set to prevent duplicates
    nb_ranges = []  # List of ranges that cannot be a beacon
    bar.text("Generating zones")
    for i in d:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, INPUT_REGEX.match(i).groups())
        if beacon_y == row:  # If the beacon is on the row we're looking for, add the beacon X value to the set
            beacon_xs.add(beacon_x)  # this is used to exclude beacons from the ranges later
        manhattan = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y) - abs(sensor_y - row)
        nb_ranges.append((sensor_x - manhattan, sensor_x + manhattan + 1))  # range of X values that are not beacons
        bar()

    bar.text("Generating final zone")
    # Calculate the length by subtracting the number of beacon X values from the total number of X values in the ranges
    return len(range(min(nb_ranges)[0], max(nb_ranges, key=lambda m: m[1])[1])) - len(beacon_xs)
