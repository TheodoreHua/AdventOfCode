# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import sys
from datetime import timedelta
from time import time
from typing import Callable

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
    :param test_runner: Whether or not the function is being run as a test
    """
    start = time()

    if test_runner is None:
        with open(input_path, "r") as f:
            d = [l.strip() for l in f.readlines()]
    else:
        d = test_runner

    with alive_bar(force_tty=True, unknown='stars') as bar:
        r = func(d, bar, *args, **kwargs)
    print("Program successfully finished in {}, return value is '{}'".format(timedelta(seconds=time() - start), r))


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        try:
            day = int(sys.argv[1])
            part = int(sys.argv[2])
            ars = sys.argv[3:] if len(sys.argv) > 3 else []
        except ValueError:
            print("Day and part must be integers")
            sys.exit(-1)
        if not 25 >= day >= 1 or part not in (1, 2):
            print("Invalid day or part value")
            sys.exit(-1)
        directory = "Day_{:02}".format(day)
        module = __import__("{}.part{}".format(directory, part), fromlist=['main'])
        run_aoc(getattr(module, 'main'), "{}/data/input.txt".format(directory, day), test_runner=None, *ars)
    else:
        # Basic test if file is run by itself
        from time import sleep
        from random import randint

        run_aoc(example_func, '', test_runner=[i for i in range(1, 1000)], target=randint(1, 1000))
