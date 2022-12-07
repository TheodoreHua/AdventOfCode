# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .common_funcs import *

def get_sum_above_100000(directory: dict, total: int=0):
    for i in directory["dirs"].values():
        size = get_total_size(i)
        if size <= 100000:
            total += size
        total = get_sum_above_100000(i, total)

    return total

def main(d: list, bar):
    directory = {"dirs": {}, "files": {}, "parent": None}
    cur_directory = directory
    for i in d:
        if i.startswith("$ "):
            i = i.lstrip("$ ")
            if i.startswith("cd"):
                i = i.lstrip("cd ")
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
        if i.startswith("dir "):
            cur_directory["dirs"][i.lstrip("dir ")] = {"dirs": {}, "files": {}, "parent": cur_directory}
        else:
            filesize, filename = i.split(" ")
            cur_directory["files"][filename] = int(filesize)
        bar()

    return get_sum_above_100000(directory)
