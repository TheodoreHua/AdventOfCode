# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *


def main(d: str, bar):
    rules, updates = parse_input(d)

    incorrect = []
    for update in updates:
        if is_incorrect(rules, update):
            incorrect.append(update)
        bar()

    middle_sum = 0
    for inc in incorrect:
        while swp := is_incorrect(rules, inc):
            i, j = swp
            inc[i], inc[j] = inc[j], inc[i]
        middle_sum += inc[len(inc)//2]
        bar()

    return middle_sum
