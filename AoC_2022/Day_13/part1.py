# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from json import loads
from .commons import *


def main(d: str, bar):
    packets = []
    for pairs in d.strip().split("\n\n"):
        packets.append([loads(pair) for pair in pairs.split("\n")])

    correct_sum = 0
    for i, packet in enumerate(packets):
        if list_compare(packet[0], packet[1]):
            correct_sum += i + 1
        bar()

    return correct_sum
