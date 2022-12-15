# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

INPUT_REGEX = compile(r"Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)")

def main(d: list, bar, max_x=4000000, max_y=4000000):
    # What in the heck is P2? I'm going to work on this tomorrow when I'm more awake.
    raise NotImplementedError("P2 is not implemented yet.")
