# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

"""
Script to prep the directory structure for a specific day of AoC.
"""

if __name__ == "__main__":
    import argparse
    from datetime import date
    from os import makedirs
    from os.path import isdir, isfile

    # Get the template code
    with open("template.py") as f:
        template = f.read()

    # Create the argument parser
    parser = argparse.ArgumentParser(description='Create template AoC folders and files')
    parser.add_argument('day', type=int, choices=range(1, 26), help='which day to create', metavar='DAY')
    parser.add_argument('-y', '--year', type=int, default=date.today().year,
                        help='which year to create (default: current year)', metavar='YEAR')

    # Parse the provided arguments
    args = parser.parse_args()

    # Create all dirs in path if needed
    makedirs("AoC_{}/Day_{:02}/data".format(args.year, args.day), exist_ok=True)
    if not isfile("AoC_{}/Day_{:02}/part1.py".format(args.year, args.day)):  # Create the part 1 file if needed
        with open("AoC_{}/Day_{:02}/part1.py".format(args.year, args.day), "w") as f:
            f.write(template)
    if not isfile("AoC_{}/Day_{:02}/part2.py".format(args.year, args.day)):  # Create the part 2 file if needed
        with open("AoC_{}/Day_{:02}/part2.py".format(args.year, args.day), "w") as f:
            f.write(template)

    # TODO: Automatically retrieve and parse test inputs
    # TODO: Automatically retrieve and store problem description as README.md
