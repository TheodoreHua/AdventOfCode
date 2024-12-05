# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *


def main(d: str, bar):
    rules, updates = parse_input(d)

    middle_sum = 0
    for update in updates:
        if not is_incorrect(rules, update):
            middle_sum += update[len(update)//2]
        bar()

    return middle_sum
