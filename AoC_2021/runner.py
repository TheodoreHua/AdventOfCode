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
    if test_runner is None:
        if not isfile(input_path):
            print("Input file does not exist")
            sys.exit(-1)
        with open(input_path, "r") as f:
            d = [l.strip() for l in f.readlines()]
    else:
        d = test_runner

    start = time()
    with alive_bar(force_tty=True, unknown='stars') as bar:
        r = func(d, bar, *args, **kwargs)
    print("Program successfully finished in {}, return value is '{}'".format(timedelta(seconds=time() - start), r))

    return r


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        try:
            day = int(sys.argv[1])
            part = sys.argv[2]
            test = False
            if part.endswith('-test'):
                part = int(sys.argv[2].rstrip('-test'))
                test = True
            else:
                part = int(part)
            ars = sys.argv[3:] if len(sys.argv) > 3 else []
        except ValueError:
            print("Day and part must be integers")
            sys.exit(-1)
        if not 25 >= day >= 1 or part not in (1, 2):
            print("Invalid day or part value")
            sys.exit(-1)
        directory = "Day_{:02}".format(day)
        module = __import__("{}.part{}".format(directory, part), fromlist=['main'])
        if not test:
            run_aoc(getattr(module, 'main'), "{}/data/input.txt".format(directory, day), test_runner=None, *ars)
        else:
            test_files = [i for i in listdir("{}/data".format(directory)) if i.startswith('test_')]
            if len(test_files) == 0:
                print("No test files found, cancelled")
                sys.exit(-1)
            for fn in test_files:
                print("Initiating test '{}'".format(fn))
                expected = fn.lstrip('test_').rstrip('.txt')
                actual = run_aoc(getattr(module, 'main'), "{}/data/{}".format(directory, fn), test_runner=None, *ars)
                if str(actual) == expected:
                    print("Test '{}' SUCCEEDED with a return result of '{}' and an expected result of {}".format(
                        fn, actual, repr(expected)))
                else:
                    print("Test '{}' FAILED with a return result of '{}' and an expected result of {}".format(
                        fn, actual, repr(expected)))
    else:
        # Basic test if file is run by itself
        from time import sleep
        from random import randint

        run_aoc(example_func, '', test_runner=list(range(1, 1000)), target=randint(1, 1000))
