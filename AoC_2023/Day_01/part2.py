# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

REGEX_START = compile(r"^.*?(\d|one|two|three|four|five|six|seven|eight|nine)")
REGEX_END = compile(r".*(\d|one|two|three|four|five|six|seven|eight|nine).*?$")

number_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def main(d: list, bar):
    total = 0
    for line in d:
        number = ""
        match = REGEX_START.findall(line)[0]
        if match.isdigit():
            number += match
        else:
            number += number_to_digit[match]
        match = REGEX_END.findall(line)[0]
        if match.isdigit():
            number += match
        else:
            number += number_to_digit[match]
        total += int(number)
        bar()

    return total
