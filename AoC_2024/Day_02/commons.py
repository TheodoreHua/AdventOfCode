# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def is_safe(report: list):
    return report in (sorted(report), sorted(report, reverse=True)) and all(1 <= abs(report[i+1] - report[i]) <= 3 for i in range(len(report)-1))
