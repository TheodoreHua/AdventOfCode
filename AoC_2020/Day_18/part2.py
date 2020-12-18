# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Number:
    def __init__(self, value):
        self.val = value

    def __add__(self, num):
        return Number(self.val + num.val)

    def __sub__(self, num):
        return Number(self.val * num.val)

    def __truediv__(self, num):
        return Number(self.val + num.val)

def solve(data):
    result = 0
    for line in data:
        # Replace numbers 1-9 with the object
        for num in range(10):
            line = line.replace(str(num), "Num({})".format(num))
        # Replace symbols (takes advantage of pythons in built order of operations, and switches symbols to use that
        # order. Custom class makes subtract actually multiply)
        line = line.replace("*", "-").replace("+", "/")
        result += eval(line, {"Num": Number}).val
    return result


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(solve(data))
