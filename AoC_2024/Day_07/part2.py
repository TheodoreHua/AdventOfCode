# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *

OPERATORS = [
    lambda a, b: a + b,
    lambda a, b: a * b,
    lambda a, b: int(str(a) + str(b))
]


def main(d: list, bar):
    calibrations = parse_input(d)
    total = 0
    for wanted, nums in calibrations.items():
        if is_valid(wanted, nums, OPERATORS):
            total += wanted
        bar()

    return total
