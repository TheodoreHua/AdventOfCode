# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import floor

DEGREES = {-0: "E", -90: "S", -180: "W", -270: "N",
           0: "E", 90: "N", 180: "W", 270: "S"}

def get_manhattan(instructions):
    coordinates = [0, 0]  # Reversed, NS/Y in index 0, EW/X on index 1
    rotation = 0
    for instruction in instructions:
        print(instruction, "NS", coordinates[0], "coordinates[1]", coordinates[1], "Rotation", rotation)
        instruc = instruction[:1]
        num = int(instruction[1:])
        if instruc == "N":
            coordinates[0] += num
        elif instruc == "S":
            coordinates[0] -= num
        elif instruc == "E":
            coordinates[1] += num
        elif instruc == "W":
            coordinates[1] -= num
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
                coordinates[0] += num
            elif DEGREES[rotation] == "S":
                coordinates[0] -= num
            elif DEGREES[rotation] == "E":
                coordinates[1] += num
            elif DEGREES[rotation] == "W":
                coordinates[1] -= num
            else:
                print("Invalid Degree")
        else:
            print("Invalid Coordinates")
    return abs(coordinates[0]) + abs(coordinates[1])


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(get_manhattan(data))
