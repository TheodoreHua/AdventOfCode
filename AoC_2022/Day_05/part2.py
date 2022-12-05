# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from collections import defaultdict
from re import compile

STEP_REGEX = compile(r"move (\d+) from (\d+) to (\d+)")


def main(d: str, bar):
    original, steps = d.split("\n\n")
    steps = steps.strip().split("\n")

    parsed = defaultdict(list)
    for i in original.split("\n"):
        for j, k in enumerate(i):
            if k.isalpha():
                parsed[j].append(k)

    full_parsed = [parsed[i] for i in sorted(parsed.keys())]

    for i in steps:
        quantity, from_, to = STEP_REGEX.match(i).groups()
        for j in range(int(quantity)):
            try:
                full_parsed[int(to) - 1].insert(0 + j, full_parsed[int(from_) - 1].pop(0))
            except IndexError:
                pass
        bar()

    return "".join([i[0] for i in full_parsed])
