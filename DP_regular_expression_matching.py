##https://leetcode.com/problems/regular-expression-matching/

"""
i=> index of s
j=> index of p
start from i=0,j=0

NOTE: even if i has reached to the end, and j is not at the end, there still could be a match since there may exist "*", only senario that we need to stop the program is when j (pattern) has reaced to the end

so:
first check if current letter matched : start_matched = i<len(s) and (p[j] == s[i] or p[j] == ".")

then if p[j+1] == "*", we have two directions to go: one is to skip the "*" and call matched(i,j+2)
another one is to call matched(i+1, j)

if start_matched is not matched, then only if p[j+1] == "*", we have chance to find the match,

otherwise return false
"""
from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def matched(i,j):
            if j>=len(p):
                return i>=len(s)

            start_matched = i<len(s) and (p[j] == s[i] or p[j] == ".")
            if start_matched: ##if start letter of s and p is matched
                if j+1< len(p) and p[j+1] == "*": ##if p[j+1] is star, then we have two ways
                    return matched(i,j+2) or matched(i+1,j)
                else:
                    return matched(i+1,j+1)

            else: ### start letter is not matched, then only if p[j+1] == "*", we have chance to find the match
                if j+1< len(p) and p[j+1] == "*":
                    return matched(i,j+2)

            return False

        return matched(0,0)


