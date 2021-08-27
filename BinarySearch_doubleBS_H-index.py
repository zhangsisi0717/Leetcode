#https://leetcode.com/problems/h-index/
from bisect import bisect_left
"""
double binary search number of citations, lb,ub = 0, len(citation)
time comlexity (nlgn)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)
        lb,ub = 0,n
        while(lb+1<ub):
            mid = (lb + ub) //2
            idx = bisect_left(citations,mid)
            if (n-idx) >= mid:
                lb = mid

            else:
                ub = mid-1

        return lb if n-bisect_left(citations,ub) < ub else ub