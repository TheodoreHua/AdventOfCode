# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2021.Day_04.commons import *


def main(d: list, bar):
    # Obtain draws and boards as properly formatted lists
    draws, boards = parse_input(d, bar)
    # Go through each draw, then each board and return the sum of undrawn values multiplied by the draw when one wins
    for draw in draws:
        for board in boards:
            board.add_draw(draw)
            if board.check_win():
                return board.sum_undrawn() * int(draw)
        bar()  # Increment progress bar
