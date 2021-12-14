# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from collections import Counter


def main(d: list, bar):
    polymer = list(d[0])
    pairings = {}
    for i in d[2:]:
        s = i.split(' -> ')
        pairings[s[0]] = s[1]

    for _ in range(10):
        new_list = []
        for i in range(len(polymer)):
            j = ''.join(polymer[i:i + 2])
            if len(j) == 1:
                new_list.append(j[0])
                break
            try:
                new_list.append(j[0] + pairings[j])
            except KeyError:
                print("Error in sequence, {} not in pairings".format(j))
        polymer = []
        for i in new_list:
            polymer += list(i)
        bar()

    c = Counter(polymer).most_common()
    return c[0][1] - c[-1][1]
