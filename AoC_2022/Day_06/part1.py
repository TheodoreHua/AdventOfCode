# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    for i in range(0, len(d[0])):
        if len(set(d[0][i: i + 4])) == 4:
            return i + 4
        bar()


def oneliner(d: list, bar):
    return [i for i in range(0, len(d[0])) if len(set(d[0][i: i + 4])) == 4][0] + 4
