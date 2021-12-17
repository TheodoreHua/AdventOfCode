# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from AoC_2020.Day_03.common_functions import *
from math import prod


def main(d: list, bar):
    sets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    set_results = []
    for s in sets:
        set_results.append(count_trees(duplicate_required(d, right=s[0], down=s[1]), right=s[0], down=s[1]))
        bar()
    return prod(set_results)
