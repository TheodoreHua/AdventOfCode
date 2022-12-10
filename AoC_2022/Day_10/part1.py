# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    x_vals = {}
    x = 1
    cycle = 1
    for i in d:
        if i == "noop":
            cycle += 1
        else:
            cycle += 2
            x += int(i.lstrip("addx "))
        x_vals[cycle] = x
        bar()

    s = 0
    for i in range(20, 240, 40):
        if i in x_vals:
            s += x_vals[i] * i
        else:
            for j in range(i, 0, -1):
                if j in x_vals:
                    s += x_vals[j] * i
                    break
    return s
