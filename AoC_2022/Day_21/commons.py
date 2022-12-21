# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

NUMBER_REGEX = compile(r"^(.*): (\d+)$")
MATH_REGEX = compile(r"^(.*): (.*) (.*) (.*)$")


class Monkey:
    def __init__(self, name):
        self.name = name
        self.number = None

    def __repr__(self):
        return f"{self.name}: {self.number}"

    def __str__(self):
        return f"{self.name}"


class MathMonkey(Monkey):
    def __init__(self, name, operation, operand_monkey_1, operand_monkey_2):
        super().__init__(name)
        self.operation = operation
        self.operand_monkey_1 = operand_monkey_1
        self.operand_monkey_2 = operand_monkey_2

    def can_perform_operation(self):
        return self.operand_monkey_1.number is not None and self.operand_monkey_2.number is not None

    def perform_operation(self):
        if not self.can_perform_operation():
            raise ValueError("Can't perform operation")
        if self.operation == "+":
            self.number = self.operand_monkey_1.number + self.operand_monkey_2.number
        elif self.operation == "-":
            self.number = self.operand_monkey_1.number - self.operand_monkey_2.number
        elif self.operation == "*":
            self.number = self.operand_monkey_1.number * self.operand_monkey_2.number
        elif self.operation == "/":
            self.number = self.operand_monkey_1.number / self.operand_monkey_2.number
        else:
            raise ValueError("Invalid operation")
        return self.number

    def get_equation(self):
        return f"{self.operand_monkey_1.name} {self.operation} {self.operand_monkey_2.name}"

    def __repr__(self):
        return f"{self.name}: {self.operand_monkey_1} {self.operation} {self.operand_monkey_2} = {self.number}"

    def __str__(self):
        return f"{self.name}"


def parse_input(d: list):
    monkeys = {}
    for line in d:
        if line[-1].isdigit():
            name, number = NUMBER_REGEX.match(line).groups()
            monkey = Monkey(name)
            monkey.number = int(number)
            monkeys[name] = monkey
        else:
            name, operand_monkey_1_name, operation, operand_monkey_2_name = MATH_REGEX.match(line).groups()
            monkey = MathMonkey(name, operation, operand_monkey_1_name, operand_monkey_2_name)
            monkeys[name] = monkey

    for monkey in monkeys.values():
        if isinstance(monkey, MathMonkey) and not isinstance(monkey.operand_monkey_1, Monkey):
            monkey.operand_monkey_1 = monkeys[monkey.operand_monkey_1]
            monkey.operand_monkey_2 = monkeys[monkey.operand_monkey_2]

    return monkeys
