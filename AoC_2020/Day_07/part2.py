# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

# ******************************************************************************************
# BIG FAT CREDIT TO /u/metaquarx (https://github.com/metaquarx/) for helping with debugging
# ******************************************************************************************

from common_functions import *

def count_contain(bag_name, bag_dict):
    if bag_dict[bag_name] is None:
        return 1
    count = 1
    for num, contain in bag_dict[bag_name]:
        count += count_contain(contain, bag_dict) * num
    return count


with open("data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(count_contain("shiny gold", get_bag_dict(data)) - 1)
