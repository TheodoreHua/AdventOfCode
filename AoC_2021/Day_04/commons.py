# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import re

class Board:
    def __init__(self, board:list):
        self.board = [{j:False for j in i} for i in board]

    def check_win(self):
        columns = [[] for _ in range(5)]
        for row in self.board:
            # Check horizontal win
            if all(row.values()):
                return True
            # Add values to column list
            for i, v in enumerate(row.values()):
                columns[i].append(v)
        # Check vertical win
        for column in columns:
            if all(column):
                return True
        return False

    def add_draw(self, draw):
        for row in self.board:
            if draw in row.keys():
                row[draw] = True

    def sum_undrawn(self):
        s = 0
        for row in self.board:
            for num, val in row.items():
                if not val:
                    s += int(num)
        return s


def parse_input(d, bar):
    """Parse the input file to needed data formats

    :param d: Input list
    :param bar: alive-progress bar func
    :return: List of draws and list of boards (list of rows)
    """
    row_regex = re.compile(r"^(\d*)\s*(\d*)\s*(\d*)\s*(\d*)\s*(\d*)\s*$")
    draws = d[0].split(',')
    raw_boards = []
    board = []
    for row in d[2:]:
        if row == '':
            raw_boards.append(board)
            board = []
        else:
            board.append(row_regex.findall(row)[0])
        bar()

    boards = []
    for board in raw_boards + [board]:
        boards.append(Board(board))
        bar()

    return draws, boards
