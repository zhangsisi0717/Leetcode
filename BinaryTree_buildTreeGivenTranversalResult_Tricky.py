from typing import List
"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
given tranversal result of preoder and inorder lists, rebuild this binary tree

pre-order:  [root],[left],[right]
in-order:   [left], [root], [right]

therefore, for pre-order list, the first element is always the "root", then we found the index of the "root" in in-order,
and then we could find the left-subtree and right-subtree given "root", then we recursively reconstruct it

i:prefix, j:surfix
reconstruct(pre_i,pre_j,in_i,in_j)  will return the root of this reconstructed tree given (preorder_i,preorder_j) and
(inorder_i,inorder_j)
    if preorder list or inorder list is empty: then return None
    else:
        pre-order[preorder_i] must be root of this subtree
        then we find the idx of this root in in-order (by using a dictionary O(1)), and 
        reconstruct 1. left-subtree of in-order and right-subtree of in-order
                    2. left-subtree in pre-order and right-subtree in pre-order
                    
       left_node_of_root = reconstruct(l_pre_i,l_pre_j,;l_in_i,l_in_j)
       right_node_of_root = reconstruct(r_pre_i,r_pre_j,;r_in_i,r_in_j)  
       
       root.left =  left_node_of_root 
       root.right = right_node_of_root
                    
Time Complexity O(m)  m is number of nodes     

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    #preorder -> root,left,right
    #inorder -> left, root, right
    int_to_idx = {inorder[idx]:idx for idx in range(len(inorder))}

    def reconstruct(pre_i,pre_j,in_i,in_j):
        if pre_i>pre_j or in_i>in_j:
            return None
        root = TreeNode(val=preorder[pre_i])
        idx = int_to_idx[preorder[pre_i]]
        l_inorder_i,l_inorer_j = in_i,idx-1
        r_inorder_i,r_inorer_j = idx+1,in_j

        l_pre_i,l_pre_j = pre_i+1,pre_i+idx-in_i
        r_pre_i,r_pre_j = pre_i+idx-in_i+1,pre_j

        l_subtree_root = reconstruct(l_pre_i,l_pre_j,l_inorder_i,l_inorer_j)
        r_subtree_root = reconstruct(r_pre_i,r_pre_j,r_inorder_i,r_inorer_j)

        root.left = l_subtree_root
        root.right = r_subtree_root
        return root

    return reconstruct(0,len(preorder)-1,0,len(preorder)-1)