"""
###https://leetcode.com/problems/remove-k-digits/

Make it smallest: stack "Increasing" order
Makr it largest: stack "Decreasing" order
explaination: make sure the number in "stack" is in "INCREASING order", if we
checked all the digit in "num" and k>0, just popout top k elements in "stack"

stack=[1,2,3,4,5,6], if need to delete one element to make it smallest, then it must be the last element "6"


1. if stack is not empty and stack[-1]> next digit:
        stack.pop()

   else:
        stack.append(digit)

2. in the end,
    if k>0, then popout k top elements in the stack
    if stack is like ["0",'0','0','2','0','0'], popout all the
    "0" before the first digit that is not "0"

3. return stack
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        for digit in num:
            while k>0 and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)


        finalStack = numStack[:-k] if k else numStack

        return "".join(finalStack).lstrip('0') or "0"














