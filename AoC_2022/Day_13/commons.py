# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------


def list_compare(left: list, right: list):
    compare_index = 0
    while True:
        if compare_index == len(left) == len(right):
            return None
        elif compare_index == len(left):
            return True
        elif compare_index == len(right):
            return False
        cleft, cright = left[compare_index], right[compare_index]
        if isinstance(cleft, int) and isinstance(cright, int):
            if cleft < cright:
                return True
            elif cleft > cright:
                return False
        elif isinstance(cleft, list) or isinstance(cright, list):
            v = list_compare(cleft if isinstance(cleft, list) else [cleft],
                             cright if isinstance(cright, list) else [cright])
            if v is not None:
                return v
        compare_index += 1
