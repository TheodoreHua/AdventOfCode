# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

DIGIT_REGEX = compile(r"\d+")

def main(d: str, bar):
    t, d = (list(map(int, i)) for i in map(DIGIT_REGEX.findall, d.strip().split("\n")))

    p = 1
    for ind, i in enumerate(t):
        c = 0
        record = d[ind]
        for tp in range(1, i):
            tr = i - tp
            dist = tr * tp
            if dist > record:
                c += 1
        if c > 0:
            p *= c
        bar()

    return p
