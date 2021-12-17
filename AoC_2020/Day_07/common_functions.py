# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import re

BAG_NAME_REGEX = re.compile(r"^([a-zA-Z ]+?) bags")
CONTAIN_BAG_NAME_REGEX = re.compile(r"(\d) ?([a-z ]+)(?: bag[s]?)?")
BAG_REGEX = re.compile(r"(?:[a-zA-Z ]+) bags contain (no other|\d [a-z ]+) bag[s]?((?:, \d [a-z ]+ bag[s]?)*)")


def find_data(bag_string):
    matches = BAG_REGEX.findall(bag_string)[0]
    new_matches = []
    for match in matches:
        if ", " in match:
            for m in match.split(", "):
                if m != "":
                    match_data = CONTAIN_BAG_NAME_REGEX.findall(m)[0]
                    match_data = (int(match_data[0]), match_data[1].replace(" bags", "").replace(" bag", ""))
                    new_matches.append(match_data)
        else:
            if match == "no other":
                return None
            if match != "":
                match_data = CONTAIN_BAG_NAME_REGEX.findall(match)[0]
                match_data = (int(match_data[0]), match_data[1].replace(" bags", "").replace(" bag", ""))
                new_matches.append(match_data)
    return new_matches


def get_bags(bag_string):
    data = find_data(bag_string)
    if data is None:
        return None
    return data


def get_bag_dict(bags):
    bag_dict = {}
    for bag in bags:
        bag_data = get_bags(bag)
        bag_name = BAG_NAME_REGEX.findall(bag)[0]
        bag_dict[bag_name] = bag_data
    return bag_dict
