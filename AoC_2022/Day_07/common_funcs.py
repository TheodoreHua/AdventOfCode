# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def get_total_size(directory: dict):
    total = 0
    for i in directory["files"].values():
        total += i
    for i in directory["dirs"].values():
        total += get_total_size(i)
    return total

def parse_directory(commands: list, bar):
    directory = {"dirs": {}, "files": {}, "parent": None}
    cur_directory = directory
    for i in commands:
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
        elif i.startswith("dir ") and i[4:] not in cur_directory["dirs"]:
            cur_directory["dirs"][i[4:]] = {"dirs": {}, "files": {}, "parent": cur_directory}
        else:
            filesize, filename = i.split(" ")
            cur_directory["files"][filename] = int(filesize)
        bar()

    return directory
