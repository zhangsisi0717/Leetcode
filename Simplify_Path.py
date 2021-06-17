"/home/./sisi/../../yuchen"
#https://leetcode.com/problems/simplify-path/
from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = deque([])
        for i in dirs:
            if i in ("","."):
                continue

            elif i == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(i)

        re = "/" + "/".join(stack)
        return re







