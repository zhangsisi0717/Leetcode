from collections import deque
def minRemoveToMakeValid(s: str) -> str: ##https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/
    invalidleft=deque()
    invalideright=deque()
    for i in range(len(s)):
        if s[i] == "(":
            invalidleft.append(i)

        elif s[i] == ")" and invalidleft:
            invalidleft.pop()

        elif s[i] == ")" and (not invalidleft):
            invalideright.append(i)

    re=""
    invalid_set = set(invalidleft).union(set(invalideright))
    return "".join([s[idx] for idx in range(len(s)) if idx not in invalid_set])
