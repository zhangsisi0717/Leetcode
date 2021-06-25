#https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = deque([(root,0)])
        result=[]
        while(queue):
            cur_node,layer = queue.popleft()
            if layer>len(result)-1:
                result.append([cur_node.val])
            else:
                result[layer].append(cur_node.val)

            if cur_node.left:
                queue.append((cur_node.left,layer+1))
            if cur_node.right:
                queue.append((cur_node.right,layer+1))

        return result
