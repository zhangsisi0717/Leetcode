from functools import cache
"""
def isLeave(i,j,k) return if the left substring s1[i:] and s2[j:] could combine to form substring of s3[k:]

"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def isLeave(i,j,k):
            if k>=len(s3): return True

            re_1,re_2 = False,False
            if i<len(s1) and s1[i] == s3[k]:
                re_1 = isLeave(i+1,j,k+1)

            if j<len(s2) and s2[j] == s3[k]:
                re_2 = isLeave(i,j+1,k+1)

            return re_1 or re_2

        return isLeave(0,0,0)