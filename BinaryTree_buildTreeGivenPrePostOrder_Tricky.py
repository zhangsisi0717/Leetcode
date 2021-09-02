#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""
pre-order:  [root],[left],[right]
post-order:   [left],  [right],[root]

there are multiple possible results for this question

For pre-order list, the first element is always the "root",  we regard the second element pre[1] be "left_node" of root, regard second last element "post[-2]" be the "right_node" of root.
then we
try to find the "left_node_index" of this "left_node" in the post-order, then postorder[start:left_node_index+1] must be the left_subtree, postorder[left_node_index:right_node_index-1] must be the right subtree

after we find the left-subtree and right-subtree given "root", then we recursively reconstruct it

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val_to_idx = {postorder[idx]:idx for idx in range(len(postorder))} ##in pre_order
        n = len(preorder)
        def subTree(pre_i,pre_j,post_i,post_j):
            # print(pre_i,pre_j,post_i,post_j)
            if pre_i > pre_j or post_i>post_j:
                return None
            if pre_i == pre_j or post_i == post_j:
                return TreeNode(val=preorder[pre_i])
            root = TreeNode(preorder[pre_i])
            left_n = preorder[pre_i + 1]
            left_n_idx_post =  val_to_idx[left_n]
            right_n_idx_post = post_j-1


            l_post_i,l_post_j = post_i, left_n_idx_post
            r_post_i,r_post_j = l_post_j+1,right_n_idx_post

            l_pre_i,l_pre_j = pre_i+1, pre_i +1 + (l_post_j-l_post_i)
            r_pre_i,r_pre_j = l_pre_j+1, pre_j

            l_node = subTree(l_pre_i,l_pre_j,l_post_i,l_post_j)
            r_node = subTree(r_pre_i,r_pre_j,r_post_i,r_post_j)

            root.left = l_node
            root.right = r_node
            return root
        return subTree(0,n-1,0,n-1)

