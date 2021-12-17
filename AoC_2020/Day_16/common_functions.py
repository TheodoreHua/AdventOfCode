# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

FIELD_REGEX = compile(r"^([a-zA-Z ]*): (\d*?)-(\d*?) or (\d*?)-(\d*?)$")


def parse_input(data):
    new_data = {"fields": {}, "my_ticket": [], "tickets": []}
    pointer = 0
    for i, line in enumerate(data):
        if line == '':
            break
        field_data = FIELD_REGEX.findall(line.replace("\n", ""))[0]
        new_data["fields"][field_data[0]] = [(int(field_data[1]), int(field_data[2])),
                                             (int(field_data[3]), int(field_data[4]))]
        pointer = i
    pointer += 3
    new_data["my_ticket"] = [int(l) for l in data[pointer].replace("\n", "").split(",")]
    pointer += 3
    for line in data[pointer:]:
        # noinspection PyTypeChecker
        new_data["tickets"].append([int(l) for l in line.replace("\n", "").split(",")])
    return new_data


def check_valid(value, fields):
    valid_fields = []
    for name, sa in fields.items():
        for s in sa:
            if s[0] <= value <= s[1]:
                valid_fields.append(name)
                break
    if len(valid_fields) > 0:
        return valid_fields
    return False
