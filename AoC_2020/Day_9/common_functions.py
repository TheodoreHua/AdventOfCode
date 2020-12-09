# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def adds_together(sequence, target):
    for i in sequence:
        for j in sequence:
            if i + j == target and i != j:
                return True
    return False
