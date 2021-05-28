#https://leetcode.com/problems/rotate-image/
import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m_copy = copy.deepcopy(matrix)
        for row in range(n):
            for col in range(n):
                matrix[col][n-1-row] = m_copy[row][col]