# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Lanternfish:
    def __init__(self, timer):
        self.timer = timer

    def age(self):
        if self.timer == 0:
            self.timer = 6
            return Lanternfish(8)
        else:
            self.timer -= 1

def lanternfish_simulation(d:list, bar, length):
    lanternfishes = [Lanternfish(int(i)) for i in d[0].split(',')]
    for _ in range(length):
        new = []
        for lanternfish in lanternfishes:
            r = lanternfish.age()
            if r is not None:
                new.append(r)
        lanternfishes = lanternfishes + new
        bar()

    return len(lanternfishes)
