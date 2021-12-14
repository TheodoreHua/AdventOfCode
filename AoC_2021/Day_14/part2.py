# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from collections import Counter, defaultdict


def main(d: list, bar):
    polymer = defaultdict(int)
    pairings = {}
    for i in range(len(d[0]) - 1):
        polymer[d[0][i:i + 2]] += 1
    for i in d[2:]:
        s = i.split(' -> ')
        pairings[s[0]] = s[1]

    for _ in range(40):
        new_polymer = defaultdict(int)
        for i in polymer:
            a, b = i
            insert = pairings[''.join(i)]
            occurrences = polymer[i]
            new_polymer[a + insert] += occurrences
            new_polymer[insert + b] += occurrences
        polymer = new_polymer
        bar()

    char_occur = defaultdict(int)
    for i, j in polymer.items():
        char_occur[i[0]] += j

    c = Counter(char_occur).most_common()
    return c[0][1] - c[-1][1] + 1
