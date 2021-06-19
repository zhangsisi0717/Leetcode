from collections import deque
from typing import List
from collections import deque
"""
put 2* nums into a stack
pop out all the elements in the stack that is smaller than the current new element, and if the index current element  is 
smaller than len(nums), append it into the stack, else continue. After all the iterations, the element left in the stack should
be the largest the elements and set it to -1
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [None for _ in range(len(nums))]
        s = deque([(nums[0],0)])
        for i in range(1,2*len(nums)):
            idx = i if i < len(nums) else i-len(nums)
            while(s and nums[idx]>s[-1][0]):
                number, index = s.pop()
                if index < len(nums):
                    result[index] = nums[idx]

            if i <len(nums):
                s.append((nums[idx],i))

        for j in s:
            result[j[1]] = -1

        return result