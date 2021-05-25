# class Solution:
#     def search(nums, target) -> int:
#         lb,ub = 0,len(nums)-1
#         while(lb<=ub):
#             mid = lb + (ub-lb) //2
#             if target == nums[mid]: return mid
#             if nums[lb]<target<nums[mid]:
#                 ub = mid - 1
#
#             elif nums[mid] < target < nums[ub]:
#                 lb = mid + 1
#
#             elif nums[lb] > nums[mid] and (target > nums[lb] or target < nums[mid]):
#                 ub = mid -1
#
#             elif nums[mid]> nums[ub] and (target > nums[mid] or target < nums[ub]):
#                 lb = mid + 1
#
#         return -1

def search(nums, target) -> int:
    lb,ub = 0,len(nums)-1
    while(lb<=ub):
        mid = lb + (ub-lb) //2
        if target == nums[mid]: return mid
        # if nums[ub] < nums[mid] and nums[ub] < nums[mid]:
        if nums[ub] < nums[lb] < nums[mid]:
            if nums[lb]<target<nums[mid]:
                ub = mid -1

            else:
                lb = mid + 1

        elif nums[mid] < nums[ub] < nums[lb]:
            if nums[mid] < target < nums[ub]:
                lb = mid + 1
            else:
                ub = mid - 1




