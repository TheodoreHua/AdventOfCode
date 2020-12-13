# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

# ******************************************************************************************
# CREDIT TO /u/metaquarx (https://github.com/metaquarx/) for helping with debugging
# ******************************************************************************************

from common_functions import *

def check_contain(target, bag_name, bag_dict):
    if bag_dict[bag_name] is None:
        return False
    for num, contain in bag_dict[bag_name]:
        if target == contain:
            return True
        elif check_contain(target, contain, bag_dict):
            return True
    return False

def count_contain(target, bags):
    target_contain = 0
    bag_dict = get_bag_dict(bags)
    for contain_bag in bag_dict.keys():
        if check_contain(target, contain_bag, bag_dict):
            target_contain += 1
    return target_contain


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(count_contain("shiny gold", data))
