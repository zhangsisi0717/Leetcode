#https://leetcode.com/problems/smallest-range-i/
#https://leetcode.com/problems/smallest-range-ii/
"""
explainations: for a sorted array [a1,a2,a3....aN], to get minimal difference,
we must increase the number from a1 to ai, and decrease a(i+1) to aN, so the point
is to find the larset index = i that needs to be increased, then the optimal
minimal difference will only depend on "a1(min), ai, a(i+1) and aN(max)"

    minimal_difference = g_max - g_min
    since a1+k <= ai+k, a(i+1)-k<=aN-k:
        g_max = max(ai+k, aN-k),
        g_min = min(a1+k, a(i+1)-k)

"""
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        minimal,maximum = nums[0],nums[-1]
        re = maximum - minimal
        for i in range(len(nums)-1):
            g_max = max(nums[i]+k, maximum-k)
            g_min = min(minimal+k,nums[i+1]-k)
            re = min(re, g_max-g_min)
        return re








