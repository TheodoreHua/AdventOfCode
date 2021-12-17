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


def main(d: list, bar):
    if d[-1] != '':
        d.append('')
    yes_sum = 0
    group = ''
    for l in d:
        if l == '':
            yes_sum += count_yes(group)
            group = ''
        else:
            group += l + ' '
        bar()
    return yes_sum
