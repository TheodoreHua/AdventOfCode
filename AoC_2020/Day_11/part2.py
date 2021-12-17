# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2020.Day_11.common_functions import *

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, +1),
    (1, -1), (1, 0), (1, 1)
]


def check_occupy(row_index, seat_index, rows):
    adjacent_full = 0
    for row, seat in DIRECTIONS:
        row_pointer = row_index + row
        seat_pointer = seat_index + seat
        while (row_pointer >= 0 if row == -1 else row_pointer < len(rows)) \
                and (seat_pointer >= 0 if seat == -1 else seat_pointer < len(rows[row_index])):
            s = check_seat(rows[row_pointer][seat_pointer])
            if s is not None:
                if s is True:
                    adjacent_full += 1
                    break
                else:
                    break
            row_pointer += row
            seat_pointer += seat
    return adjacent_full


def check_empty(row_index, seat_index, rows):
    adjacent_empty = 0
    for row, seat in DIRECTIONS:
        row_pointer = row_index + row
        seat_pointer = seat_index + seat
        while (row_pointer >= 0 if row == -1 else row_pointer < len(rows)) \
                and (seat_pointer >= 0 if seat == -1 else seat_pointer < len(rows[row_index])):
            s = check_seat(rows[row_pointer][seat_pointer])
            if s is not None:
                if s is False:
                    adjacent_empty += 1
                    break
                else:
                    break
            row_pointer += row
            seat_pointer += seat
        else:
            adjacent_empty += 1
    return adjacent_empty


def replace_empty(row_index, rows):
    new_str = ""
    for i, seat in enumerate(rows[row_index]):
        if seat != ".":
            empty_count = check_empty(row_index, i, rows)
            if empty_count == 8:
                new_str += "#"
            else:
                new_str += seat
        else:
            new_str += seat
    return new_str


def replace_occupy(row_index, rows):
    new_str = ""
    for i, seat in enumerate(rows[row_index]):
        if seat != ".":
            occupy_count = check_occupy(row_index, i, rows)
            if occupy_count >= 5:
                new_str += "L"
            else:
                new_str += seat
        else:
            new_str += seat
    return new_str


def replace_occupy_rows(rows):
    new_rows = rows[:]
    for index in range(len(rows)):
        new_rows[index] = replace_occupy(index, rows)
    return new_rows


def replace_empty_rows(rows):
    new_rows = rows[:]
    for index in range(len(rows)):
        new_rows[index] = replace_empty(index, rows)
    return new_rows


def main(d: list, bar):
    cont_count = 0
    while True:
        orig_rows = d
        if cont_count % 2 == 0:
            d = replace_empty_rows(d)
        else:
            d = replace_occupy_rows(d)
        if d == orig_rows:
            break
        cont_count += 1
        bar()
    occupy_count = 0
    for row in d:
        for seat in row:
            if check_seat(seat) is True:
                occupy_count += 1
        bar()
    return occupy_count
