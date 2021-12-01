import math
"""
Build tree only Given pre-order traversal ("None" included)
    1
  /   \
  2    3
       / \
       4  5
#l=[1,2,None,None,3,4,None,None,5,None,None]##

Intuition: l[0] must be root, left subtree must be somewhere between l[1] to the middle_index, right subtree must be l[middle_index+1] to the end
Always build the root => left_subtree => right_subtree

step 1: use recursion, 
if l[0] is None:
    then just return
else=> l[0] must be the root element
  then curRoot = TreeNode(l[0])
  then we pop root element from list, l.pop(0)
  then build the left-subtree,
  finally build the right-subtree
  
"""
class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

l=[1,2,None,None,3,4,None,None,5,None,None]##
def deserialize(l):
    l = deque(l)
    def recursion(l):
        if l[0] == "None":
            l.popleft()
            return None

        curRoot = Node(l[0])
        l.popleft()
        curRoot.left = recursion(l)
        curRoot.right = recursion(l)
        return curRoot

    return recursion(l)

"""
Build tree with Pre-order && Post-

"""

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

            """
            find correct left_subtree range and build left subtree
            """
            left_n = preorder[pre_i + 1]
            left_n_idx_post =  val_to_idx[left_n]
            l_post_i,l_post_j = post_i, left_n_idx_post
            l_pre_i,l_pre_j = pre_i+1, pre_i +1 + (l_post_j-l_post_i)
            root.left = subTree(l_pre_i,l_pre_j,l_post_i,l_post_j)

            """
            find correct right_subtree range and build left subtree
            """
            right_n_idx_post = post_j-1
            r_post_i,r_post_j = l_post_j+1,right_n_idx_post
            r_pre_i,r_pre_j = l_pre_j+1, pre_j
            root.right = subTree(r_pre_i,r_pre_j,r_post_i,r_post_j)

            return root
        return subTree(0,n-1,0,n-1)

