#https://leetcode.com/problems/balance-a-binary-search-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    step 1: tranver binary search tree
    step 2: create a new blanced tree
    """
def balanceBST(self, root: TreeNode) -> TreeNode:

    def tranver(node):
        if not node:
            return []

        return tranver(node.left) + [node.val] + tranver(node.right)

    def subBalanTree(listNode):
        if len(listNode) ==1: return TreeNode(val=listNode[0])
        if len(listNode) == 2:
            l,r = TreeNode(val=listNode[0]),TreeNode(val=listNode[1])
            r.left = l
            return r

        mid = int(len(listNode) / 2)
        mid_node = TreeNode(val=listNode[mid])
        mid_node.left = subBalanTree(listNode[0:mid])
        mid_node.right = subBalanTree(listNode[mid+1:])
        return mid_node

    return subBalanTree(tranver(root))







