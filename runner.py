# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import sys
from datetime import timedelta
from time import time
from typing import Callable
from os import listdir
from os.path import isfile

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

    # Store the start time and start the function with a progress bar
    start = time()
    with alive_bar(force_tty=True, unknown='stars') as bar:
        r = func(d, bar, *args, **kwargs)
    # Print the run time and the return result
    print("Program successfully finished in {}, return value is{}".format(timedelta(
        seconds=time() - start), ":\n{}".format(r) if type(r) is str and '\n' in r else " '{}'".format(r)))

    # Return result from function for tests and other functionality that may need it
    return r


if __name__ == "__main__":
    # Check if the runner was provided enough arguments, if not, run demo function
    if len(sys.argv) >= 4:
        try:
            year = int(sys.argv[1])
            day = int(sys.argv[2])
            part = sys.argv[3]
            test = False
            # If the part number ends with test, run the part function against test data rather than real data
            if part.endswith('-test'):
                part = int(part.rstrip('-test'))
                test = True
            else:
                part = int(part)
            ars = sys.argv[4:] if len(sys.argv) > 4 else []
        except ValueError:
            print("Day and part must be integers")
            sys.exit(-1)
        # Basic checks to make sure day and parts are valid
        if not 25 >= day >= 1 or part not in (1, 2):
            print("Invalid day or part value")
            sys.exit(-1)
        # 2020 was not made around runner, and doesn't support it (yet)
        elif year == 2020:
            print("2020 is not currently available using runner, as runner was made in 2021 and 2020 wasn't updated.")
            sys.exit(-1)
        directory = "AoC_{}/Day_{:02}".format(year, day)
        # Import the main function from the corresponding year, day, part file
        module = __import__("{}.part{}".format(directory.replace('/', '.'), part), fromlist=['main'])
        if not test:
            run_aoc(getattr(module, 'main'), "{}/data/input.txt".format(directory, day), test_runner=None, *ars)
        else:
            # Get a list of all valid test filenames
            test_files = [i for i in listdir("{}/data".format(directory)) if i.startswith('test{}_'.format(part))]
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
                actual = run_aoc(getattr(module, 'main'), "{}/data/{}".format(directory, fn), test_runner=None, *ars)
                print("Test '{}' {}ED with a return result of '{}' and an expected result of {}".format(
                    fn, 'SUCCEED' if str(actual) == expected else 'FAIL', actual, repr(expected)))
    else:
        # Basic test if file is run by itself
        from time import sleep
        from random import randint

        run_aoc(example_func, '', test_runner=list(range(1, 1000)), target=randint(1, 1000))
