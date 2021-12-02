# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    horizontal = 0
    depth = 0
    for i in d:
        if i.startswith('forward '):
            horizontal += int(i.lstrip('forward '))
        elif i.startswith('up '):
            depth -= int(i.lstrip('up '))
        elif i.startswith('down '):
            depth += int(i.lstrip('down '))
        else:
            print("Invalid value detected: " + i)
        bar()

    return horizontal * depth
