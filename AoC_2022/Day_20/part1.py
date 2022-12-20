# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import build_linked_list, mix, get_result

def main(d: list, bar):
    nums = list(map(int, d))
    nodes = mix(build_linked_list(nums), bar)
    return get_result(nodes)
