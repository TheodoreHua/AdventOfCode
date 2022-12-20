# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

class Node:
    def __init__(self, num, n):
        self.num = num
        self.next = n

    def __repr__(self):
        return str(self.num)

    def __str__(self):
        return str(self.num)

def build_linked_list(nums):
    nodes = [Node(nums[0], None)]
    tail = nodes[-1]
    for n in nums[1:]:
        tail.next = Node(n, None)
        tail = tail.next
        nodes.append(tail)
    return nodes

def mix(nodes, bar, current_node=None):
    if current_node is None:
        current_node = nodes[0]
    while True:
        if current_node is None:
            break
        ind = nodes.index(current_node)
        new_ind = (ind + current_node.num) % (len(nodes) - 1)
        nodes.insert(new_ind, nodes.pop(ind))
        current_node = current_node.next
        bar()

    return nodes

def get_result(nodes):
    ind = [i for i, n in enumerate(nodes) if n.num == 0][0]
    return nodes[(ind + 1000) % (len(nodes))].num + nodes[(ind + 2000) % len(nodes)].num + nodes[(ind + 3000) % len(nodes)].num
