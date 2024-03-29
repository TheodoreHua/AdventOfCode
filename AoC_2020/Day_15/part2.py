# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    starting = list(map(int, d[0].split(',')))
    nums = {}
    turn_number = 1
    last_num = None
    for num in starting:
        nums[num] = [turn_number]
        turn_number += 1
        last_num = num
    while turn_number <= 30000000:
        bar.text("TN: {:,}".format(turn_number))
        if len(nums[last_num]) <= 1:
            if 0 not in nums.keys():
                nums[0] = [turn_number]
            else:
                nums[0] = [nums[0][-1], turn_number]
            last_num = 0
        else:
            sub_num = nums[last_num][-1] - nums[last_num][-2]
            if sub_num not in nums.keys():
                nums[sub_num] = [turn_number]
            else:
                nums[sub_num] = [nums[sub_num][-1], turn_number]
            last_num = sub_num
        turn_number += 1
        bar()
    return last_num
