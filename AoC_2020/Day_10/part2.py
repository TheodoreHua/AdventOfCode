# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def count_distinct(adapters):
    adapters.sort()
    adapters = sorted(adapters) + [max(adapters) + 3]
    answers = {0:1}
    for jolt in adapters:
        ans = 0
        for i in range(1,4):
            ans += answers.get(jolt - i, 0)
        answers[jolt] = ans
    return answers[adapters[-1]]


with open("data/input.txt", "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

print(count_distinct(data))
