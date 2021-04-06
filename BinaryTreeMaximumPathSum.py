# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Start from root, and recursively check root.left and root.right, keep track of local_Max, global_Max
local_max is the cur_max collecting to current node, global_Max is the max sum belowing the current node
for root, global_Max = max(l+root.val, r+root.val, l+r+root.val,root.val,l_gMax,r_gMax)
l-root-r, global_max = max(l-root,root, root-r, l_gMax,r_gMax)

"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int: ##https://leetcode.com/problems/binary-tree-maximum-path-sum/
        import numpy as np

        def maxSumFromRoot(root):
            if not root.left and not root.right:
                return root.val, root.val##max(left, right), global_max

            elif not root.left and root.right:
                r,gMax = maxSumFromRoot(root.right)
                gMax = max(r + root.val,root.val,gMax)
                return max(r + root.val,root.val),gMax

            elif root.left and not root.right:
                l,gMax =maxSumFromRoot(root.left)
                gMax = max(l + root.val,root.val,gMax)
                return max(l + root.val,root.val),gMax

            else:
                l,l_gMax = maxSumFromRoot(root.left)
                r,r_gMax = maxSumFromRoot(root.right)
                gMax = max(l+root.val, r+root.val, l+r+root.val,root.val,l_gMax,r_gMax)
                return max(l+root.val,r+root.val,root.val),gMax

        return maxSumFromRoot(root)[1]