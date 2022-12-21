# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from sympy import Symbol, solve, sympify

from .commons import parse_input, MathMonkey


def main(d: list, bar):
    monkeys = parse_input(d)

    monkeys["root"].operation = '='
    monkeys["humn"].number = None  # Just so I don't accidentally use it

    last_solve_count = -1
    solve_count = 0
    while last_solve_count != solve_count:
        last_solve_count = solve_count
        solve_count = 0
        for monkey in monkeys.values():
            if monkey.name == "root":
                continue
            elif monkey.name == "humn":
                continue
            if isinstance(monkey, MathMonkey):
                if monkey.can_perform_operation():
                    monkey.perform_operation()
                    solve_count += 1

    equation = monkeys["root"].get_equation()
    replace_count = None
    while replace_count != 0:
        replace_count = 0
        for monkey in monkeys.values():
            if monkey.name == "root":
                continue
            elif monkey.name == "humn":
                continue
            if monkey.number is not None:
                old_equation = equation
                equation = equation.replace(monkey.name, str(monkey.number))
            else:
                old_equation = equation
                equation = equation.replace(monkey.name, f"({monkey.get_equation()})")
            if old_equation != equation:
                replace_count += 1
        bar()

    equation_l, equation_r = equation.split(" = ")
    equation = sympify(equation_l) - sympify(equation_r)
    return str(round(solve(equation, Symbol("humn"))[0]))
