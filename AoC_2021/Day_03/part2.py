# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    # Initiate default values
    entry_length = len(d[0])
    trimmed_oxygen, trimmed_co2 = d[:], d[:]
    oxygen, co2 = None, None
    for i in range(entry_length):
        oc, cc = (lambda x=[c[i] for c in trimmed_oxygen]: {'0': x.count('0'), '1': x.count('1')})(), \
                 (lambda x=[c[i] for c in trimmed_co2]: {'0': x.count('0'), '1': x.count('1')})()
        m, s = max(oc, key=oc.get) if oc['0'] != oc['1'] else '1', min(cc, key=cc.get) if cc['0'] != cc['1'] else '0'
        new_trimmed_oxygen, new_trimmed_co2 = [], []

        for j in trimmed_oxygen:
            if m == j[i]:
                new_trimmed_oxygen.append(j)
        for j in trimmed_co2:
            if s == j[i]:
                new_trimmed_co2.append(j)

        if len(new_trimmed_oxygen) == 1:
            oxygen = new_trimmed_oxygen[0]
            trimmed_oxygen = []
        else:
            trimmed_oxygen = new_trimmed_oxygen[:]
        if len(new_trimmed_co2) == 1:
            co2 = new_trimmed_co2[0]
            trimmed_co2 = []
        else:
            trimmed_co2 = new_trimmed_co2[:]

        if oxygen is not None and co2 is not None:
            break
        bar()
    return int(oxygen, 2) * int(co2, 2)
