"""
#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/submissions/
brute force search:

dfs(start_idx,cur_sum,target,cur_group,k)
dfs returns if current group could be finished given cur_sum and start_idx

start to see if we could find couple of numbers in nums combined to be target, if YES, then we
use left numbers to see if we could make another target(group 1)...do this recursively, until
we met group K, then return True
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = sum(nums) // k
        if total % k !=0 or not nums or len(nums)==0:
            return False
        chosen = [False for _ in range(len(nums))]

        def dfs(start_idx,cur_sum,target,cur_group,k):
            if cur_sum > target:
                return False

            if cur_group == k:
                return True

            if cur_sum == target:
                return dfs(0,0,target,cur_group+1,k)

            for idx in range(start_idx,len(nums)):
                if chosen[idx]:
                    continue

                chosen[idx] = True
                if dfs(idx+1,cur_sum+nums[idx],target,cur_group,k):
                    return True
                chosen[idx] = False

            return False
        return dfs(0,0,target,0,k)
