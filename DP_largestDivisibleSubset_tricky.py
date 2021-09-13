from typing import List
"""
explaination:
step 1 : sort the list of nums first [1,2,3,4,8,9]
step 2 : use dynamic programming, use a list of keep track of largest length of subset if only considering
to index "idx",(nums[:index]) max_lenght = [1 for _ in range(len(nums))]
                                initial max_length = [1,1,1,....1]
                            prev_idx = [None,None,.....None]
    g_max_idx = None
    g_max_len = 1
    for i in range(len(nums)):
        temp_max = 1
        for j in range(0,i):
            if nums[i] % nums[j] == 0 and  max_length[j] + 1 > temp_max:
                then update max_length[i] =  max_length[j] + 1 
                            prev_idx[i] = j
        after updating max_length[i], compare it with global max length, and update  g_max_len and g_max_idx
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        max_len = 0
        max_idx = None
        prev_idx = [None] * n
        size = [1] * n
        for k in range(n):
            cur_max = 1
            for l in range(k):
                if nums[k] % nums[l] == 0 and cur_max < size[l] + 1:
                    cur_max = 1 + size[l]
                    prev_idx[k] = l
            size[k] = cur_max
            if max_len < size[k]:
                max_len = size[k]
                max_idx = k

        cur_idx = max_idx
        res = [nums[cur_idx]]
        while prev_idx[cur_idx] is not None:
            cur_idx = prev_idx[cur_idx]
            res.append(nums[cur_idx])

        return res

