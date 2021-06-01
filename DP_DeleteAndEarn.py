from collections import Counter
from functools import cache
"""
https://leetcode.com/problems/delete-and-earn/
nums = [2,2,3,3,3,4]
ordered_num = [2,3,4]
num_to_count = {2:2,3:3,4:1}
dynamic program: recursion(i) return maximum points counting from index i
if ordered_num[i] + 1 < ordered_num[i+1] => then we should always include ordered_num[i], so recursion(i) = ordered_num[i]*frequency of order_nums[i] + recursion(i+1)
if ordered_num[i] + 1 == ordered_num[i+1] => then i and i+1 are neighbors,  recursion(i) = max(include ith num , not include ith num)
    include ith num = ordered_num[i]*frequency of order_nums[i] + recursion(i+2)
    not_include ith num = recursion(i+1)

"""

def deleteAndEarn(nums):
    num_to_count = Counter(nums)
    ordered_num = sorted([i for i in num_to_count.keys()])

    @cache
    def recursion(i):
        if i >= len(ordered_num):
            return 0
        if i == len(ordered_num)-1:
            return num_to_count[ordered_num[i]]*ordered_num[i]
        if ordered_num[i+1] - 1 > ordered_num[i]:
            return num_to_count[ordered_num[i]]*ordered_num[i] + recursion(i+1)

        add_i = num_to_count[ordered_num[i]]*ordered_num[i] + recursion(i+2)
        not_add_i = recursion(i+1)
        return max(add_i,not_add_i)

    return recursion(0)










