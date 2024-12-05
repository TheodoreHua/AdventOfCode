# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from collections import defaultdict


def parse_input(d: str):
    rules_raw, updates = d.split("\n\n")
    rules = defaultdict(lambda: [])
    for i in rules_raw.split():
        req_prev, page = map(int, i.split("|"))
        rules[page].append(req_prev)  # y: x -- given page to page numbers that must be before it
    updates = [list(map(int, i.split(','))) for i in updates.split()]

    return rules, updates


def is_incorrect(rules, update):
    for page_i, page in enumerate(update):
        for req_prev in rules[page]:
            if req_prev not in update:
                continue
            req_prev_i = update.index(req_prev)
            if req_prev_i > page_i:
                return page_i, req_prev_i
    return False
