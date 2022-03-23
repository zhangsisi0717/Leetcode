#https://leetcode.com/problems/copy-list-with-random-pointer/
import math
"""
deepcopy directed graph with cycles
"""
node_to_copied_node= dict()
def dfs_copy(node):
    if not node:
        return None
    if node in node_to_copied_node:
        return node_to_copied_node[node]


    new_node = Node(node.val)
    node_to_copied_node[node] = new_node
    new_node.next = dfs_copy(node.next)
    new_node.random = dfs_copy(node.random)

    return new_node
    return dfs_copy(head)
