# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from itertools import permutations

def main(d: list, bar):
    d = [[j.split(' ') for j in i.split(' | ')] for i in d]
    output_sum = 0
    m = {'abcdeg': 0, 'ab': 1, 'acdfg': 2, 'abcdf': 3, 'abef': 4, 'bcdef': 5, 'bcdefg': 6, 'abd': 7,
         'abcdefg': 8, 'abcdef': 9}
    all_chars = 'abcdefg'
    for line in d:
        for permutation in permutations(all_chars):
            perm_m = {i:j for i,j in zip(permutation, all_chars)}
            signals = [''.join(perm_m[j] for j in i) for i in line[0]]
            if all(''.join(sorted(i)) in m.keys() for i in signals):
                output_sum += int(''.join(
                    str(m[l]) for l in [''.join(sorted(k)) for k in [''.join(perm_m[j] for j in i) for i in line[1]]]))
                break
        bar()

    return output_sum
