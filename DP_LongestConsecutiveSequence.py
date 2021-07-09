#https://leetcode.com/problems/longest-consecutive-sequence/
from functools import cache
"""
array = [100,4,200,1,3,2]
unsoted array, to find longest consecutive subsequence (1,2,3,4) with O(n)

maxLength(num) returns longest length if num is the maximum number
then:
maxLength(num) = 1 + maxLength(num-1)
(if num is not in numset,then return 0) , keep track of unvisited number
"""
def longestConsecutive(nums: List[int]) -> int:
    numset = set(nums)
    unvisited = set(nums)
    @cache
    def maxLength(num):
        if num not in numset:
            return 0

        unvisited.remove(num)
        return 1 + maxLength(num-1)

    maximum=0
    for i in nums:
        if i in unvisited:
            maximum = max(maximum,maxLength(i))

    return maximum