# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    # Initiate default values
    counts = [(lambda x=[i[pos] for i in d]: {'0': x.count('0'), '1': x.count('1')})() for pos in range(len(d[0]))]
    gamma = int(''.join([max(i, key=i.get) for i in counts]), 2)
    epsilon = int(''.join([min(i, key=i.get) for i in counts]), 2)

    return gamma * epsilon


def oneliner(d: list, bar):
    return (lambda
                y=[(lambda x=[i[pos] for i in d]: {'0': x.count('0'), '1': x.count('1')})() for pos in
                   range(len(d[0]))]: int(
        ''.join([max(i, key=i.get) for i in y]), 2) * int(''.join([min(i, key=i.get) for i in y]), 2))()
