# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2021.Day_11.commons import *


def main(d: list, bar):
    octopuses = [[Octopus(int(j)) for j in i] for i in d]
    mh, mw = len(octopuses), len(octopuses[0])
    total_octopus = mh * mw
    step = 1
    while True:
        flashes = 0
        for l in octopuses:
            for octopus in l:
                octopus.increment()
        for y in range(mh):
            for x in range(mw):
                o = octopuses[y][x]
                if o.should_flash():
                    o.flash()
                    flash_adjacent(octopuses, x, y)
        for l in octopuses:
            for octopus in l:
                if octopus.is_flashed():
                    octopus.deplete()
                    octopus.reset()
                    flashes += 1
        if flashes == total_octopus:
            return step
        else:
            step += 1
        bar()
