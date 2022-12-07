# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def get_total_size(directory: dict):
    total = 0
    for i in directory["files"].values():
        total += i
    for i in directory["dirs"].values():
        total += get_total_size(i)
    return total
