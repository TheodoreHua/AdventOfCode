# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2021.Day_09.commons import Heightmap

def main(d:list, bar):
    heightmap = Heightmap(d)
    risk_level = 0
    for x in range(heightmap.width):
        for y in range(heightmap.height):
            if heightmap.is_low(x, y):
                risk_level += heightmap.risk_level(x, y)
            bar()

    return risk_level
