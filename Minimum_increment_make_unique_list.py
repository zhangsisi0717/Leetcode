##https://leetcode.com/problems/minimum-increment-to-make-array-unique/
from typing import List
"""
step 1 :sort
step 2: keep track of unique set and cur_max
step 3: iterate the list, 
if cur number not in unique:
    add unique_set.add(this number), cur_max = max(cur_max,this_number)

if cur number in unique:
    then this number must increment to (cur_max + 1)

"""
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        cur_max = (-1)*float("inf")
        unique = set()
        incre = 0
        for idx in range(len(sorted_nums)):
            if sorted_nums[idx] in unique:
                incre += (cur_max + 1 - sorted_nums[idx])
                cur_max +=1
                unique.add(cur_max)
            else:
                unique.add(sorted_nums[idx])
                cur_max = max(cur_max,sorted_nums[idx])

        return incre