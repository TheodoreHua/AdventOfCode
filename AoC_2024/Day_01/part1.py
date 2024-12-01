# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    s1, s2 = [], []
    for l in d:
        s = l.split()
        s1.append(int(s[0]))
        s2.append(int(s[-1]))
    return sum(abs(i - j) for i, j in zip(sorted(s1), sorted(s2)))


def oneliner(d: list, bar):
    return sum(abs(i - j) for i, j in zip(sorted([int(s.split()[0]) for s in d]), sorted([int(s.split()[-1]) for s in d])))
