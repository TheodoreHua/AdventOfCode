# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import ceil


def main(d: list, bar):
    ids = d[1].split(',')
    timestamp = 1
    period_incre = 1
    times = []
    last_period = {}
    bus_periods = {}
    while True:
        bar.text("TS: {:,}".format(timestamp))
        # print(timestamp, len(str(timestamp)), period_incre)
        for i in ids:
            if i != "x":
                i = int(i)
                times.append(i * ceil(timestamp / i))
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
        bar()
