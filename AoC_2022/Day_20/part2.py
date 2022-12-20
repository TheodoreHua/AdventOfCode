# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import build_linked_list, mix, get_result

def main(d: list, bar):
    nums = [811589153 * i for i in map(int, d)]
    nodes = build_linked_list(nums)
    begin = nodes[0]
    for _ in range(10):
        mix(nodes, bar, begin)

    return get_result(nodes)
