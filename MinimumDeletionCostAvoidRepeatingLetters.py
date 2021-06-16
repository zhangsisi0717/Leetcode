from collections import deque
#https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
"""
use a stack to contain the results, if current letter == stack[-1]. then delete the smaller ones
"""
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stack = deque([[s[0],cost[0]]])
        total=0
        for i in range(1,len(s)):
            if s[i] == stack[-1][0] and stack[-1][1] < cost[i]:
                total += stack[-1][1]
                stack.pop()
                stack.append([s[i],cost[i]])

            elif s[i] == stack[-1][0] and stack[-1][1] >= cost[i]:
                total += cost[i]

            elif s[i] != stack[-1][0]:
                stack.append([s[i],cost[i]])

        return total



