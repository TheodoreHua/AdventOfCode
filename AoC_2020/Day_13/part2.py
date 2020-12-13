# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import ceil

def get_subsequent_timestamp(ids):
    timestamp = 1
    times = []
    while True:
        print(timestamp)
        for id in ids:
            if id != "x":
                id = int(id)
                times.append(id*ceil(timestamp/id))
            else:
                times.append("x")
        if times[0] != timestamp:
            timestamp += 1
            times = []
            continue
        incre_count = 1
        rtrn = False
        for index, time in enumerate(times):
            if index == 0:
                continue
            if time == "x":
                incre_count += 1
                continue
            if time - timestamp != incre_count:
                break
            if index == len(times) - 1:
                rtrn = True
            incre_count += 1
        if rtrn:
            return timestamp
        timestamp += 1
        times = []


with open("data/input.txt", "r") as f:
    data = f.readlines()

print(get_subsequent_timestamp(data[1].split(",")))
