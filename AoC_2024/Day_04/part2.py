# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

POS = ("MAS", "SAM")


def get_cross(d: list, ri: int, ci: int):
    return d[ri-1][ci-1] + "A" + d[ri+1][ci+1], d[ri-1][ci+1] + "A" + d[ri+1][ci-1]


def main(d: list, bar):
    c = 0
    for ri, row in enumerate(d[1:-1]):
        ri += 1

        for ci, cell in enumerate(row[1:-1]):
            ci += 1

            bar()
            if cell != "A":
                continue

            tl_br, tr_bl = get_cross(d, ri, ci)
            if tl_br in POS and tr_bl in POS:
                c += 1

    return c
