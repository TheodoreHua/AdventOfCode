# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

"""Very simple script to create the folder stricture for a specific day of AoC -- because I'm lazy"""

if __name__ == "__main__":
    import argparse
    from datetime import date
    from os import mkdir
    from os.path import isdir, isfile

    with open("template.py") as f:
        template = f.read()

    parser = argparse.ArgumentParser(description='Create template AoC folders and files')
    parser.add_argument('day', type=int, choices=range(1, 26), help='which day to create', metavar='DAY')
    parser.add_argument('-y', '--year', type=int, default=date.today().year,
                        help='which year to create (default: current year)', metavar='YEAR')

    args = parser.parse_args()
    if not isdir("AoC_{}".format(args.year)):
        mkdir("AoC_{}".format(args.year))
    if not isdir("AoC_{}/Day_{:02}".format(args.year, args.day)):
        mkdir("AoC_{}/Day_{}".format(args.year, args.day))
    if not isdir("AoC_{}/Day_{:02}/data".format(args.year, args.day)):
        mkdir("AoC_{}/Day_{}/data".format(args.year, args.day))

    if not isfile("AoC_{}/Day_{:02}/part1.py".format(args.year, args.day)):
        with open("AoC_{}/Day_{:02}/part1.py".format(args.year, args.day), "w") as f:
            f.write(template)
    if not isfile("AoC_{}/Day_{:02}/part2.py".format(args.year, args.day)):
        with open("AoC_{}/Day_{:02}/part2.py".format(args.year, args.day), "w") as f:
            f.write(template)
