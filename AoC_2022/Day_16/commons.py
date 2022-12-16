# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

INPUT_REGEX = compile(
    r"Valve (?P<valve>\w+) has flow rate=(?P<flow_rate>\d+); tunnels? leads? to valves? (?P<leads_to>.*)")


class Valve:
    def __init__(self, name, flow_rate, to):
        self.name = name
        self.flow_rate = flow_rate
        self.to = to


def parse_input(d: list):
    valves = {}
    for i in d:
        valve, flow_rate, leads_to = INPUT_REGEX.fullmatch(i).groups()
        leads_to = leads_to.split(", ")
        valves[valve] = Valve(valve, int(flow_rate), leads_to)

    for valve in valves.values():
        valve.to = [valves[v] for v in valve.to]

    return valves
