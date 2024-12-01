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
    return sum(i * s2.count(i) for i in s1)


def oneliner(d: list, bar):
    return sum((s1 := int(l.split()[0])) * [int(l2.split()[-1]) for l2 in d].count(s1) for l in d)
