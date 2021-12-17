# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

# ******************************************************************************************
# CREDIT TO /u/metaquarx (https://github.com/metaquarx/) for helping with debugging
# ******************************************************************************************

from AoC_2020.Day_07.common_functions import *


def count_contain(bag_name, bag_dict):
    if bag_dict[bag_name] is None:
        return 1
    count = 1
    for num, contain in bag_dict[bag_name]:
        count += count_contain(contain, bag_dict) * num
    return count


def main(d: list, bar):
    bag_dict = get_bag_dict(d)
    bag_name = 'shiny gold'
    if bag_dict[bag_name] is None:
        return 1
    count = 1
    for num, contain in bag_dict[bag_name]:
        count += count_contain(contain, bag_dict) * num
        bar()
    return count - 1
