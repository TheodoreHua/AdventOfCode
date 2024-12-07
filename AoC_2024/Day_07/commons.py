# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from itertools import product
from typing import Callable


def parse_input(d: list):
    return {int((c := i.split(': '))[0]): list(map(int, c[1].split(' '))) for i in d}


def is_valid(wanted: int, nums: list[int], operators: list[Callable[[int, int], int]]):
    for op in product(operators, repeat=len(nums)-1):
        acc = op[0](nums[0], nums[1])
        for i, n in enumerate(nums[2:]):
            acc = op[i+1](acc, n)
        if acc == wanted:
            return True
    return False
