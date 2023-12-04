# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

LINE_REGEX = compile(r"^Card +\d+: ([\d ]+) \| ([\d ]+)$")
DIGIT_REGEX = compile(r"\d+")

def main(d: list, bar):
    matches = [
        len(
            set(DIGIT_REGEX.findall(
                (match := LINE_REGEX.fullmatch(card))
                .group(1)
            ))
            & set(DIGIT_REGEX.findall(match.group(2)))
        )
        for card in d
    ]
    cards = [1] * len(d)
    for i, mc in enumerate(matches):
        for j in range(mc):
            cards[i+j+1] += cards[i]
        bar()

    return sum(cards)
