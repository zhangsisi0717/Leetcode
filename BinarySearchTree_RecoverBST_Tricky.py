##https://leetcode.com/problems/recover-binary-search-tree/
from typing import *
"""
approach 1: space complexity O(n), time complexity O(n)

if a list [1,2,3,4,5,6] =>swap 2 and 5 => [1,5,3,4,2,6]
                                             ↑ ↑   ↑
                                             x y   y(updated)
x,y, prev = None,None,None
iterate idx from 0 to end,
    if prev is none, then prev=l[idx]
 once we found "prev" > l[idx], x is None and y is None,  ( then it is the first time decrease )， 
 x=l[idx-1], y = l[idx], prev=l[idx], no matter which two numbers are swapped, the x will not change, then we keep updating the prev=l[idx], 
 if we found decrease again  (prev>l[idx]), we update y=l[idx]... eventually x and y are the swapped number
 
 -------------------------------
 Apply the same logic to binary search tree, all we need is nonlocal x,y,prev = None,None,None
 
"""
def recoverTree(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    x,y, prev = None, None, None
    def traversal(node):
        nonlocal x,y,prev
        if not node: ##if node is none, return
            return

        traversal(node.left) ## traverse left subtree and update x,y,prev

        ##line 32-36 is how we actually update the x,y,prev
        if prev and prev.val > node.val: ##if prev is not None and prev_val > node.val
            if not x:
                x = prev
            y = node

        prev = node ##always update prev = node
        traversal(node.right)

    traversal(root)
    x.val, y.val = y.val, x.val
