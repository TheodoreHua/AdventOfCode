# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

char_map = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

def main(d: list, bar):
    decimal_sum = 0
    bar.text("Converting to decimal...")
    for line in d:
        cur = 0
        for char in line:
            cur = cur * 5 + char_map[char]
        decimal_sum += cur
        bar()

    bar.text("Converting back to SNAFU...")
    answer = ''
    while decimal_sum > 0:
        m = decimal_sum % 5
        if m == 0: answer = "0" + answer
        elif m == 1: answer = "1" + answer
        elif m == 2: answer = "2" + answer
        elif m == 3:
            answer = "=" + answer
            decimal_sum += 2
        elif m == 4:
            answer = "-" + answer
            decimal_sum += 1
        decimal_sum //= 5

    return answer
