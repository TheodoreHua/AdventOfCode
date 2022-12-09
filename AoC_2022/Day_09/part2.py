# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

def main(d: list, bar):
    head_x, head_y = 0, 0
    tails = [[0, 0] for _ in range(9)]
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
            prev_tail = (head_x, head_y)
            for tail in tails:
                if abs(prev_tail[0] - tail[0]) > 1 or abs(prev_tail[1] - tail[1]) > 1:
                    if prev_tail[0] > tail[0]:
                        tail[0] += 1
                    elif prev_tail[0] < tail[0]:
                        tail[0] -= 1
                    if prev_tail[1] > tail[1]:
                        tail[1] += 1
                    elif prev_tail[1] < tail[1]:
                        tail[1] -= 1
                prev_tail = tuple(tail)
            visited.add(prev_tail)
        bar()

    return len(visited)
