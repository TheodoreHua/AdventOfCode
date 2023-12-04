# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile
from math import floor

LINE_REGEX = compile(r"^Card +\d+: ([\d ]+) \| ([\d ]+)$")  # TODO: Optimize regex (should not need 2)
DIGIT_REGEX = compile(r"\d+")

def main(d: list, bar):
    total = 0
    for card in d:
        match = LINE_REGEX.fullmatch(card)
        winning = set(DIGIT_REGEX.findall(match.group(1)))
        ours = set(DIGIT_REGEX.findall(match.group(2)))
        total += floor(2**(len(winning & ours) - 1))
        bar()

    return total

def oneliner(d: list, bar):
    return sum([floor(2**(len(set(DIGIT_REGEX.findall((match := LINE_REGEX.fullmatch(card)).group(1))) & set(DIGIT_REGEX.findall(match.group(2)))) - 1)) for card in d])
