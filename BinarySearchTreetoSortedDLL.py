class Solution: ##https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def dfs(node):
            if not node.left and not node.right:
                return node,node

            elif node.left and not node.right:
                l_min_node,l_max_mode = dfs(node.left)
                l_max_mode.right = node
                node.left = l_max_mode
                return l_min_node,node

            elif not node.left and node.right:
                r_min_node,r_max_mode = dfs(node.right)
                r_min_node.left = node
                node.right = r_min_node
                return node,r_max_mode

            else:
                l_min_node,l_max_mode = dfs(node.left)
                r_min_node,r_max_mode = dfs(node.right)
                l_max_mode.right = node
                node.left = l_max_mode
                r_min_node.left = node
                node.right = r_min_node
                return l_min_node,r_max_mode

        min_node,max_node = dfs(root)
        min_node.left = max_node
        max_node.right = min_node

        return min_node