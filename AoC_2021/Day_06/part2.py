# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

"""I tried to brute force using Day 1 on a high-powered compute server w/ 92 GB of RAM and a fast CPU...didn't work.
Heck part 2, IHMS. Onto r/adventofcode in desperation we go (full disclosure, the below code was not made by me but
rather /u/JohnnyWobble over on r/AdventOfCode. Good job to them!)"""


def main(d: list, bar):
    d = list(map(int, d[0].split(',')))
    fish = [d.count(i) for i in range(9)]
    for _ in range(256):
        n = fish.pop(0)
        fish[6] += n
        fish.append(n)
        bar()

    return sum(fish)
