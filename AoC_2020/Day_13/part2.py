# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import ceil

def get_subsequent_timestamp(ids):
    timestamp = 1
    period_incre = 1
    times = []
    last_period = {}
    bus_periods = {}
    while True:
        print(timestamp, len(str(timestamp)), period_incre)
        for id in ids:
            if id != "x":
                id = int(id)
                times.append(id*ceil(timestamp/id))
            else:
                times.append("x")
        if times[0] != timestamp:
            timestamp += period_incre
            times = []
            continue
        incre_count = 0
        bus_count = 0
        for index, time in enumerate(times):
            if time == "x":
                incre_count += 1
                continue
            else:
                bus_count += 1
            if time - timestamp != incre_count:
                break
            if index == len(times) - 1:
                return timestamp
            else:
                if bus_count not in last_period.keys():
                    last_period[bus_count] = timestamp
                elif bus_count not in bus_periods.keys():
                    bus_periods[bus_count] = timestamp - last_period[bus_count]
                    period_incre = bus_periods[bus_count]
            incre_count += 1
        timestamp += period_incre
        times = []


with open("data/test_input.txt", "r") as f:
    data = f.readlines()

print("---\n", get_subsequent_timestamp(data[1].split(",")), "\n---")
