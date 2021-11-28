from typing import *
#longest Palindrom s
##https://leetcode.com/problems/longest-palindromic-substring/solution/
"""
isPalin(i,j) return if a substring s[i:j+1] is Palin

then iterate i,j => update the maxLength

(Since we used memoization here, the time comlexity is only O(N2)), space is also O(N2)

"""
from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pre,sur = 0,0

        @cache
        def isPalin(i,j):
            if i<0 or j>= len(s) or i>j:
                return False

            if i == j:
                return True
            if s[i] == s[j] and i+1==j:
                return True

            if s[i] == s[j] and isPalin(i+1,j-1):
                return True

            return False

        for i in range(len(s)):
            for j in range(len(s)):
                if isPalin(i,j) and j-i>sur-pre:
                    pre,sur = i,j

        return s[pre: sur+1]

