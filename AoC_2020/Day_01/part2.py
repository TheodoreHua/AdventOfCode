# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def sum_check(target:int, values:list):
    compare_list = values[:]
    compare_list_2 = values[:]
    for i in values:
        for j in compare_list:
            for k in compare_list_2:
                if i + j + k == target:
                    print("{0} + {1} + {2} = {3}\n{0} * {1} * {2} = {4}".format(i, j, k, i + j + k, i * j * k))
                    return


with open("data/input.txt", "r") as f:
    report = f.readlines()
    try:
        report = [int(r.strip()) for r in report]
    except ValueError:
        print("Invalid Value in Report")
        exit(1)

sum_check(2020, report)
