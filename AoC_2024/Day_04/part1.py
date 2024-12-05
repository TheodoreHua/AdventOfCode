# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

import numpy as np
from typing import Sequence


def total_count(it: Sequence, bar=None):
    if bar:
        bar()
    return it.count("XMAS") + it.count("SAMX")


def main(d: list, bar):
    dm = np.array([list(i) for i in d])

    rows = d
    cols = [''.join(i) for i in dm.transpose()]
    diags = [''.join(dm[::-1, :].diagonal(i)) for i in range(-dm.shape[0]+1, dm.shape[1])]
    diags += [''.join(dm.diagonal(i)) for i in range(dm.shape[1]-1, -dm.shape[0], -1)]

    return sum(total_count(i, bar) for i in rows + cols + diags)
