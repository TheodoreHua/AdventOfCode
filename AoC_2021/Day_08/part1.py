# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d:list, bar):
    d = [i.split(' | ')[1].split(' ') for i in d]
    easy_count = 0
    for line in d:
        for i in line:
            if len(i) in (2, 4, 3, 7):
                easy_count += 1
        bar()

    return easy_count
