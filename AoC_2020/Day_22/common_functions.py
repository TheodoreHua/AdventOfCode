# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def parse_input(data):
    dat = {}
    cur_player = ""
    for line in data:
        if line.startswith("Player "):
            dat[line[:-1]] = []
            cur_player = line[:-1]
        elif line == "":
            continue
        else:
            dat[cur_player].append(int(line))
    return dat
