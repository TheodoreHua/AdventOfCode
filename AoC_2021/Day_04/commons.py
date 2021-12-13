# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import re


class Board:
    def __init__(self, board: list):
        # Convert data into list of boards (list of rows [list of nums with dict to represent marking])
        self.board = [{j: False for j in i} for i in board]

    def check_win(self):
        """Check if this board has won"""
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
        """Mark off a draw on the board"""
        for row in self.board:
            if draw in row.keys():
                row[draw] = True

    def sum_undrawn(self):
        """Get the sum of all undrawn values"""
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
    row_regex = re.compile(r"^(\d*)\s*(\d*)\s*(\d*)\s*(\d*)\s*(\d*)\s*$")  # Compile regex for obtaining row values
    draws = d[0].split(',')  # Get list of draws (list of draws are all on the first line, comma-delimited)
    # Initiate default values
    raw_boards = []
    board = []
    for row in d[2:]:
        if row == '':  # If row is empty, that means that that board is done, and to prepare for the next one
            raw_boards.append(board)
            board = []
        else:
            board.append(row_regex.findall(row)[0])  # Process row and add it to temporary board list
        bar()  # Increment progress bar

    # Convert the list of raw boards into a list of Board objects
    boards = []
    for board in raw_boards + [board]:
        boards.append(Board(board))
        bar()

    return draws, boards
