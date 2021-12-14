#https://leetcode.com/problems/largest-number/
import copy
from functools import total_ordering
"""
define curstomized comapring method to find largest number
"""
@total_ordering
class strNum(object):
    def __init__(self, val):
        self.val = str(val)

    def __eq__(self, other):
        return (self.val == other.val)

    # def __ne__(self, other):
    #     return not (self.val == other.val)

    def __lt__(self, other):
        self_other = self.val + other.val
        other_self = other.val + self.val
        return other_self > self_other

def largestNumber(self, nums: List[int]) -> str:
    str_nums = [strNum(i) for i in nums]
    str_nums.sort(reverse=True)
    re = ""
    for j in str_nums:
        re += j.val
    return re if re[0]!="0" else "0"

a=strNum(57389)
b=strNum(573)

[498, 666, 135, 279, 416, 932, 407, 53, 521, 140, 256, 513, 553, 838, 339,45,35,67,123,56,456,890,1,44,53453,5675,867,3423,234567,786]

sort(key = lambda x: x[0])