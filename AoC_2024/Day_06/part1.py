# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from .commons import *


def main(d: list, bar):
    blocked, sr, sc = parse_input(d)
    return len(set(guard_path(blocked, sr, sc, bar=bar)))
