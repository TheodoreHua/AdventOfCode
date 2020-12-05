# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import *

def get_highest_seat_id(sequence_set):
    seat_ids = []
    for sequence in sequence_set:
        seat_ids.append(get_seat_id(sequence))
    return max(seat_ids)


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(get_highest_seat_id(data))
