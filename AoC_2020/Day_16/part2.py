# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2020.Day_16.common_functions import *


def remove_invalid(tickets, fields):
    new_tickets = []
    for ticket in tickets:
        new_ticket = []
        a = True
        for value in ticket:
            if check_valid(value, fields) is False:
                a = False
                break
            new_ticket.append(value)
        if a:
            new_tickets.append(new_ticket)
    return new_tickets


def main(d: list, bar):
    data = parse_input(d)
    valid_pos_fields = {}
    data["tickets"] = remove_invalid(data["tickets"], data["fields"])
    for i in range(len(data["tickets"][0])):
        valid_pos_fields[i] = list(data["fields"].keys())
    for ticket in data["tickets"]:
        for pos, value in enumerate(ticket):
            val = check_valid(value, data["fields"])
            for name in valid_pos_fields[pos]:
                if name not in val:
                    valid_pos_fields[pos].remove(name)
        bar()
    already_found = []
    while True:
        for pos, possibilities in valid_pos_fields.items():
            if len(possibilities) > 1:
                for possibility in possibilities[:]:
                    if possibility in already_found:
                        valid_pos_fields[pos].remove(possibility)
                if len(possibilities) == 1:
                    already_found.append(possibilities[0])
            else:
                already_found.append(possibilities[0])
        br = True
        for possibilities in valid_pos_fields.values():
            if len(possibilities) > 1:
                br = False
        if br:
            break
        bar()
    last_val = 1
    for i, val in enumerate(data["my_ticket"]):
        if valid_pos_fields[i][0].startswith("departure"):
            last_val *= val
    return last_val
