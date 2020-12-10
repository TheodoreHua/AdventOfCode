# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def check_valid(adapter, jolts):
    if adapter - 3 <= jolts <= adapter:
        return adapter - jolts
    return None

def multiply_1_3_adapter(adapters):
    adapters = sorted(adapters) + [max(adapters) + 3]
    one_count = 0
    three_count = 0
    last_jolt = 0
    for adapter in adapters:
        val = check_valid(adapter, last_jolt)
        if val == 1:
            one_count += 1
        elif val == 3:
            three_count += 1
        else:
            break
        last_jolt = adapter
    return one_count * three_count


with open("data/input.txt", "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

print(multiply_1_3_adapter(data))
