# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

NUM = compile(r"\d")


def main(d: list, bar):
    total = 0
    for line in d:
        num_chars = NUM.findall(line)
        total += int(num_chars[0] + num_chars[-1])
        bar()

    return total


def oneliner(d: list, bar):
    return sum([int(NUM.findall(line)[0] + NUM.findall(line)[-1]) for line in d])
