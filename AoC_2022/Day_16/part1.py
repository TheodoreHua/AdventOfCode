# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from functools import lru_cache

from .commons import parse_input


@lru_cache(maxsize=None)
def get_maximum_flow(valve, bar, time_left=30, opened_valves=None):
    """Credit to /u/nthistle (again) for figuring out this solution logic"""
    # Create opened_valves if not passed in
    if opened_valves is None:
        opened_valves = tuple()
    if time_left <= 0:
        return 0
    largest = 0
    pos_val = valve.flow_rate * (time_left - 1)  # The maximum flow rate if we open this valve
    for v in valve.to:
        # If this valve is not already opened, and it makes sense to open it (will actually relieve pressure), try to open it
        if valve not in opened_valves and pos_val > 0:
            # Calculate the maximum flow rate if we open this valve, then store if larger than the current maximum
            largest = max(largest, pos_val + get_maximum_flow(v, bar, time_left - 2, opened_valves + (valve,)))
        # Calculate the maximum flow rate if we don't open this valve. If larger, store it
        largest = max(largest, get_maximum_flow(v, bar, time_left - 1, opened_valves))
        bar()
    return largest


def main(d: list, bar):
    return get_maximum_flow(parse_input(d)["AA"], bar)
