# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from functools import cmp_to_key
from json import loads

from .commons import *


def compare_wrapper(*args):
    v = list_compare(*args)
    if v is None:
        return 0
    return -1 if v else 1


def main(d: str, bar):
    packets = [[2], [6]]
    for packet in d.strip().replace("\n\n", "\n").split("\n"):
        packets.append(loads(packet))

    sort = sorted(packets, key=cmp_to_key(compare_wrapper))
    return (sort.index([2]) + 1) * (sort.index([6]) + 1)
