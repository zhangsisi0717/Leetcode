from collections import Counter
"""
p
"""
def fourSum(nums, target):
    num_to_count = Counter(nums)
    unique_num = [i for i in num_to_count.keys()]
    num_count = [j for j in num_to_count.values()]
    def sumToIdx(idx, target, num_left, num_count):
        if idx == 0:
            return 4*[unique_num[0]] if num_count[0]>=4 else False
        if target<0: return False
        if target == 0: return []
        ub = min(num_left, num_count[idx], target // unique_num[idx])
        re = []
        for i in range(0,ub+1):
            num_count_copy = num_count.copy()
            num_count_copy[idx] = num_count_copy[idx]-i
            temp_re = sumToIdx(idx - 1, target-i*unique_num[idx], num_left-i, num_count_copy)
            if temp_re != False:
                temp_re = i*[unique_num[idx]] + temp_re

    return sumToIdx(len(nums)-1,target,4)

nums = [2,2,2,2,2]
target = 8
fourSum(nums, target)

