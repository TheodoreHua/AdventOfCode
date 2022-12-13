# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from numpy import product


class Monkey:
    def __init__(self, starting_items, operation, test, test_result):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.test_result = test_result
        self.inspection_count = 0

    def run_operation(self, old):
        return eval(self.operation.replace("old", str(old)))

    def run_test(self, item):
        return self.test_result[self.test(item)]


def parse_input(d: str):
    monkeys = []
    lcm = []
    for monkey in d.split("\n\n"):
        lines = monkey.split("\n")
        starting_items = list(map(int, lines[1][17:].split(", ")))
        operation = lines[2][19:]
        mod = int(lines[3][21:])
        test = lambda x, v=mod: x % v == 0
        lcm.append(mod)
        test_result = (int(lines[5][-1]), int(lines[4][-1]))
        monkeys.append(Monkey(starting_items, operation, test, test_result))
    return monkeys, product(lcm)
