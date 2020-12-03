# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from math import ceil

def duplicate_required(lines, right=3, down=1):
    duplicate_num = ceil(len(lines)/down*right/len(lines[0]))
    new_lines = []
    for line in lines:
        line_str = line
        for i in range(duplicate_num - 1):
            line_str += line
        new_lines.append(line_str)
    return new_lines

def count_trees(lines, right=3, down=1):
    row, column, tree_count = 0, 0, 0
    while row < len(lines):
        if lines[row][column] == "#":
            tree_count += 1
        column += right
        row += down
    return tree_count


with open("../data/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(count_trees(duplicate_required(data)))
