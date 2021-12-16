# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import sys
from datetime import date
from typing import Callable
from os import listdir
from os.path import isfile

from about_time import about_time
from alive_progress import alive_bar


def example_func(d, bar, target):
    """Basic mimic function to test AoC runner"""
    for i, j in enumerate(d):
        if j == target:
            return i
        sleep(0.01)
        bar()
    return "No result found"


def run_aoc(func: Callable, input_path: str, test_runner: list = None, *args, **kwargs):
    """Default puzzle function runner code for AoC

    :param func: Function to run that takes arguments d (data) and bar (progress bar), expected to return final value
    :param input_path: Path to the input file to run from
    :param test_runner: Whether the function is being run as a test
    """
    # Load file data, if it's a test, user demo data provided through the argument
    if test_runner is None:
        if not isfile(input_path):
            print("Input file does not exist")
            sys.exit(-1)
        with open(input_path, "r") as f:
            d = [l.strip() for l in f.readlines()]
    else:
        d = test_runner

    # Track runtime and start the function with a progress bar
    with about_time() as at:
        with alive_bar(force_tty=True, unknown='stars') as bar:
            r = func(d, bar, *args, **kwargs)
    # Print the run time and the return result
    print("Program successfully finished in {}, return value is{}".format(
        at.duration_human, ":\n{}".format(r) if type(r) is str and '\n' in r else " '{}'".format(r)))

    # Return result from function for tests and other functionality that may need it
    return r


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run AoC code in a human-friendly way')
    parser.add_argument('-y', '--year', type=int, default=date.today().year,
                        help='Specify the year to run, default is this year')
    parser.add_argument('day', type=int, choices=range(1, 26), help='Which day to run', metavar='DAY')
    parser.add_argument('part', type=int, choices=[1, 2], help='Which part to run', metavar='PART')
    parser.add_argument('-t', '--test', action='store_true', help='If the program should be run using test values')
    parser.add_argument('-a', '--args', nargs='+', default=[], help='Additional arguments to provide to the program')

    parse = parser.parse_args()
    print(parse)

    # 2020 was not made around runner, and doesn't support it (yet)
    if parse.year == 2020:
        print("2020 is not currently available using runner, as runner was made in 2021 and 2020 wasn't updated.")
        sys.exit(-1)
    directory = "AoC_{}/Day_{:02}".format(parse.year, parse.day)
    # Import the main function from the corresponding year, day, part file
    module = __import__("{}.part{}".format(directory.replace('/', '.'), parse.part), fromlist=['main'])
    if not parse.test:
        run_aoc(getattr(module, 'main'), "{}/data/input.txt".format(directory, parse.day), test_runner=None,
                *parse.args)
    else:
        # Get a list of all valid test filenames
        test_files = [i for i in listdir("{}/data".format(directory)) if i.startswith('test{}_'.format(parse.part))]
        if len(test_files) == 0:
            print("No test files found, cancelled")
            sys.exit(-1)
        # Iterate through every test and run the corresponding part against it
        for fn in test_files:
            print("Initiating test '{}'".format(fn))
            # Slice out the test_ and .txt parts of the filename to get the expected values, as well as - which can
            # be appended to the end of a filename in order to allow for tests with the same result (which would
            # originally result in the same filename)
            expected = fn[6:-4].rstrip('-')
            actual = run_aoc(getattr(module, 'main'), "{}/data/{}".format(directory, fn), test_runner=None,
                             *parse.args)
            print("Test '{}' {}ED with a return result of '{}' and an expected result of {}".format(
                fn, 'SUCCEED' if str(actual) == expected else 'FAIL', actual, repr(expected)))
