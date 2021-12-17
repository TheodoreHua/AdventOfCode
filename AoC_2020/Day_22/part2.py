# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from operator import itemgetter
from AoC_2020.Day_22.common_functions import *


def recursive_combat(data):
    prev_decks = {}
    for player in data.keys():
        prev_decks[player] = []
    while True:
        all_decks = True
        for player, deck in data.items():
            if deck not in prev_decks[player]:
                all_decks = False
                prev_decks[player].append(deck[:])
        if all_decks:
            calc_deck = reversed(data["Player 1"])
            score = 0
            for i, card in enumerate(calc_deck):
                score += card * (i + 1)
            return "Player 1", score
        played_cards = {}
        all_great = True
        for player, deck in data.items():
            played_cards[player] = deck.pop(0)
            if len(deck) < played_cards[player]:
                all_great = False
        if all_great:
            new_data = {}
            for player, deck in data.items():
                new_data[player] = deck[:played_cards[player]]
            winner = recursive_combat(new_data)[0]
        else:
            winner = max(played_cards.items(), key=itemgetter(1))[0]
        data[winner].append(played_cards[winner])
        del played_cards[winner]
        for card in played_cards.values():
            data[winner].append(card)
        cont = True
        for player, deck in data.items():
            if len(deck) == 0:
                cont = False
                break
        if not cont:
            break
    for player, deck in data.items():
        if len(deck) != 0:
            winner = player
            break
    calc_deck = reversed(data[winner])
    score = 0
    for i, card in enumerate(calc_deck):
        score += card * (i + 1)
    return winner, score


def main(d: list, bar):
    return recursive_combat(parse_input(d))[1]
