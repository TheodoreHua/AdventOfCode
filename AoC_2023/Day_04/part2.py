# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

LINE_REGEX = compile(r"^Card +(\d+): ([\d ]+) \| ([\d ]+)$")
DIGIT_REGEX = compile(r"\d+")

def count_scratchcards(id_, winning, ours, cards):
    scratchcards = 1
    win_count = 0
    for i in ours:
        if i in winning:
            win_count += 1

    for i in range(id_ + 1, id_ + win_count + 1):
        scratchcards += count_scratchcards(i, *cards[i], cards)

    return scratchcards

def main(d: list, bar):
    # TODO: Optimize -- recursive function takes 11s, and it looks like there are inefficiencies
    total = 0
    cards = {}
    for card in d:
        match = LINE_REGEX.fullmatch(card)
        winning = list(map(int, DIGIT_REGEX.findall(match.group(2))))
        ours = list(map(int, DIGIT_REGEX.findall(match.group(3))))
        cards[int(match.group(1))] = (winning, ours)
    for id_, (winning, ours) in cards.items():
        total += count_scratchcards(id_, winning, ours, cards)
        bar()

    return total
