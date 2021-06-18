#https://leetcode.com/problems/integer-break/
from functools import cache
"""
f(x) return the maximal product of x 
f(x) ==  i * f(x-i) for i in range(1,x)
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def _f(x):
            if x <= 3:
                return x
            return max(x, max(i * _f(x - i) for i in range(1, x)))

        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            return _f(n)