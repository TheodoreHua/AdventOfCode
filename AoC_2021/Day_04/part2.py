# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2021.Day_04.commons import *

def main(d:list, bar):
    draws, boards = parse_input(d, bar)
    for draw in draws:
        won = []
        for board in boards:
            board.add_draw(draw)
            if board.check_win():
                if len(boards) == 1:
                    return boards[0].sum_undrawn() * int(draw)
                won.append(board)
        for board in won:
            boards.remove(board)
        bar()
