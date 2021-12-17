# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    d = list(map(int, d))
    compare_list = d[:]
    for i in d:
        for j in compare_list:
            if i + j == 2020:
                return i * j
            bar()
