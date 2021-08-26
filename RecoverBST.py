##https://leetcode.com/problems/recover-binary-search-tree/
from typing import *
"""
approach 1: space complexity O(n), time complexity O(n)

step 1 : inorder tranverse the BST, return all the elements into one list
step 2 :  [1,5,3,4,2,6], 2 and 5 were swapped, x,y = None, iterate from i = 0 to len(list)-1,
        if cur[i+1].val < cur[i].val:
            y = cur[i+1]
            if x is None:
                x = cur[i]
            else:
                found x and y, just break
                
step 3: swap x and y
"""
"""
approach 2: space complexity O(1), time complexity O(1)
step 1: recursively read BST as approach 1 , use x,y,prev to find swapped two elements
        def findSwap(node):
            nonlocal x,y,prev
            if not node:
                return 
            
            findSwap(node.left)  ##tranver node.left and update x,y,prev
            if prev and prev.val > node.val:
                y = node
                if not x:
                    x = prev
            prev = node  ##update prev = node
            findSwap(node.right)  ##read node.right
"""
def recoverTree(self, root: Optional[TreeNode]) -> None:
    def inorderTraversal(node):
        if not node:
            return []

        l = inorderTraversal(node.left)
        r = inorderTraversal(node.right)
        return l + [node] + r

    cur = inorderTraversal(root)
    print([i.val for i in cur])
    x,y = None,None
    for i in range(len(cur)-1):
        if cur[i+1].val < cur[i].val:
            y = cur[i+1]
            if not x:
                x = cur[i]
            else:
                break
    y.val,x.val = x.val,y.val
