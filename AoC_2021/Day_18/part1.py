# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import json


def add_pairs(p1, p2) -> list:
    return [p1] + [p2]


def count_nested(l, n:int=1) -> int:
    for i in l:
        if isinstance(i, list):
            n += 1
            n = count_nested(i, n)
            break
    return n


def reduce_pair(pair) -> list:
    r = True
    while True:
        r = False
        for p in pair:
            print(count_nested(p))
            # try:
            #     p[0][0][0][0]
            # except (KeyError, TypeError):
            #     pass
            # else:
            #     r = True
            #     nep = p[0][0][0]
            #     ap = p[0][0]
            #     print('Found nested pair: ', repr(nep), repr(pair))
            #     print('New pair:')
    return pair


def main(d: list, bar):
    d = [json.loads(i) for i in d]
    p1 = d[0]
    p2 = d[1]
    pointer = 2

