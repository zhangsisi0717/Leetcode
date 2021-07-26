"""
https://leetcode.com/problems/sum-of-subarray-minimums/
we need to keep track of : 1. first element(l_idx) to the right that is smaller than arr[idx]
                           2. first element(r_idx) to the left that is smaller than arr[idx]

so the sum of all the subarrays whose smallest value is arr[idx] ==  (idx-l_idx) * (r_idx-idx)

we can use one stack to get both l_idx and r_idx

it is trivial that we can get r_idx by using stack and it is worth noting that after all the operations,
the l_idx is actually left to the idx in the stack
"""
"""
the following is one scanning aprroach,
but we can use two scanning approach which is clearer, scan the list twice to get both 
 1. first element(l_idx) to the right that is smaller equal than arr[idx] (to avoid redundant sum when there are duplicates)
 2. first element(r_idx) to the left that is smaller than arr[idx]
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        arr.append(float('-inf'))
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop() # now, arr[i] is the first element to the right strictly less than arr[idx]
                res += arr[idx] * (i - idx) * (idx - (stack[-1] if stack else -1))
            stack.append(i) # element can be greater than or equal to the peek element in the stack

        return res % (10**9 + 7)