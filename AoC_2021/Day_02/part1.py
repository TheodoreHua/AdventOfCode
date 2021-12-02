# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    # Initiate default values
    horizontal = 0
    depth = 0
    for i in d:
        if i.startswith('forward '):
            horizontal += int(i.lstrip('forward '))  # Increase horizontal value by X if command is forward
        elif i.startswith('up '):
            depth -= int(i.lstrip('up '))  # Decrease depth by X if command is up
        elif i.startswith('down '):
            depth += int(i.lstrip('down '))  # Increase depth by X if command is down
        else:
            print("Invalid value detected: " + i)  # Print an error message if there's an issue in data then skip it
        bar()

    return horizontal * depth  # Return multiplied value
