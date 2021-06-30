##https://leetcode.com/problems/binary-tree-vertical-order-traversal/
from collections import defaultdict
from collections import deque
"""
vertically tranverse the binary tree,  from top to bottom, column by column,If two nodes are in the same row and column, the order should be from left to right.

approach: 
 step 1: create columnTable to update the column number of current node
dictionary columnTable: key: col, val: list of nodes at that column

step 2: use BFS to update the column infomation of all the nodes (queue data structure)

step 3: sort key value and return the results
"""
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in sorted(columnTable.keys())]
