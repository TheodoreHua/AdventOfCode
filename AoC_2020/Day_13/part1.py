# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import ceil


def main(d: list, bar):
    number = int(d[0])
    ids = d[1].split(',')
    times = {}
    for i in ids:
        if i != "x":
            i = int(i)
            times[i] = i * ceil(number / i)
        bar()
    closest_id = min(times, key=lambda x: abs(times.get(x) - number))
    # print(closest_id, times[closest_id], times)
    return closest_id * (times[closest_id] - number)
