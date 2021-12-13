# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False

    def reset(self):
        self.flashed = False

    def flash(self):
        self.flashed = True

    def is_flashed(self):
        return self.flashed

    def deplete(self):
        if self.flashed:
            self.energy = 0

    def increment(self):
        self.energy += 1

    def should_flash(self):
        return self.energy > 9 and not self.flashed


def flash_adjacent(octopuses, x, y):
    adjacent = [
        (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
        (x - 1, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1)
    ]
    for cx, cy in adjacent:
        if cx < 0 or cy < 0:
            continue
        try:
            if not octopuses[cy][cx].is_flashed():
                o = octopuses[cy][cx]
                o.increment()
                if o.should_flash():
                    o.flash()
                    flash_adjacent(octopuses, cx, cy)
        except IndexError:
            continue
