## 1. find the index of the minimal element(min_idx)
## 2. determinine which part should target be (before min_idx or after min_idx)
#3. do normal  binary search

#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] > nums[i]:
                min_idx = i
                break

        idx_add = 0
        if min_idx ==0:
            new_l = nums
        else:
            if nums[0] <= target <= nums[min_idx-1]:
                new_l = nums[:min_idx]
            else:
                new_l = nums[min_idx:]
                idx_add = min_idx

        lb,ub = 0,len(new_l)-1
        if target > new_l[-1] or target < new_l[0]:return -1
        while(lb<=ub):
            mid = lb + (ub-lb) // 2
            if new_l[mid] == target:
                return mid+idx_add
            elif new_l[mid] > target:
                ub = mid -1

            elif new_l[mid] < target:
                lb = mid+1

        return (lb+idx_add) if new_l[lb] == target else -1
                