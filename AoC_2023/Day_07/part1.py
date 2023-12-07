# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from collections import Counter

STRENGTH = "AKQJT98765432"

class Hand:
    def __init__(self, hand, bid):
        self.hand = list(hand)
        self.bid = int(bid)
        self.score = get_score_value(self.hand)

    def __repr__(self):
        return f"{''.join(self.hand)} (BID: {self.bid}, SCORE: {self.score})"

def get_hand_score(hand):
    return [STRENGTH.index(i) for i in hand]

def get_score_value(hand):
    occur = Counter(hand)
    occur_len = len(occur)
    if occur_len == 1:  # 5k
        ts = [0]
    elif occur_len == 2:  # 4k or fh
        vals = list(occur.values())
        if vals[0] == 4 or vals[0] == 1:  # 4k
            ts = [1]
        else:  # fh
            ts = [2]
    elif occur_len == 3:  # 3k or 2p
        if list(occur.values()).count(2) == 2:  # 2p
            ts = [4]
        else:  # 3k
            ts = [3]
    elif occur_len == 4:  # 1p
        ts = [5]
    elif occur_len == 5:
        ts = [6]
    else:
        raise Exception(f"Unexpected state while handling hand | {''.join(hand)} | Uniques: {occur_len}")

    return ts + get_hand_score(hand)

def main(d: list, bar):
    hands = sorted([Hand(*i.split(" ")) for i in d], key=lambda x: x.score, reverse=True)
    total = 0
    for i, hand in enumerate(hands, start=1):
        total += hand.bid * i
    return total
