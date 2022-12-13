# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .common_funcs import *


def get_sum_above_100000(directory: dict, total: int = 0):
    for i in directory["dirs"].values():
        size = get_total_size(i)
        if size <= 100000:
            total += size
        total = get_sum_above_100000(i, total)

    return total


def main(d: list, bar):
    return get_sum_above_100000(parse_directory(d, bar))
