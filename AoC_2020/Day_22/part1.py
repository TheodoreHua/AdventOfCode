# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from operator import itemgetter
from common_functions import *

def get_win_score(data):
    while True:
        played_cards = {}
        for player, deck in data.items():
            played_cards[player] = deck.pop(0)
        win_player = max(played_cards.items(), key=itemgetter(1))[0]
        data[win_player].append(played_cards[win_player])
        del played_cards[win_player]
        for card in played_cards.values():
            data[win_player].append(card)
        cont = True
        for player, deck in data.items():
            if len(deck) == 0:
                cont = False
                break
        if not cont:
            break
    for player, deck in data.items():
        if len(deck) != 0:
            win_player = player
            break
    calc_deck = reversed(data[win_player])
    score = 0
    for i, card in enumerate(calc_deck):
        score += card * (i + 1)
    return score


print(get_win_score(parse_input("data/input.txt")))
