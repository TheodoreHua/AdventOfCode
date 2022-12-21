# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import parse_input, MathMonkey


def main(d: list, bar):
    monkeys = parse_input(d)

    root = monkeys["root"]
    while root.number is None:
        for monkey in monkeys.values():
            if isinstance(monkey, MathMonkey) and monkey.can_perform_operation():
                monkey.perform_operation()
            bar()

    assert root.number is not None
    return int(root.number)
