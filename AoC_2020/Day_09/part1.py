# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2020.Day_09.common_functions import *


def main(d: list, bar):
    d = list(map(int, d))
    preamble_length = 25
    pointer = preamble_length
    while pointer < len(d) - 1:
        preamble = d[pointer - preamble_length:pointer]
        if not adds_together(preamble, d[pointer]):
            return d[pointer]
        pointer += 1
        bar()
    return None
