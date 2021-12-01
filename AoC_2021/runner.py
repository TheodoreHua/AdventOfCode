# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

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

def run_aoc(func:Callable, test_runner:list=None, **kwargs):
    """Default puzzle function runner code for AoC

    :param func: Function to run that takes arguments d (data) and bar (progress bar), expected to return final value
    :param test_runner: Whether or not the function is being run as a test
    """
    start = time()

    if test_runner is None:
        with open("data/input.txt", "r") as f:
            d = f.readlines()
    else:
        d = test_runner

    with alive_bar(force_tty=True, unknown='stars') as bar:
        r = func(d, bar, **kwargs)
    print("Program successfully finished in {}, return value is '{}'".format(timedelta(seconds=time() - start), r))


if __name__ == "__main__":
    # Basic test if file is run by itself
    from time import sleep
    from random import randint

    run_aoc(example_func, test_runner=[i for i in range(1,1000)], target=randint(1,1000))
