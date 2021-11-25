from type_checking import *
##https://leetcode.com/problems/maximum-length-of-repeated-subarray/
##https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""
find longest common substring: set i,j as suffix of nums2 and nums1
create a table to keep track of the longest common string ending at index i and j
 if num1[j] == num2[i] => then lcs[i][j] == lcs[i-1][j-1] + 1 else 0
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        lcs_suffix = [[0 for i in range(len(nums1)+1)] for j in range(len(nums2)+1)]
        lcs = 0
        for i in range(1,len(nums2)+1): ##i => nums2 , j => nums1
            for j in range(1,len(nums1)+1):
                lcs_suffix[i][j] = lcs_suffix[i-1][j-1]+1 if nums2[i-1] == nums1[j-1] else 0
                if lcs_suffix[i][j] >lcs:
                    lcs = lcs_suffix[i][j]

        return lcs
