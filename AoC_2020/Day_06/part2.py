# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import sub


def count_yes(responses):
    group_members = responses.count("\n") + 1
    responses = list(sub(r"[^a-z]]", "", responses))
    all_yes = []
    for response in responses:
        if responses.count(response) == group_members and response not in all_yes:
            all_yes.append(response)
    return len(all_yes)


def main(d: list, bar):
    if d[-1] != '':
        d.append('')
    yes_sum = 0
    group = ''
    for l in d:
        if l == '':
            yes_sum += count_yes(group.strip())
            group = ''
        else:
            group += l + '\n'
        bar()
    return yes_sum
