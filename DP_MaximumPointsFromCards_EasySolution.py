#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
from typing import List
"""
purpose: each time, choose from start or end, return max points we can get
in this question, if we do need to iterate all the paths => 2^K complexity
          
"""

"""
time complexity: O(2K)
cardPoints = [1,2,3,4,5,6,1], k = 3
start_pointer = k-1
end_pointer = len(cardPoints)-1

if we always choose from start, then start_pointer will end at index = k-1, end_pointer = len(cardPoints)-1
if we always choose from end, then start_pointer will end at index = 0, end_pointer = len(cardPoints)-k
so we only have 2K options

each time start -=1, end-=1, then calculate current sum value 
and we can determine the maximum result by this way
"""

def maxScore(cardPoints: List[int], k: int) -> int:
    s = sum(cardPoints[:k])
    max_val = s
    start = k - 1

    end = len(cardPoints) - 1
    if start == end:
        return max_val

    while start >= 0:
        s -= cardPoints[start]
        s += cardPoints[end]
        start -= 1
        end -= 1
        if s > max_val:
            max_val = s

    return max_val

"""
DO not use recursion:  
this way Time complexity O(2^k)    
        def subMaxScore(i,j,k):
            if k<=0 or i>j:
                return 0
            return max(cardPoints[i]+subMaxScore(i+1,j,k-1),cardPoints[j]+subMaxScore(i,j-1,k-1))
"""