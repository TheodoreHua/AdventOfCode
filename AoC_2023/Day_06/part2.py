# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

DIGIT_REGEX = compile(r"\d+")

def main(d: str, bar):
    t, record = map(DIGIT_REGEX.findall, d.strip().split("\n"))
    t = int("".join(t))
    record = int("".join(record))

    c = 0
    for tp in range(1, t):
        tr = t - tp
        dist = tr * tp
        if dist > record:
            c += 1
        bar()

    return c
