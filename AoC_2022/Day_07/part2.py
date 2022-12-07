# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .common_funcs import *

def get_all_sizes(directory: dict, totals=None) -> list:
    if totals is None:
        totals = []
    if directory["parent"] is None:
        totals.append(get_total_size(directory))
    for i in directory["dirs"].values():
        totals.append(get_total_size(i))
        totals = get_all_sizes(i, totals)

    return totals

def main(d: list, bar):
    directory = parse_directory(d, bar)
    needed_free = -40000000 + get_total_size(directory)
    return sorted([i for i in get_all_sizes(directory) if i >= needed_free])[0]
