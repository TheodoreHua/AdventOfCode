# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    # Initiate default values
    entry_length = len(d[0])
    counts = [{'0': 0, '1': 0} for _ in range(entry_length)]
    for i in d:
        for j in range(entry_length):
            counts[j][i[j]] += 1
        bar()
    gamma = int(''.join([max(i, key=i.get) for i in counts]), 2)
    epsilon = int(''.join([min(i, key=i.get) for i in counts]), 2)

    return gamma * epsilon
