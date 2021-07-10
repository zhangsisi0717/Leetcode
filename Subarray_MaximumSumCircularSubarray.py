from typing import List
"""
a = [1,-2,3,-2]

without circular, we only need to keep track of global_max and cur_max ending at index i, and return the final result
with circular, we would need to record both  (global_max,global_min, cur_max, cur_min)

return max(global_max,total-global_min) if total != global_min else global_max 

{{
    one thing need to pay attention is that, if total_sum == global_min, which means the smallest is to add all the elements,
    then should return global_max, insead of max(global_max, total_sum-global_min) 
}}
"""
def maxSubarraySumCircular(nums: List[int]) -> int:
    total=nums[0]
    global_max,global_min = nums[0],nums[0]
    cur_max,cur_min = nums[0],nums[0]
    for idx in range(1,len(nums)):
        cur_max = max(nums[idx]+cur_max,nums[idx])
        global_max = max(global_max,cur_max)

        cur_min = min(nums[idx]+cur_min,nums[idx])
        global_min = min(global_min,cur_min)

        total += nums[idx]

    return max(global_max,total-global_min) if total != global_min else global_max

