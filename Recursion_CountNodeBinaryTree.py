##https://leetcode.com/problems/count-good-nodes-in-binary-tree/
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def recursion(node,max_val):
            if not node:
                return 0

            add = 0
            if max_val <= node.val:
                add = 1
                max_val = node.val

            re = recursion(node.left,max_val) + recursion(node.right,max_val)
            return re+add

        return recursion(root,root.val)

