##https://leetcode.com/problems/jump-game-ii/
from typing import List
from functools import cache
"""
smallest jumps reach to last index
f(idx) return smallest jumps to reach to last index starting from postion idx
nums = [2,3,1,1,4]
f(idx) == min[1+f(idx+1), 1+f(idx+2)....1+f(idx+i))]  =>  i == nums[idx]
"""
def jump(nums: List[int]) -> int:
    @cache
    def f(idx):
        if idx == len(nums)-1:
            return 0

        all_step = [1+f(i) for i in range(idx+1, min(idx+nums[idx]+1,len(nums)))]
        if not all_step: return float("inf")
        return min(all_step)

    return f(0)

