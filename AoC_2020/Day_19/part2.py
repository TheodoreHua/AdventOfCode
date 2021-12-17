# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile
from AoC_2020.Day_19.common_functions import *

CHAR_RULE = compile(r"^(\d*): \"([a-z])\"$")
SUB_RULE = compile(r"^(\d*): ([0-9 ]*)$")
OR_RULE = compile(r"^(\d*): ([0-9 ]*) | ([0-9 ]*)$")


def parse_input(data):
    pointer = 0
    dat = {"rules": {}, "messages": []}
    for i, rule in enumerate(data):
        pointer = i
        if rule == "":
            pointer += 1
            break
        elif '"' in rule:
            r = CHAR_RULE.findall(rule)[0]
            dat["rules"][int(r[0])] = {"type": "char", "val": r[1]}
        elif '|' in rule:
            r = OR_RULE.findall(rule)
            dat["rules"][int(r[0][0])] = {"type": "or", "val": [[int(rn) for rn in r[0][1].split(" ")],
                                                                [int(rn) for rn in r[1][2].split(" ")]]}
        else:
            r = SUB_RULE.findall(rule)[0]
            dat["rules"][int(r[0])] = {"type": "sub", "val": [[int(rn) for rn in r[1].split(" ")]]}
    for message in data[pointer:]:
        dat["messages"].append(message)
    for changed_rule in ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]:
        r = OR_RULE.findall(changed_rule)
        dat["rules"][int(r[0][0])] = {"type": "or", "val": [[int(rn) for rn in r[0][1].split(" ")],
                                                            [int(rn) for rn in r[1][2].split(" ")]]}
    return dat


def main(d: list, bar):
    return count_valid(parse_input(d))
