#https://leetcode.com/problems/search-a-2d-matrix/solution/
from typing import List
"""
make it into a sorted array and use binary search to find it
"""
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    nums = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
    lb,ub = 0,len(nums)-1
    while(lb<ub):
        mid = lb + (ub-lb) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            ub = mid -1

        elif nums[mid] < target:
            lb = mid+1

    return True if nums[lb] == target else False