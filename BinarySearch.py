from bisect import bisect_left
from collections import deque
a = deque([2.5, 3, 6, 77, 334, 777])
bisect_left(a,2.6)
a.insert(1,2.6)


from bisect import bisect_right
a = [[10,20]]
bisect_right(a,[20,30])


l = [1,2,2,2,3,4,5,6]
from typing import List
def bisectRight(lb,ub,num,l):
    """
    bisectRight is just the regular binary search
    """
    while(lb<ub):
        print(f"lb={lb},ub={ub}")
        mid = int((lb + ub)/2)
        print(f"mid={mid}")
        if l[mid]>num:
            ub = mid-1
        else:
            lb = mid +1
    return lb

def bisectLeft(lb,ub,num,l):
    while(lb<ub):
        mid = int((lb + ub)/2)
        if l[mid]>num:
            ub = mid-1
        elif l[mid]==num:
            """
            only difference here
            """
            ub = mid
        else:
            lb = mid +1
    return lb


bisectLeft(0,len(l)-1,2,l)

#https://leetcode.com/problems/binary-search/
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         lb,ub = 0,len(nums)-1
#         if target > nums[-1] or target < nums[0]:return -1
#         while(lb<ub):
#             mid = (ub+lb) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 ub = mid -1
#
#             elif nums[mid] < target:
#                 lb = mid+1
#
#         return lb if nums[lb] == target else -1
#
# ##https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# """
# bisect_left and biset_right implementations
# find the first and last index of target element
# """
# import random
# """
# bisect_right
# """
# def binarySearch(lb,ub,num,l):
#     while(lb<ub):
#         print(f"lb={lb},ub={ub}")
#         mid = int((lb + ub)/2)
#         print(f"mid={mid}")
#         if l[mid]>num:
#             ub = mid-1
#         elif l[mid]==num:
#
#             lb = mid+1
#         else:
#             lb = mid +1
#     return lb
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums: return [-1,-1]
#         lb,ub = 0,len(nums)-1
#         while(lb+1<ub):
#             mid = lb + (ub - lb)//2
#             if nums[mid]>target:
#                 ub = mid-1
#             elif nums[mid] == target:
#                 """
#                 !!this part is bi_sect left!!
#                 only difference is: if nums[mid] == target => ub =mid
#                 """
#                 ub = mid
#             else:
#                 lb = mid +1
#         l_idx = lb if nums[lb] == target else ub
#
#         lb,ub = 0,len(nums)-1
#         while(lb+1<ub):
#             mid = lb + (ub - lb)//2
#             if nums[mid]>target:
#                 ub = mid-1
#             elif nums[mid] == target:
#                 """
#                 !!this part is bi_sect right!!
#                 only difference is: if nums[mid] == target => lb =mid
#                 """
#                 lb = mid
#             else:
#                 lb = mid +1
#
#         r_idx = ub if nums[ub] == target else lb
#         if l_idx>len(nums) -1 or nums[l_idx] != target: return [-1,-1]
#         return [l_idx,r_idx]
#
# nums = [5,7,7,8,8,10]
# target = 8