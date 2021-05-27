#https://leetcode.com/problems/container-with-most-water/
import numpy as np

"""

Approach 1: Comlexity O(n)
height = [1,8,6,2,5,4,8,3,7]
Start from the leftmost(i=0) and right most(j=n-1), we want to try to move to center, if height[i] < height[j] , then there is absolute no benifits to move the high one, then
we move the lower one (may be benifits), and keep track of the largest area until index i==j

"""
def maxArea2(height) -> int:
    i,j = 0, len(height)-1
    cur_max = min(height[i],height[j]) * (len(height)-1)
    while(i<j):
        cur_max = max(cur_max, min(height[i],height[j])*(j-i))
        if height[i] < height[j]:
            i +=1
        else:
            j -=1

    return cur_max



"""
Approach 2:
complexity: nlogn
height = [1,8,6,2,5,4,8,3,7]
1. np.argsort the list x1 < x2 < x3 < x4 < x5
2. iterate from x5 to x1 , when we arrive Xi, we need to calculate the max area if using Xi and the other end should be larger than Xi, then under that circumstance,
the further other end is to Xi, the larger of the area.
"""
def maxArea(height) -> int:
    order = np.argsort(height)
    cur_min_idx = order[-1]
    cur_max_idx = order[-1]
    cur_max_area = 0
    for idx in range(len(height)-2,-1,-1):
        cur_max_area = max(order[idx]*abs(cur_min_idx-order[idx]), order[idx]*abs(cur_max_idx-order[idx]),cur_max_area)
        cur_min_idx = min(cur_min_idx,order[idx])
        cur_max_idx = max(cur_max_idx,order[idx])

    return cur_max_area







