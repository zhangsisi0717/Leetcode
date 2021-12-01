import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""
step 1 : run dfs from root to keep track of parents of each node
step 2: start from target node to run BFS to output all the nodes that have a distance "k" from the target node
"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_to_parent = dict()
        def dfs(node, parent):
            if node:
                node_to_parent[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)

        """
        run dfs from root to keep track of parents of each node
        """
        dfs(root,None)


        """
        BFS
        """
        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            # print([[i[0].val,i[1]] for i in queue])
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node_to_parent[node]):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []



