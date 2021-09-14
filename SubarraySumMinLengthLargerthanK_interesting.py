##https://leetcode.com/problems/minimum-size-subarray-sum/
"""
two pointer method

"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j,cur_sum = 0,0,nums[0]
        re = float("inf")
        if sum(nums) < target: return 0
        while j<len(nums)-1:
            if nums[j]>= target:
                return 1
            j +=1
            cur_sum = cur_sum + nums[j]
            while i<j and cur_sum-nums[i]>=target:
                cur_sum -= nums[i]
                i+=1
            if cur_sum >= target:
                re = min(re,j-i+1)
        return re












