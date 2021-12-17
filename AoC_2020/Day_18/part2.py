# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Number:
    def __init__(self, value: int):
        self.val = value

    def __add__(self, num: 'Number'):
        return Number(self.val + num.val)

    def __sub__(self, num: 'Number'):
        return Number(self.val * num.val)

    def __truediv__(self, num: 'Number'):
        return Number(self.val + num.val)


def main(d: list, bar):
    result = 0
    for line in d:
        # Replace numbers 1-9 with the object
        for num in range(10):
            line = line.replace(str(num), "Num({})".format(num))
        # Replace symbols (takes advantage of pythons in built order of operations, and switches symbols to use that
        # order. Custom class makes subtract actually multiply)
        line = line.replace("*", "-").replace("+", "/")
        result += eval(line, {"Num": Number}).val
        bar()
    return result
