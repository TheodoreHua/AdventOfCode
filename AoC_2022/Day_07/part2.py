# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .common_funcs import *

def get_all_sizes(directory: dict, totals: list) -> list:
    if directory["parent"] is None:
        totals.append(get_total_size(directory))
    for k, v in directory["dirs"].items():
        totals.append(get_total_size(v))
        totals = get_all_sizes(v, totals)

    return totals

def main(d: list, bar):
    directory = {"dirs": {}, "files": {}, "parent": None}
    cur_directory = directory
    for i in d:
        if i.startswith("$ "):
            i = i[2:]
            if i.startswith("cd"):
                i = i[3:]
                if i == "/":
                    cur_directory = directory
                elif i == "..":
                    cur_directory = cur_directory["parent"]
                elif i in cur_directory["dirs"]:
                    cur_directory = cur_directory["dirs"][i]
                else:
                    cur_directory["dirs"][i] = {"dirs": {}, "files": {}, "parent": cur_directory}
                    cur_directory = cur_directory["dirs"][i]
            continue
        if i.startswith("dir ") and i[4:] not in cur_directory["dirs"]:
            cur_directory["dirs"][i[4:]] = {"dirs": {}, "files": {}, "parent": cur_directory}
        else:
            filesize, filename = i.split(" ")
            cur_directory["files"][filename] = int(filesize)
        bar()


    needed_free = -40000000 + get_total_size(directory)
    return sorted([i for i in get_all_sizes(directory, []) if i >= needed_free])[0]
