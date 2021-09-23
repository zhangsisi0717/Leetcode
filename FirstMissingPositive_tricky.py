##https://leetcode.com/problems/first-missing-positive/
"""
nums = [3,4,-1,1]
we want to modify nums in place, such that nums[idx]=idx+1 eg. [1,2,3,4....]
for i in nums,
cur_num = i
if i in right postions, just continue,
if i<0 or i>len(nums), then it should not be in the list,
    nums[i-1] = -1
    continue
else:
    we put "i" at correct postion:
        new_num = nums[i-1]
        nums[i-1] = cur_num
        cur_num = new_num
        and keep doing the same thing for the cur_nums until we can not put cur_num into nums anymore, then break

After we updating the nums, we find the smallest index in nums that nums[index] == -1 and return index+1
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == i+1:
                continue
            x = nums[i]
            nums[i] = -1
            while True:
                if x <= 0 or x > len(nums):
                    break
                if nums[x - 1] == x:
                    break
                y = nums[x - 1]
                nums[x - 1] = x
                x = y
        for i in range(n):
            if nums[i] == -1:
                return i + 1
        else:
            return n + 1