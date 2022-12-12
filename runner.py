# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import sys
from datetime import date
from re import compile
from typing import Callable, Union, get_type_hints
from os import listdir
from os.path import isfile

from about_time import about_time
from alive_progress import alive_bar
from aocd import get_data, submit

FINITE_REGEX = compile(r"F\[\[(\d+)]]")

def run_aoc(func: Callable, input_path: str, finite: Union[int, bool] = False, *args, **kwargs):
    """Default puzzle function runner code for AoC

    :param func: Function to run that takes arguments d (data) and bar (progress bar), expected to return final value
    :param input_path: Path to the input file to run from
    :param finite: Whether the progress bar should have a finite value or not, True for input lines, or int to specify.
    """
    # Load file data
    if not isfile(input_path):
        print("Input file does not exist")
        sys.exit(-1)
    expected_type = get_type_hints(func)["d"]
    with open(input_path, "r") as f:
        if expected_type is list:
            d = [l.strip() for l in f.readlines()]
        elif expected_type is str:
            d = f.read()

    # Track runtime and start the function with a progress bar
    finite_doc = FINITE_REGEX.search(func.__doc__)
    if type(finite) is int:
        b = alive_bar(finite, force_tty=True)
    elif finite is True:
        b = alive_bar(len(d), force_tty=True)
    elif finite_doc:
        b = alive_bar(int(finite_doc.group(1)), force_tty=True)
    else:
        b = alive_bar(force_tty=True, unknown='stars')
    with b as bar:
        with about_time() as at:
            r = func(d, bar, *args, **kwargs)
    # Print the run time and the return result
    print("Program successfully finished in {}, return value is{}".format(
        at.duration_human, ":\n{}".format(r) if type(r) is str and '\n' in r else " '{}'".format(r)))

    # Return result from function for tests and other functionality that may need it
    return r


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run AoC code in a human-friendly way')
    parser.add_argument('day', type=int, choices=range(1, 26), nargs='?', help='which day to run', metavar='DAY')
    parser.add_argument('part', type=int, choices=[1, 2], nargs='?', help='which part to run', metavar='PART')
    parser.add_argument('-y', '--year', type=int, default=date.today().year,
                        help='specify the year to run, default is the current year')
    parser.add_argument('-t', '--test', action='store_true', help='if the program should be run using test values')
    parser.add_argument('-s', '--submit', action='store_true', help='automatically submit the result to AoC')
    parser.add_argument('-o', '--oneliner', action='store_true',
                        help='Run the program using one liner code (if available)')
    parser.add_argument('-f', '--finite', type=int, const=True, default=False, nargs='?',
                        help="specify a finite number of iterations for the progress bar, if flag is used but argument "
                             "is left empty, number of lines in input file is used")
    parser.add_argument('-a', '--args', nargs='+', default=[], help='additional arguments to provide to the program')

    parse = parser.parse_args()

    directory = "AoC_{}/Day_{:02}".format(parse.year, parse.day)
    if parse.day is not None and 1 <= parse.part <= 2:
        # Import the main function from the corresponding year, day, part file
        module = __import__("{}.part{}".format(directory.replace('/', '.'), parse.part), fromlist=['main'])
        if not parse.test:
            # If input data does not exist, get it
            if not isfile("{}/data/input.txt".format(directory)):
                print("Input file does not exist, getting input data from AoC")
                data = get_data(day=parse.day, year=parse.year)
                with open("{}/data/input.txt".format(directory), "w") as f:
                    f.write(data)
            result = run_aoc(getattr(module, "oneliner" if parse.oneliner else "main"),
                             "{}/data/input.txt".format(directory, parse.day), parse.finite, *parse.args)
            if parse.submit:
                submit(result, day=parse.day, year=parse.year, part="a" if parse.part == 1 else "b", reopen=False)
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
                actual = run_aoc(getattr(module, 'oneliner' if parse.oneliner else 'main'),
                                 "{}/data/{}".format(directory, fn), finite=parse.finite, *parse.args)
                print("Test '{}' {}ED with a return result of '{}' and an expected result of {}".format(
                    fn, 'SUCCEED' if str(actual) == expected else 'FAIL', actual, repr(expected)))
