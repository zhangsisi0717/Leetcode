##https://leetcode.com/problems/copy-list-with-random-pointer/submissions/
"""
use original node reference as key, new copyed node as value
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
        return head
    node_dict = dict()
    cur_node = head
    # idx=0
    while(cur_node):
        node_dict[cur_node] = Node(cur_node.val,None,None)
        cur_node = cur_node.next

    # print(len(node_list))

    cur_node = head
    while(cur_node):
        if cur_node.next:
            node_dict[cur_node].next = node_dict[cur_node.next]
        if cur_node.random:
            node_dict[cur_node].random = node_dict[cur_node.random]
        cur_node = cur_node.next

    return node_dict[head]
