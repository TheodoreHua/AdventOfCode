# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    adapters = list(map(int, d))
    adapters.sort()
    adapters = sorted(adapters) + [max(adapters) + 3]
    answers = {0: 1}
    for jolt in adapters:
        ans = 0
        for i in range(1, 4):
            ans += answers.get(jolt - i, 0)
        answers[jolt] = ans
        bar()
    return answers[adapters[-1]]
