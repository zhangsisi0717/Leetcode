from collections import deque
"""

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

re = dfs(4,4)

s = "()()())()"