##https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
"""
Prefix_Sum!!!! O(N)
explaination: pretty similar to "count subarrays sum to k", in a 1-d array [x1,x2,x3,x4,x5], count cumulative sum, if SumToX2 + k == SumToX4, then X3 + X4 == k,
so if we cumulate to SumToX5, then count += [SumToX5-k]

Apply it to binary tree, we use pre-order traversal, root->left->right,
each time we use hashmap to keep track of "cumulative sum to cur_Node"

if cur_sum + cur_node.val == target: then count +=1
if (cur_sum + cur_node.val - target) in hashmap, then count += hashmap[cur_sum + cur_node.val - target]

cur_sum becomes cur_sum + cur_node.val, and 
 call traversal(node.left,cur_sum,targetSum)
 call traversal(node.right,cur_sum,targetSum)

NOTE: after traverse left child and right child ,we need to reverse the hashmap to make hashmap[cur_sum] -=1
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap = defaultdict(lambda:0)
        count = 0
        def traversal(node,cur_sum,targetSum):
            nonlocal count
            if not node:
                return
            cur_sum = cur_sum + node.val
            if cur_sum == targetSum:
                count +=1

            if (cur_sum - targetSum) in hashmap:
                count += hashmap[cur_sum - targetSum]

            hashmap[cur_sum] +=1

            traversal(node.left,cur_sum,targetSum)
            traversal(node.right,cur_sum,targetSum)

            hashmap[cur_sum] -=1

        traversal(root,0,targetSum)
        return count















