# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import *

def count_invalid(data):
    invalid_tickets = []
    for ticket in data["tickets"]:
        for value in ticket:
            if check_valid(value, data["fields"]) is False:
                invalid_tickets.append(value)
    return sum(invalid_tickets)


print(count_invalid(parse_input("data/input.txt")))
