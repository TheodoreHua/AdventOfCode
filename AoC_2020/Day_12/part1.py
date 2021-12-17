# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import floor

DEGREES = {-0: "E", -90: "S", -180: "W", -270: "N",
           0: "E", 90: "N", 180: "W", 270: "S"}


def main(d: list, bar):
    coordinates = [0, 0]
    rotation = 0
    for instruction in d:
        instruc = instruction[:1]
        num = int(instruction[1:])
        if instruc == "N":
            coordinates[1] += num
        elif instruc == "S":
            coordinates[1] -= num
        elif instruc == "E":
            coordinates[0] += num
        elif instruc == "W":
            coordinates[0] -= num
        elif instruc == "R":
            rotation -= num
            if rotation <= -360:
                rotation = rotation - 360 * floor(rotation / 360)
        elif instruc == "L":
            rotation += num
            if rotation >= 360:
                rotation = rotation - 360 * floor(rotation / 360)
        elif instruc == "F":
            if DEGREES[rotation] == "N":
                coordinates[1] += num
            elif DEGREES[rotation] == "S":
                coordinates[1] -= num
            elif DEGREES[rotation] == "E":
                coordinates[0] += num
            elif DEGREES[rotation] == "W":
                coordinates[0] -= num
            else:
                print("Invalid Degree")
        else:
            print("Invalid Coordinates")
        bar()
    return abs(coordinates[0]) + abs(coordinates[1])
