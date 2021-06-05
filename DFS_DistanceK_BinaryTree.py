#All Nodes Distance K in Binary Tree
#https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
a=1
"""
purpose: find all the nodes that have a distance K from the target node
approach: 
1.run dfs to find all the ancestors of target node in order, including target. ancestors_list = [target, target.parent, target.parent.parent..., root]
2. for idx in range(len(ancestors_list)), run dfs to find all the nodes that has a distance K-idx from ancestors_list[idx]
    (we need to use a set to keep track of all the visited node!!!!!!!, do not add visited node!!

"""
def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    result=[]
    visited=set()
    def dfs(node,dis):
        if not node or dis<0:return []
        if node.val in visited: return []
        if dis==0:
            return [node.val]
        l = dfs(node.left,dis-1)
        r = dfs(node.right,dis-1)
        visited.add(node.val)
        return l+r
    def findParents(node):
        if not node: return []
        if node == target:
            return [target]
        l = findParents(node.left)
        r = findParents(node.right)
        if not l and not r:return []
        parents = l or r
        return parents + [node]
    parents = findParents(root)
    for idx in range(len(parents)):
        result += dfs(parents[idx],k-idx)
    return result