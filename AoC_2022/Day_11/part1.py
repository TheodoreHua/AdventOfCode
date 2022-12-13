# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *


def main(d: str, bar):
    """F[[20]]"""
    monkeys, _ = parse_input(d)

    for _ in range(20):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                monkey.inspection_count += 1
                monkey.items[i] = monkey.run_operation(monkey.items[i]) // 3
                monkeys[monkey.run_test(monkey.items[i])].items.append(monkey.items[i])
            monkey.items = []
        bar()

    return product(sorted([monkey.inspection_count for monkey in monkeys])[-2:])
