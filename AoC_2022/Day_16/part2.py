# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import parse_input


# Starts at 25 rather than 26 as the first valve shouldn't be opened, and this removes travel time to the next valve
def get_maximum_flow(valve_person, valve_elephant, valves, bar, time_left=25, state=None, seen=None):
    """Credit to /u/hugh_tc for figuring out this solution logic"""
    # FIXME: The example input is off by 1, but the actual input works...

    # Create state and seen dicts if not passed in
    if state is None:
        state = {}
    if seen is None:
        seen = {}
    # Calculate the current flow rate at this point in time, considering the valves we have open
    flow_rate = sum(k.flow_rate * v for k, v in state.items() if v is not None)
    if time_left <= 0:
        return flow_rate

    # If we have already seen this state before, and the current position is the same or worse, skip it
    if seen.get((valve_person, valve_elephant, time_left), -1) >= flow_rate:
        return 0
    # Otherwise, store the current flow rate into seen, so we can skip this state if we see it again
    seen[(valve_person, valve_elephant, time_left)] = flow_rate

    largest = 0
    for person in [valve_person] + valve_person.to:
        # If this is the current valve we are at, the valve is not already open, and it makes sense to open it,
        # then open the valve (this is then used in following calls for the elephant). If it doesn't make sense,
        # then move onto the next valve
        if person == valve_person:
            if state.get(valve_person) is None and valve_person.flow_rate > 0:
                state[valve_person] = time_left
            else:
                continue

        for elephant in [valve_elephant] + valve_elephant.to:
            bar()
            # If this is the current valve we are at, the valve is not already open, and it makes sense to open it,
            # then open the valve (to calculate the max pressure relief if we do open it). If it doesn't make sense,
            # then move onto the next valve
            if elephant == valve_elephant:
                if state.get(valve_elephant) is None and valve_elephant.flow_rate > 0:
                    state[valve_elephant] = time_left
                else:
                    continue

            # Calculate the maximum flow rate if we open this valve, then store if larger than the current maximum
            largest = max(largest, get_maximum_flow(person, elephant, valves, bar, time_left - 1, state, seen))

            # Close the valve for future calculations (adjacent valves), this way we calculate both if we open it
            # (this iteration) and if we don't (future iterations). This covers all cases.
            if elephant == valve_elephant:
                state[valve_elephant] = None

        # Close the valve for future calculations (adjacent valves), this way we calculate both if we open it
        # (this iteration) and if we don't (future iterations). This covers all cases.
        if person == valve_person:
            state[valve_person] = None

    return largest


def main(d: list, bar):
    valves = parse_input(d)

    return get_maximum_flow(valves["AA"], valves["AA"], valves, bar)
