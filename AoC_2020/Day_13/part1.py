# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import ceil

def get_earliest_result(ids, number):
    times = {}
    for id in ids:
        if id != "x":
            id = int(id)
            times[id] = id*ceil(number/id)
    closest_id = min(times, key=lambda x:abs(times.get(x)-number))
    print(closest_id, times[closest_id],times)
    return closest_id * (times[closest_id] - number)


with open("data/input.txt", "r") as f:
    data = f.readlines()

print(get_earliest_result(data[1].split(","),int(data[0])))
