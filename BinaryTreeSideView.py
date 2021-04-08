class Solution: #https://leetcode.com/problems/binary-tree-right-side-view/submissions/
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def dfs(node):
            if not node.left and not node.right:
                return [node.val]

            elif not node.left and node.right:
                return [node.val] + dfs(node.right)

            elif node.left and not node.right:
                return [node.val] + dfs(node.left)

            else:
                l = dfs(node.left)
                r = dfs(node.right)
                if(len(r)>=len(l)):
                    return [node.val] + r
                else:
                    return [node.val] + r + l[len(r):]

        return dfs(root)