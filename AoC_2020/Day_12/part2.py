# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import floor, sin, cos, sqrt, atan, asin, radians

DEGREES = {-0: "E", -90: "S", -180: "W", -270: "N",
           0: "E", 90: "N", 180: "W", 270: "S"}

def rotate(origin, point, degrees):
    ox, oy = origin
    px, py = point
    degree = radians(degrees)
    r = sqrt(((px - ox) ** 2) + ((py - oy) ** 2))
    # FIXME: asin and atan returns different results, both are wrong
    radian = asin((py - oy) / r)
    # radian = atan((py - oy) / (px - ox))
    newx = ox + r * cos(degree + radian)
    newy = oy + r * sin(degree + radian)
    return [newx, newy]

def get_manhattan(instructions):
    ship_coordinates = [0, 0]
    waypoint_coordinates = [10, 1]
    rotation = 0
    for instruction in instructions:
        instruc = instruction[:1]
        num = int(instruction[1:])
        if instruc == "N":
            waypoint_coordinates[1] += num
        elif instruc == "S":
            waypoint_coordinates[1] -= num
        elif instruc == "E":
            waypoint_coordinates[0] += num
        elif instruc == "W":
            waypoint_coordinates[0] -= num
        elif instruc == "L":
            # FIXME: Seems that instruction sets with a instruction that rotates
            #  left somehow causes incorrect values, with right being fine
            # https://lambda.sx/L2d.png
            rotation += num
            if rotation >= 360:
                rotation = rotation - 360 * floor(rotation / 360)
            rotated = rotate(ship_coordinates, waypoint_coordinates, num)
            waypoint_coordinates = [round(rotated[0]), round(rotated[1])]
        elif instruc == "R":
            rotation -= num
            if rotation <= -360:
                rotation = rotation - 360 * floor(rotation / 360)
            # print(waypoint_coordinates)
            rotated = rotate(ship_coordinates, waypoint_coordinates, -num)
            waypoint_coordinates = [round(rotated[0]), round(rotated[1])]
            # print(waypoint_coordinates)
        elif instruc == "F":
            x_diff = waypoint_coordinates[0] - ship_coordinates[0]
            y_diff = waypoint_coordinates[1] - ship_coordinates[1]
            for i in range(num):
                ship_coordinates = waypoint_coordinates[:]
                waypoint_coordinates[0] += x_diff
                waypoint_coordinates[1] += y_diff
        print(instruction, "SX", ship_coordinates[0], "SY", ship_coordinates[1], "WX", waypoint_coordinates[0],
              "WY", waypoint_coordinates[1],"Rotation", rotation, ":", DEGREES[rotation], "SWDX",
              waypoint_coordinates[0] - ship_coordinates[0], "SWDY", waypoint_coordinates[1] - ship_coordinates[1])
    # print(ship_coordinates)
    return abs(ship_coordinates[0]) + abs(ship_coordinates[1])


with open("data/test_input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(get_manhattan(data))
