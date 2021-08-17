from functools import cache
"""
explaination: use binary search to find the minimal capacity that can ship all items within given days
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lb,ub = max(weights), sum(weights)

        def isEnough(cap):
            i,cur,total = 0,0,0
            while(i<len(weights)):
                if cur+weights[i] <= cap:
                    cur += weights[i]
                    i+=1
                else:
                    total += 1
                    cur = 0
            return total+1<=days

        while(lb<ub):
            mid = int((lb+ub)/2)
            if isEnough(mid):
                ub = mid
            else:
                lb = mid+1
        return lb





