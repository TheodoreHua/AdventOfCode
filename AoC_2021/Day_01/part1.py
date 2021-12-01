# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    # Initiate default values, past is inf to make sure the first comparison is False
    past = float('inf')
    mapped = []
    # Loop through each value and compare with the previous, add bool value to mapped list
    for i in d:
        i = int(i)
        mapped.append(i > past)
        past = i
        bar()
    # Return number of Trues in bool list (True is 1, False is 0 for sum)
    return sum(mapped)
