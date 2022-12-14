# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2021.Day_13.commons import parse_input
from advent_of_code_ocr import convert_6


def main(d: list, bar):
    grid, folds = parse_input(d)
    for fold in folds:
        grid.fold(*fold)
        bar()

    grid_str = str(grid)
    print(grid_str)
    return convert_6(grid_str)
