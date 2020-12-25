class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def part2(s):
    N = int(1e6)
    nodes = {}
    for c in range(1, N + 1):
        nodes[c] = Node(c)

    for x, y in zip(s, s[1:]):
        x, y = map(int, [x, y])
        nodes[x].next = nodes[y]

    if len(s) == N:
        nodes[int(s[-1])].next = nodes[int(s[0])]
    else:
        nodes[int(s[-1])].next = nodes[len(s) + 1]
        for i in range(len(s) + 1, N):
            nodes[i].next = nodes[i + 1]
        nodes[N].next = nodes[int(s[0])]

    head = nodes[int(s[0])]
    for _ in range(int(1e7)):
        print(_)
        rem_start = head.next
        rem_end = head.next.next.next

        vals = [rem_start.val, rem_start.next.val, rem_end.val]
        goal = head.val - 1 if head.val > 1 else N
        while goal in vals:
            goal -= 1
            if goal == 0:
                goal = N

        head.next = rem_end.next
        rem_end.next = nodes[goal].next
        nodes[goal].next = rem_start

        head = head.next

    a, b = nodes[1].next.val, nodes[1].next.next.val
    return a, b, a * b


with open("data/input.txt", "r") as f:
    print(part2(f.read()))
