# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    converted_list = [int(i) for i in d]
    index = 0
    mapped = []
    past = float('inf')
    while index <= len(d):
        s = sum(converted_list[index:index+3])
        mapped.append(s > past)
        past = s
        index += 1
        bar()

    return sum(mapped)
