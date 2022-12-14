# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np
from advent_of_code_ocr import convert_array_6


def cycle(crt, current_draw, row, x):
    if current_draw in range(x - 1, x + 2):
        crt[row, current_draw] = True
    current_draw += 1
    if current_draw == 40:
        current_draw = 0
        row += 1
    return crt, current_draw, row


def main(d: list, bar):
    crt = np.zeros((6, 40), dtype=bool)
    row, current_draw = 0, 0
    x = 1
    for i in d:
        crt, current_draw, row = cycle(crt, current_draw, row, x)
        if i.startswith("addx"):
            crt, current_draw, row = cycle(crt, current_draw, row, x)
            x += int(i.lstrip("addx "))
        bar()

    print("\n".join(["".join(['◼️' if j else '◻️' for j in i]) for i in crt]))
    try:
        return convert_array_6(crt, fill_pixel=True, empty_pixel=False)
    except KeyError:
        return None
