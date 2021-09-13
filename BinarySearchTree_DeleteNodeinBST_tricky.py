##https://leetcode.com/problems/delete-node-in-a-bst/solution/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
use recursion to recursively delete the node

if root == None: return None
if key > root.val,
    then we need to delete node from right-subtree
    root.right = self.deleteNode(root.right, key)
if key < root.val,
    then we need to delete node from left-subtree
    root.left = self.deleteNode(root.left, key)

if key == root.val, then we found the node that need to be deleted:
    if root is a leaf: then root = None
    if root has right child, then we set root.val = successor(root), and call
        root.right = deleteNode(root.right, root.val)

    elif root only has left child, then root.val = predecessor(root), and call
        root.left = deleteNode(root.left, root.val)

"""
class Solution:
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.left and not root.right:
                root = None

            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root









