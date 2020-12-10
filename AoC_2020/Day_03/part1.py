# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from common_functions import *

with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(count_trees(duplicate_required(data)))
