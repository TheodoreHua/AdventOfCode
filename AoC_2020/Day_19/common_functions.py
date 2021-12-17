# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def match(message, nums, rules):
    if not nums:
        return not message
    rule = rules[nums.pop(0)]
    if rule["type"] == "char":
        return message.startswith(rule["val"]) and match(message[len(rule["val"]):], nums, rules)
    else:
        results = []
        for sub in rule["val"]:
            results.append(match(message, sub + nums, rules))
        return any(results)


def count_valid(data):
    results = []
    for message in data["messages"]:
        results.append(match(message, [0], data["rules"]))
    return sum(results)
