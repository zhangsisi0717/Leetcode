##https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List
"""
lb, ub = matrix[0][0], matrix[n - 1][n - 1]
mid = (lb + ub) // 2

                          1.the largest number in matrix that is smaller than "mid" and 
                          2. smallest number in matrix that is larger than "mid"
                          3. count = number of numbers that is smaller and equal to "mid"
                          
        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower                       
"""
def countLessEqual(matrix, mid):
    """
    countLessEqual returns:
          1.the largest number in matrix that is smaller than "mid" and
          2. smallest number in matrix that is larger than "mid"
          3. count = number of numbers that is smaller and equal to "mid"

    start search from the "lower left corner" to "upper right corner"
    """
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    smaller,larger = (-1)*float("inf"),float("inf")
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # As matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1

        else:
            # As matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

        count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower

    return start




















