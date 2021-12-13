# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2021.Day_04.commons import *


def main(d: list, bar):
    # Obtain draws and boards as properly formatted lists
    draws, boards = parse_input(d, bar)
    for draw in draws:
        won = []
        for board in boards:
            board.add_draw(draw)  # Mark the number as drawn on the board
            if board.check_win():  # Check if the board won
                # If the board is the last board, return the sum of undrawn values on that board multiplied by the draw
                if len(boards) == 1:
                    return boards[0].sum_undrawn() * int(draw)
                # If it's not the last board, add it to the list of boards that won and are to be removed
                won.append(board)
        # Remove all boards that won in that cycle, I spent way too long debugging because I forgot removing while in
        # a for loop with that list ends badly
        for board in won:
            boards.remove(board)
        bar()  # Increment progress bar
