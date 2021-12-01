# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    # Convert values in data to int and initiate default values
    converted_list = [int(i) for i in d]
    index = 0
    mapped = []
    past = float('inf')
    while index <= len(d):
        # Get the sum of the current index and the next 2
        s = sum(converted_list[index:index+3])
        # Check whether the current sum is larger than the past one
        mapped.append(s > past)
        # Update loop vars
        past = s
        index += 1
        # Increment alive-progress
        bar()

    return sum(mapped)
