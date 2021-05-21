from bisect import bisect_left
from collections import deque
a = deque([2.5, 3, 6, 77, 334, 777])
bisect_left(a,2.6)
a.insert(1,2.6)




#https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb,ub = 0,len(nums)-1
        if target > nums[-1] or target < nums[0]:return -1
        while(lb<=ub):
            mid = lb + (ub-lb) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ub = mid -1

            elif nums[mid] < target:
                lb = mid+1

        return lb if nums[lb] == target else -1