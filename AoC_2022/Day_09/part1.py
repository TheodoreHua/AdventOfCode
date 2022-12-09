# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    visited = {(0, 0)}
    for i in d:
        direction, distance = i[0], int(i[2:])
        for _ in range(distance):
            if direction == 'U':
                head_y -= 1
            elif direction == 'D':
                head_y += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'R':
                head_x += 1
            if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
                if head_x > tail_x:
                    tail_x += 1
                elif head_x < tail_x:
                    tail_x -= 1
                if head_y > tail_y:
                    tail_y += 1
                elif head_y < tail_y:
                    tail_y -= 1
            visited.add((tail_x, tail_y))
        bar()

    return len(visited)
