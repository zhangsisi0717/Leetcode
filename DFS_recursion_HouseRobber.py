#https://leetcode.com/problems/house-robber/
from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def maxMoney(idx):
            if idx == len(nums)-1:
                return nums[idx]

            if idx>=len(nums):
                return 0

            return max(nums[idx]+maxMoney(idx+2),maxMoney(idx+1))

        return maxMoney(0)