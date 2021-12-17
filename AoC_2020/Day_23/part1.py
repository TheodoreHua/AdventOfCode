def main(d: list, bar):
    cups = list(map(int, d[0]))
    for _ in range(int(1e2)):
        rem = cups[1:4]
        goal = cups[0] - 1 if cups[0] > 1 else 9
        while goal in rem:
            goal -= 1
            if goal == 0:
                goal = 9

        idx = cups.index(goal)
        if idx == 0:
            # no change
            pass
        else:
            cups = list([cups[0]] + cups[4: idx + 1] + rem + cups[idx + 1:])

        cups = cups[1:] + [cups[0]]
        bar()
    return_cups = []
    pointer = cups.index(1) + 1
    while True:
        if cups[pointer] == 1:
            return "".join(return_cups)
        return_cups.append(str(cups[pointer]))
        if pointer == len(cups) - 1:
            pointer = 0
        else:
            pointer += 1
        bar()
