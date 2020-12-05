# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import ceil

def get_num(sequence, upper, up_char):
    pointer = 0
    for i in sequence:
        diff = ceil(upper / 2)
        upper = diff
        if i == up_char:
            pointer += diff
    return pointer

def get_seat_id(sequence):
    row = get_num(sequence[:7], 127, "B")
    column = get_num(sequence[7:], 7, "R")
    return row * 8 + column

def get_missing_seat_id(sequence_set):
    seat_ids = []
    for sequence in sequence_set:
        seat_ids.append(get_seat_id(sequence))
    for seat_id in range(max(seat_ids) + 1):
        if seat_id not in seat_ids:
            if seat_id + 1 in seat_ids and seat_id -1 in seat_ids:
                return seat_id


with open("../data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(get_missing_seat_id(data))
