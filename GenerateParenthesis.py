from collections import deque
#https://leetcode.com/problems/generate-parentheses/
"""
Approach 1: Brute force
Enumerate all the possible cadidates by using recursion, then check them one by one if they are valid
time complexity: recursion step : (2n)!/(n!*n!)
                then you have to check if each of them is valid, so total => 2n * (2n)!/(n!*n!)

"""
def generateParenthesis(n):
    def dfs(l_p,r_p):
        if l_p == 0 and r_p == 0:
            return [""]
        result = []

        if l_p >0:
            result += ["(" + i for i in dfs(l_p-1,r_p)]
        if r_p >0:
            result += [")" + i for i in dfs(l_p,r_p-1)]
        return result

    all_candi = dfs(n,n)

    def isValid(s):
        stack = deque([s[0]])
        for i in range(1,len(s)):
            if not stack:
                stack.append(s[i])
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
        return True if not stack else False

    return [s for s in all_candi if isValid(s)]

"""
Approach 2:
n
Σ Aj-1 * An-j = An
j=1

A valid parenthesis combination must be "(" + valid_paren<j-1 pairs of parenthesis> + ")" + valid_paren<n-j pairs of parenthesis

"""
from functools import cache
def generateParenthesis2(n):

    @cache
    def recur(n):
        if n == 0:
            return [""]
        else:
            res = []
            for j in range(1, n+1):
                res += ["(" + x + ")" + y for x in recur(j-1) for y in recur(n-j)]

            return res

    return recur(n)