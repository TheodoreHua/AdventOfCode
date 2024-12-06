# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

F_MAP = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]
F_MAP_LEN = len(F_MAP)


def parse_input(d: list):
    blocked = []
    sr, sc = None, None
    for r, i in enumerate(d):
        row = []
        for c, j in enumerate(i):
            row.append(j == "#")
            if j == "^":
                sr, sc = r, c
        blocked.append(row)
    if sr is None or sc is None:
        raise ValueError("Missing starting position")

    return blocked, sr, sc


def guard_path(blocked, sr, sc, sdi=0, bar=None, include_cdi=False):
    R = len(blocked)
    C = len(blocked[0])
    cr, cc, cdi = sr, sc, sdi

    while True:
        if bar:
            bar()

        if include_cdi:
            yield cr, cc, cdi
        else:
            yield cr, cc

        cd = F_MAP[cdi]
        nr, nc = cr + cd[0], cc + cd[1]
        if not (0 <= nr < R and 0 <= nc < C):
            break

        if blocked[nr][nc]:
            cdi = (cdi + 1) % F_MAP_LEN
            continue
        cr, cc = nr, nc
