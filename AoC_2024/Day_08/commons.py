# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from collections import defaultdict
from itertools import combinations
from typing import Any, Iterable


def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0]-b[0]) + abs(a[1] - b[1])


def point_on_line(p: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[1]*(b[0]-p[0]) + b[1]*(p[0]-a[0]) + p[1]*(a[0]-b[0]) == 0


def parse_input(d: list) -> defaultdict[Any, list[tuple[int, int]]]:
    antennas = defaultdict(list)
    for r, l in enumerate(d):
        for c, v in enumerate(l):
            if v == '.':
                continue
            antennas[v].append((r, c))
    return antennas


def grid_traverse(R, C) -> Iterable[tuple[int, int]]:
    for r in range(R):
        for c in range(C):
            yield r, c


def antenna_pairs(antennas: dict[Any, list[tuple[int, int]]]) -> Iterable[tuple[Any, tuple[int, int], tuple[int, int]]]:
    for frequency, locations in antennas.items():
        for antenna1, antenna2 in combinations(locations, 2):
            yield frequency, antenna1, antenna2
