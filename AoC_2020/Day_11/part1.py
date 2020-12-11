# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import *

def check_occupy(row, index, forward_row=None, backward_row=None, align=None):
    adjacent_full = 0
    if align == "left":
        if forward_row is not None:
            for seat in forward_row[0:index + 2]:
                if check_seat(seat) is True:
                    adjacent_full += 1
        for i, seat in enumerate(row[0:index + 2]):
            if check_seat(seat) is True and i != 0:
                adjacent_full += 1
        if backward_row is not None:
            for seat in backward_row[0:index + 2]:
                if check_seat(seat) is True:
                    adjacent_full += 1
    elif align == "right":
        if forward_row is not None:
            for seat in forward_row[index-1:len(forward_row)]:
                if check_seat(seat) is True:
                    adjacent_full += 1
        for i, seat in enumerate(row[index-1:len(row)]):
            if check_seat(seat) is True and i != 1:
                adjacent_full += 1
        if backward_row is not None:
            for seat in backward_row[index-1:len(backward_row)]:
                if check_seat(seat) is True:
                    adjacent_full += 1
    else:
        if forward_row is not None:
            for seat in forward_row[index-1:index+2]:
                if check_seat(seat) is True:
                    adjacent_full += 1
        for i, seat in enumerate(row[index-1:index+2]):
            if check_seat(seat) is True and i != 1:
                adjacent_full += 1
        if backward_row is not None:
            for seat in backward_row[index-1:index+2]:
                if check_seat(seat) is True:
                    adjacent_full += 1
    return adjacent_full

def check_empty(row, index, forward_row=None, backward_row=None, align=None):
    adjacent_empty = 0
    if align == "left":
        if forward_row is not None:
            adjacent_empty += 1
            for seat in forward_row[0:index + 2]:
                if check_seat(seat) in [False, None]:
                    adjacent_empty += 1
        else:
            adjacent_empty += 3
        adjacent_empty += 1
        for i, seat in enumerate(row[0:index + 2]):
            if check_seat(seat) in [False, None] and i != 0:
                adjacent_empty += 1
        if backward_row is not None:
            adjacent_empty += 1
            for seat in backward_row[0:index + 2]:
                if check_seat(seat) in [False, None]:
                    adjacent_empty += 1
        else:
            adjacent_empty += 3
    elif align == "right":
        if forward_row is not None:
            adjacent_empty += 1
            for seat in forward_row[index - 1:len(forward_row)]:
                if check_seat(seat) in [False, None]:
                    adjacent_empty += 1
        else:
            adjacent_empty += 3
        adjacent_empty += 1
        for i, seat in enumerate(row[index - 1:len(row)]):
            if check_seat(seat) in [False, None] and i != 1:
                adjacent_empty += 1
        if backward_row is not None:
            adjacent_empty += 1
            for seat in backward_row[index - 1:len(backward_row)]:
                if check_seat(seat) in [False, None]:
                    adjacent_empty += 1
        else:
            adjacent_empty += 3
    else:
        if forward_row is not None:
            for seat in forward_row[index - 1:index + 2]:
                if check_seat(seat) in [False, None]:
                    adjacent_empty += 1
        else:
            adjacent_empty += 3
        for i, seat in enumerate(row[index - 1:index+2]):
            if check_seat(seat) in [False, None] and i != 1:
                adjacent_empty += 1
        if backward_row is not None:
            for seat in backward_row[index - 1:index + 2]:
                if check_seat(seat) in [False, None]:
                    adjacent_empty += 1
        else:
            adjacent_empty += 3
    return adjacent_empty

def replace_empty(row, forward_row=None, backward_row=None):
    new_str = ""
    for i, seat in enumerate(row):
        if seat != ".":
            if i == 0:
                empty_count = check_empty(row, i, forward_row=forward_row, backward_row=backward_row, align="left")
            elif i == len(row) - 1:
                empty_count = check_empty(row, i, forward_row=forward_row, backward_row=backward_row, align="right")
            else:
                empty_count = check_empty(row, i, forward_row=forward_row, backward_row=backward_row)
            if empty_count == 8:
                new_str += "#"
            else:
                new_str += seat
        else:
            new_str += seat
    return new_str

def replace_occupy(row, forward_row=None, backward_row=None):
    new_str = ""
    for i, seat in enumerate(row):
        if seat != ".":
            if i == 0:
                occupy_count = check_occupy(row, i, forward_row=forward_row, backward_row=backward_row, align="left")
            elif i == len(row) - 1:
                occupy_count = check_occupy(row, i, forward_row=forward_row, backward_row=backward_row, align="right")
            else:
                occupy_count = check_occupy(row, i, forward_row=forward_row, backward_row=backward_row)
            if occupy_count >= 4:
                new_str += "L"
            else:
                new_str += seat
        else:
            new_str += seat
    return new_str

def replace_occupy_rows(rows):
    new_rows = rows[:]
    for index, row in enumerate(rows):
        kwargs = {}
        if index - 1 >= 0:
            kwargs["forward_row"] = rows[index - 1]
        if index + 1 < len(rows):
            kwargs["backward_row"] = rows[index + 1]
        new_rows[index] = replace_occupy(row, **kwargs)
    return new_rows

def replace_empty_rows(rows):
    new_rows = rows[:]
    for index, row in enumerate(rows):
        kwargs = {}
        if index - 1 >= 0:
            kwargs["forward_row"] = rows[index - 1]
        if index + 1 < len(rows):
            kwargs["backward_row"] = rows[index + 1]
        new_rows[index] = replace_empty(row, **kwargs)
    return new_rows

def count_occupied(rows):
    cont_count = 0
    while True:
        orig_rows = rows
        if cont_count % 2 == 0:
            rows = replace_empty_rows(rows)
        else:
            rows = replace_occupy_rows(rows)
        if rows == orig_rows:
            break
        cont_count += 1
    occupy_count = 0
    for row in rows:
        for seat in row:
            if check_seat(seat) is True:
                occupy_count += 1
    return occupy_count


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(count_occupied(data))
