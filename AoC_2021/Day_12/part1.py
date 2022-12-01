# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from collections import defaultdict


def main(d: list, bar):
    neighbours = defaultdict(list)
    for i in d:
        a, b = i.split("-")
        neighbours[a].append(b)
        neighbours[b].append(a)

    def count(visited=None, cave='start'):
        bar()
        if visited is None:
            visited = []
        if cave == 'end':
            return 1
        if cave in visited:
            if cave == 'start' or cave.islower():
                return 0

        return sum(count(visited + [cave], n) for n in neighbours[cave])

    return count()
