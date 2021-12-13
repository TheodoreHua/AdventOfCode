# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import re
from numpy import array_split

data_regex = re.compile(r"(\d*),(\d*) -> (\d*),(\d*)")


def parse_input(d):
    return [array_split([int(j) for j in data_regex.findall(i)[0]], 2) for i in d]
