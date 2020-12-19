# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

CHAR_RULE = compile(r"^(\d): \"([a-z])\"$")
SUB_RULE = compile(r"^(\d): ([0-9 ]*)$")
OR_RULE = compile(r"^(\d): ([0-9 ]*) | ([0-9 ]*)$")

def parse_input(filename):
    with open(filename, "r") as f:
        data = [l.strip() for l in f.readlines()]
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
    return dat

def match(message, stack, rules):
    if len(stack) > len(message):
        return False
    elif len(stack) == 0 or len(message) == 0:
        return len(stack) == 0 and len(message) == 0

    c = stack.pop()
    if isinstance(c, str):
        if message[0] == c:
            return match(message[1:], stack.copy(), rules)
    else:
        for rule in rules[c]:
            if match(message, stack + list(reversed(rule)), rules):
                return True
    return False

def r_messages(data):
    count = 0
    for message in data["messages"]:
        if match(message, list(reversed(data["rules"][0]["val"][0])), data["rules"]):
            count += 1
    return count


print(r_messages(parse_input("data/test_input.txt")))
