# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d:list, bar):
    crabs = list(map(int, d[0].split(',')))
    mapped_positions = {}
    sc, lc = min(crabs), max(crabs)
    for i in range(sc, lc + 1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - i)
        mapped_positions[i] = fuel
        bar()

    return min(mapped_positions.values())
