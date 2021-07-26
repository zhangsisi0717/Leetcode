#https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    """
    Bitwise Operators

   bitwise a ^ b  =>  (a + b) % 2

if a == 60, b == 13,
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011

a + b == (a^b) + (a&b) << 1
"""
def getSum(a: int, b: int) -> int:

    if a == 0:
        return b
    if b == 0:
        return a

    negative_one = ~0

    def _add(a, b):
        if b == 0:
            return a
        return _add(a ^ b, (a & b) << 1)

    if a > 0 and b > 0:
        return _add(a, b)
    if a < 0 and b < 0:
        return negative_one * _add(negative_one*a, negative_one*b)

    if a > 0 and b < 0:
        a, b = b, a

    # now we have a < 0, b > 0
    if negative_one * a == b:
        return 0

    if negative_one * a < b:
        return negative_one * _add(negative_one*a, negative_one*b)
    else:
        return _add(a, b)





