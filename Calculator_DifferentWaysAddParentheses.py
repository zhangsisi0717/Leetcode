#https://leetcode.com/problems/different-ways-to-add-parentheses/
##"2*3-4*5"
from typing import List
"""
regard it as a binary tree, parent nodes are all operators and leaves are all numbers
e.g "2*3-4*5"
is    -
    /   \
    *   *
  / \  /  \
 2  3  4  5
 
 in order to calculate expressions after adding parenthesis, we could use a recursion
 "def calculate(substring)" returns the result of subexpression "substring"
 for idx in range(len(subtring)):
    if subtring[idx] is operator, then we cut the substring into two parts, and calculate results of left part and right part
    left = calculate(left)
    right = calculate(right)
    result = [i "operator" j for i in left for j in right]
    return result
    
Note: if there is no operator in the substring, then return int(string) directly
"""
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operator = {"+":lambda x,y:x+y,"-":lambda x,y:x-y,"*":lambda x,y:x*y,"/":lambda x,y:x/y}
        def calculate(substring):
            result=[]
            found_operator = False
            for idx in range(len(substring)):
                if substring[idx] in ("+-*/"):
                    found_operator=True
                    left = calculate(substring[:idx])
                    right = calculate(substring[idx+1:])
                    sub_re = [operator[substring[idx]](x,y) for x in left for y in right]
                    result += sub_re

            return result if found_operator else [int(substring)]

        return calculate(expression)




