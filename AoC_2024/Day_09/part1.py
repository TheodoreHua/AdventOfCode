# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------


def main(d: str, bar):
    disk = []
    for i, num in enumerate(map(int, d)):
        if i % 2 == 0:  # files
            for _ in range(num):
                disk.append(i//2)
        else:  # free space
            for _ in range(num):
                disk.append(None)

    for i in reversed(range(len(disk))):
        bar()
        v = disk[i]
        if v is None:
            continue
        ffid = disk.index(None)
        if not ffid:
            break
        if ffid > i:
            break
        disk[ffid] = v
        disk[i] = None

    return sum(i * v for i, v in enumerate(disk) if v is not None)
