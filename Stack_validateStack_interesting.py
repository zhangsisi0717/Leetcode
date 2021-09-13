##https://leetcode.com/problems/validate-stack-sequences/solution/
from collections import deque
"""
step 1 : stack = [], add element one by one from pushed
step 2: once we found out that the popped[0] == stack[-1], which means stack[-1] is the next value to be popped, then we keep popping out the elements until stack[-1] != poppped[0]

step 3: return True if we popped out all elements in stack
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        popped = deque(popped)
        for i in pushed:
            stack.append(i)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()

        return True if not stack else False





