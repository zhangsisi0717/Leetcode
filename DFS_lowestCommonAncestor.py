#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

"""
explaination: recursive method
use recursion to find all the ancestors of node p [p,a1,a2,a3,a3] including p itself
then use the the save recursion to find all the ancestors of q, and once found that this ancestor of q already exists in ancestor set of p, then return directly
"""
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def allAncestors(node,target,l_set):
        if not node:
            return False,[]
        if node.left == target or node.right == target:
            if node.val in l_set:
                return True,node
            return False,[node]

        l_found,l = allAncestors(node.left,target,l_set)
        r_found,r = allAncestors(node.right,target,l_set)
        if not l and not r:return False,[]
        if l_found:return True,l
        if r_found: return True,r
        if not l_found and not r_found:
            re = l or r
        if node.val not in l_set: return False, re + [node]
        else: return True,node

    p_list = set([p] + allAncestors(root,p,set())[1])
    p_set = {e.val for e in p_list}
    if q.val in p_set: return q
    return allAncestors(root,q,p_set)[1]
