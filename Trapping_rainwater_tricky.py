"""
##https://leetcode.com/problems/trapping-rain-water/
for any height[i], keep track of left_running_max and right_running_max (i not included)
and the water level of height[i] = min(left_running_max[idx],right_running_max[idx])
and the water need to be filled = water level of height[i] - height[i],
(water level of height[i] - height[i]) could be negative, so max(0,(water level of height[i] - height[i]))
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left_running_max = [0 for _ in range(len(height))]
        right_running_max = [0 for _ in range(len(height))]
        n = len(height)
        l_max = 0
        r_max = 0
        for i in range(n):
            left_running_max[i] = l_max
            right_running_max[n-1-i] = r_max
            l_max = max(l_max, height[i])
            r_max = max(r_max, height[n-1-i])

        re = 0
        for idx in range(len(height)):
            re += max(0, min(left_running_max[idx],right_running_max[idx]) - height[idx])
        return re








