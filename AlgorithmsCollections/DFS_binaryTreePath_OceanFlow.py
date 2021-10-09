import typing
"""
common question 1: dfs + binary_Tree: find all path from a->b or find all path starting from "a" and path_sum == target
##https://leetcode.com/problems/path-sum-ii/
"""
def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    def dfs(node,target):
        if not node:
            return []
        path = []
        if node.val == target and not node.left and not node.right:
            path.append([target])

        l = dfs(node.left,target-node.val)
        r = dfs(node.right,target-node.val)

        for p in l+r:
            path.append([node.val]+p)

        return path

    return dfs(root,targetSum)

"""
triky question 2: sometimes, we need to decide the dfs direction
https://leetcode.com/problems/pacific-atlantic-water-flow/
in the water-flow question, starting dfs from Ocean would be much easier.
"""
#https://leetcode.com/problems/pacific-atlantic-water-flow/
def pacificAtlantic(heights):
    n_row, n_col = len(heights), len(heights[0])
    _to_paci = [[True if r == 0 or c == 0 else False for c in range(n_col)] for r in range(n_row)]
    _to_alta = [[True if r == n_row - 1 or c == n_col - 1 else False for c in range(n_col)] for r in range(n_row)]
    _called_paci = [[False for c in range(n_col)] for r in range(n_row)]
    _called_alta = [[False for c in range(n_col)] for r in range(n_row)]

    def label(r, c, to, called):
        called[r][c] = True
        to[r][c] = True
        for i, j in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= i < n_row and 0 <= j < n_col:
                if heights[i][j] >= heights[r][c] and not called[i][j]:
                    label(i, j, to, called)
    """
    Two dfs to Separetely label if a block can flow to pacific and atlantic ocean, DFS starting from block that can definitely flow to pacific/atlantic, and if the height of its neigbors are
    larger than this block, then label it as "True" and label it as "called"
    """
    for r in range(n_row):
        for c in range(n_col):
            if _to_paci[r][c] and not _called_paci[r][c]:
                label(r, c, _to_paci, _called_paci)
            if _to_alta[r][c] and not _called_alta[r][c]:
                label(r, c, _to_alta, _called_alta)

    return [(r, c) for r in range(n_row) for c in range(n_col) if _to_paci[r][c] and _to_alta[r][c]]


