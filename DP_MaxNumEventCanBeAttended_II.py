##https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
from typing import List
from bisect import bisect_left
from functools import cache
"""
subMax(i,k) return max value we can get considering list starting from index =i, and left k

if we choose current i, then we find the index of next event whose starting date value > end date of current event i
    max_val_choose = events[i] + subMax(next_index,k-1)
    
if not choose current i: max_val_not_choose = subMax(i+1,k)

return max(max_val_choose,max_val_not_choose)

time complexity:

    with out memoization, brute force search: (2**k) * lg(n)
    
    with memoization, dynamic programming: equals to fill a k*n table, so the complexity is (k*n), however 
    in order to find the next index, we use binary search, lg(n)
    so total compexity == (k*n) * lg(n)
"""


def maxValue(events: List[List[int]], k: int) -> int:

    @cache
    def subMax(i,k):
        if k<=0 or i>=len(events):
            return 0

        next_idx = bisect_left(events,[events[i][1]+1,events[i][1]+1,0])
        return max(events[i][2]+subMax(next_idx,k-1),subMax(i+1,k))

    return subMax(0,k)