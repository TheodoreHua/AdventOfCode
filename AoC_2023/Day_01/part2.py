# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

NUM = compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

num_to_dig = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def main(d: list, bar):
    total = 0
    for line in d:
        matches = NUM.findall(line)
        total += int(num_to_dig[matches[0]] + num_to_dig[matches[-1]])
        bar()

    return total


def oneliner(d: list, bar):
    return sum([int(num_to_dig[NUM.findall(line)[0]] + num_to_dig[NUM.findall(line)[-1]]) for line in d])
