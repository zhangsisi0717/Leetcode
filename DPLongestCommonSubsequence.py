
"""
#https://leetcode.com/problems/longest-common-subsequence/

https://www.techiedelight.com/longest-common-subsequence/
    if end with the same element:
        LCS(A[1,2..m],B[1,2,3...n]) = LCS(A[1,2,3...m-1],B[1,2,3...n-1]) + A[m]/B[n]

        lcs(i,j) = lcs(i-1,j-1) + A[i]/A[j] (i,j is the surffix)

    if end with different element:
        LCS(A[1,2..m],B[1,2,3...n]) = longer one of (LCS(A[1,2,3...m-1],B[1,2,3...n]), LCS(A[1,2,3...m], B[1,2,3...n-1]))

        lcs(i,j) = max (lcs(i-1,j), lcs(i, j-1) )  (i,j is the surffix)

"""
from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  ##of only need to return the length
        @cache
        def lss(i,j):
            if i < 0 or j<0:
                return 0
            if text1[i] == text2[j]:
                return lss(i-1,j-1) + 1

            return max(lss(i-1,j), lss(i,j-1))

        return lss(len(text1)-1,len(text2)-1)

def longestCommonSubsequenceWithOutputString(self, text1: str, text2: str) -> int:  ###if want to return the common substring
    @cache
    def lss(i,j):
        if i < 0 or j<0:
            return ()
        if text1[i] == text2[j]:
            re = list(lss(i-1,j-1))
            re.append(text1[i])
            return tuple(re)

        re1 = lss(i-1,j)
        re2 = lss(i,j-1)

        return re1 if len(re1)>len(re2) else re2


    return lss(len(text1)-1,len(text2)-1)
