# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2020.Day_05.common_functions import *


def main(d: list, bar):
    seat_ids = []
    for sequence in d:
        seat_ids.append(get_seat_id(sequence))
    for seat_id in range(max(seat_ids) + 1):
        if seat_id not in seat_ids:
            if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
                return seat_id
        bar()
