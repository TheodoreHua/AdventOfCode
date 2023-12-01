# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    total = 0
    for line in d:
        number = ""
        for character in line:
            if character.isdigit():
                number += character
                break
        for character in reversed(line):
            if character.isdigit():
                number += character
                break
        total += int(number)
        bar()

    return total
