# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution: #https://leetcode.com/problems/validate-binary-search-tree/
    def isValidBST(root: TreeNode) -> bool:

        def subIsValid(root):
            if not root.left and not root.right:
                return True,root.val,root.val #min,max
            elif root.left and root.right:
                lb,lmin,lmax = subIsValid(root.left)
                rb,rmin,rmax = subIsValid(root.right)
                if lb and rb and lmax<root.val and rmin > root.val:
                    return True,lmin,rmax


            elif root.left and not root.right:
                lb,lmin,lmax = subIsValid(root.left)
                if lb and lmax < root.val:
                    return True,lmin,root.val

            elif not root.left and root.right:
                rb,rmin,rmax = subIsValid(root.right)
                if rb and rmin > root.val:
                    return True,root.val,rmax


            return False,math.inf,-math.inf
        return subIsValid(root)[0]
