# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

DIGIT_REGEX = compile(r"-?\d+")  # THERE WERE NEGATIVES

def extrapolate(l):
    diffs = []
    for i in range(1, len(l)):
        diffs.append(l[i] - l[i-1])
    if any(diffs):  # not all 0s yet
        backwards = extrapolate(diffs)
        backwards.append(diffs[-1] + backwards[-1])
        return backwards
    else:
        return [0]

def extrapolate_wrapper(l):
    return l[-1] + extrapolate(l)[-1]

def main(d: list, bar):
    history = [list(map(int, DIGIT_REGEX.findall(i))) for i in d]
    return sum(list(map(extrapolate_wrapper, history)))
