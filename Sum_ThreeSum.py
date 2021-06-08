#https://leetcode.com/problems/3sum/
"""
[-1,0,1,2,-1,-4] without sorting
result = set()
for i to (0,end):
    seen = set()
    for j to (i+1,end):
        complement = -value_i-value_j
        if you have seen complement in the seen:
            add tuple(sorted([val_i,val_j,complement])) to set, sort could avoid duplicates

        if not seen:
            seen.add(val_j)

"""
##three sums to 0
def threeSum(nums):
    res= set()
    for i, val1 in enumerate(nums):
        seen = set()
        for j, val2 in enumerate(nums[i+1:]):
            complement = -val1 - val2
            if complement in seen:
                res.add(tuple(sorted((val1, val2, complement))))
            seen.add(val2)
    return res

##three sums to the closest:
#https://leetcode.com/problems/3sum-closest/
"""
step1: sort the list
step2: i from 0 to end, and another two pointer: lb_pointer, ub_pointer = 0, len(list)-1
step3: keep track of current smallest difference, 
    while  lb_pointer < ub_pointer:
        if nums[i] + nums[lb_pointer] + nums[lb_pointer] > target => means we need to move ub_pointer to the left
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff


###three sum to smaller:
##https://leetcode.com/problems/3sum-smaller/
"""
        !!!Two pointer method!!! Three sum == certain target could also use this two pointer method    O(n2) 
step 1: sort nums
step 2: implement two sum smallerthan .. if there are only two numbers, lb,ub =0,len(nums)-1
               while(lb<ub):
                if nums[lb] + nums[ub] >= target:
                    ub -=1

                else:
                    count += ub - lb
                    lb +=1
step 3: for i in range(0,len(nums)) => total count += twoSumSmaller(start_index = i+1, target = tartget- nums[i])
"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:return 0
        def twoSumSmaller(nums,lb,target):
            count=0
            lb = lb
            ub = len(nums)-1
            while(lb<ub):
                if nums[lb] + nums[ub] >= target:
                    ub -=1

                else:
                    count += ub - lb
                    lb +=1

            return count
        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            count += twoSumSmaller(nums,i+1,target-nums[i])
        return count
