# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import sub

def count_yes(responses):
    responses = sub(r"[^a-z]", "", responses)
    yes_responses = []
    for response in responses:
        if response not in yes_responses:
            yes_responses.append(response)
    return len(yes_responses)

def get_yes_sum(group_responses):
    yes_sum = 0
    for group in group_responses:
        yes_sum += count_yes(group)
    return yes_sum


with open("data/input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")

print(get_yes_sum(data))
