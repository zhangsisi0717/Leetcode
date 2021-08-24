#https://leetcode.com/problems/largest-1-bordered-square/
from functools import cache
"""
keep track of consecutive "1s" to the right and consecutive "1s" to the bottom, for all the elements in the matrix
then for grid[i][j],  longest_length = min(consecutive ones to the right, ones to the bottom)

for length in (longest_length,1) check if it forms a border

time compexiy : n = rows, n = columns, O(n*n*n)
"""
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        table = [[[0,0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ##table[0]: consecutive 1s to the right
        ##table[1]: consecutive 1s to the bottom
        for r in range(len(grid)-1,-1,-1):
            for c in range(len(grid[0])-1,-1,-1):
                if grid[r][c] == 0:
                    table[r][c] = [0,0]
                else:
                    if r == len(grid)-1:
                        table[r][c][1] = 1
                    if 0<=r<len(grid)-1:
                        table[r][c][1] = table[r+1][c][1] + 1
                    if c == len(grid[0])-1:
                        table[r][c][0] = 1

                    if 0<=c<len(grid[0])-1:
                        table[r][c][0] = table[r][c+1][0] + 1
        max_border = 0
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j] == 1:
                    for length in range(min(table[i][j]),0,-1):
                        if table[i][j+length-1][1]>=length and table[i+length-1][j][0]>=length:
                            max_border = max(max_border,length)
                            break
        return max_border **2






