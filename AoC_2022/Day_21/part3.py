# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

"""Solution for Upping the Ante from Reddit - https://www.reddit.com/r/adventofcode/comments/zrdfb0/"""

from numpy import prod
from sympy import Symbol, solve, sympify


def main(d: list, bar):
    bar.text("Parsing input")
    monkeys = parse_input(d)

    monkeys["root"].operation = '='
    monkeys["humn"].number = None  # Just so I don't accidentally use it

    bar.text("Solving non-humn equations")
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
            bar()

    bar.text("Generating equation")
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

    bar.text("Solving equation")
    equation_l, equation_r = equation.split(" = ")
    equation = sympify(equation_l) - sympify(equation_r)
    return str(prod(solve(equation, Symbol("humn"))))


if __name__ == "__main__":
    from commons import parse_input, MathMonkey
    from alive_progress import alive_bar

    inp = list(map(str.strip, """
        root: pppw + drzm
        dbpl: 41
        cczh: sllz + lgvd
        zczc: dvpt - qlgz
        ptdq: humn * humn
        dvpt: lfqf * zstt
        lfqf: 3
        humn: 5
        ljgn: 360
        sjmn: ptdq * dbpl
        sllz: ptdq * ptdq
        pppw: cczh * lfqf
        lgvd: ljgn + wvql
        drzm: hmdt - zczc
        hmdt: 0
        qlgz: bzbn * rjtn
        zstt: rjtn * ptdq
        rjtn: hwpf * humn
        hwpf: 2
        bzbn: 63
        wvql: hmdt - sjmn
    """.strip().splitlines()))

    with alive_bar(unknown="stars") as bar:
        print(main(inp, bar))
