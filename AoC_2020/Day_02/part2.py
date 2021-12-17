# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import re


def main(d: list, bar):
    valid_count = 0
    for line in d:
        data_tup = re.findall(r"(\d*)-(\d*) (\w): (\w*)", line)[0]
        n_pos, f_pos, letter = int(data_tup[0]), int(data_tup[1]), data_tup[2]
        password = data_tup[3]
        if (password[n_pos - 1] == letter) != (password[f_pos - 1] == letter):
            valid_count += 1
        bar()
    return valid_count
