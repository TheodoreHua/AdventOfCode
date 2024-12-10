# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Space:
    def __init__(self, size: int):
        self.size = size

class FreeSpace(Space):
    def __init__(self, size: int):
        super().__init__(size)

    def __str__(self):
        return '.' * self.size

class Block(Space):
    def __init__(self, size: int, value: int):
        super().__init__(size)
        self.value = value

    def __str__(self):
        return str(self.value) * self.size

    def get_hash_val(self, starting_pos):
        v = 0
        for i in range(starting_pos, starting_pos + self.size):
            v += i * self.value
        return v

def find_free_space(disk: list[Space], required: int):
    for i, space in enumerate(disk):
        if isinstance(space, FreeSpace):
            if space.size >= required:
                return i
    return None


def main(d: str, bar):
    disk = []
    files = []
    for i, num in enumerate(map(int, d)):
        if i % 2 == 0:  # files
            disk.append(Block(num, i//2))
            files.append(disk[-1])
        else:
            disk.append(FreeSpace(num))

    for file in sorted(files, key=lambda x: x.value, reverse=True):
        bar()
        fi = disk.index(file)
        fsi = find_free_space(disk, file.size)
        if fsi is None:
            continue
        if fsi >= fi:
            continue
        fs = disk[fsi]
        diff = fs.size - file.size
        disk[fsi] = file
        disk[fi] = FreeSpace(file.size)
        if diff > 0:
            disk.insert(fsi+1, FreeSpace(diff))

    pos = 0
    checksum = 0
    for space in disk:
        if isinstance(space, Block):
            checksum += space.get_hash_val(pos)
        pos += space.size

    return checksum
