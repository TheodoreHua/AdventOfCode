# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

SEED_REGEX = compile(r"^seeds: ((?:\d+ *)+)$")
TITLE_REGEX = compile(r"^(.*)-to-(.*) map:$")
LINE_REGEX = compile(r"^(\d+) (\d+) (\d+)$")
DIGIT_REGEX = compile(r"\d+")

class Map:
    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target
        self.maps = {}

    def add_map(self, destination_start: int, source_start: int, length: int):
        source = range(source_start, source_start + length + 1)
        self.maps[source] = destination_start - source_start

    def get_result(self, num: int):
        for r, adj in self.maps.items():
            if num in r:
                return num + adj
        return num

def get_last(num: int, maps, source: str = "seed"):
    if source not in maps:
        return num
    else:
        return get_last(maps[source].get_result(num), maps, maps[source].target)

def main(d: list, bar):
    seeds = map(int, DIGIT_REGEX.findall(SEED_REGEX.fullmatch(d[0]).group(1)))
    maps = {}
    last_map = None
    for line in d:
        if match := TITLE_REGEX.fullmatch(line):
            source = match.group(1)
            target = match.group(2)
            maps[source] = Map(source, target)
            last_map = source
        elif match := LINE_REGEX.fullmatch(line):
            dest, src, length = map(int, match.groups())
            maps[last_map].add_map(dest, src, length)
        bar()

    results = [get_last(seed, maps) for seed in seeds]
    return min(results)
