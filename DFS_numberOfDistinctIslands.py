from typing import List
from collections import defaultdict
"""
find number of unique islands

dfs + hashset 
1.dfs to generate all the islands with coordinates of block
2. move upper left block to (0,0) for each island, then [[0, 0], [0, 1], [1, 0], [1, 1]] and [[2, 3], [2, 4], [3, 3], [3, 4]] are equal
because [[2, 3], [2, 4], [3, 3], [3, 4]] can become [[0, 0], [0, 1], [1, 0], [1, 1]] after offset
3.use hashset to keep unique islands
"""
def numDistinctIslands(grid: List[List[int]]) -> int:
    num_r,num_c = len(grid),len(grid[0])
    visited = [[False for _ in range(num_c)] for _ in range(num_r)]
    def dfs(r,c):
        visited[r][c] = True
        result = [[r,c]]
        neighbors = [[r,c-1],[r,c+1],[r-1,c],[r+1,c]]
        for i,j in neighbors:
            if 0<=i<num_r and 0<=j<num_c and not visited[i][j] and grid[i][j]==1:
                temp = dfs(i,j)
                result += temp

        return result

    hashSet = set()
    for i in range(num_r):
        for j in range(num_c):
            if not visited[i][j] and grid[i][j]==1:
                re = dfs(i,j)
                # re.sort()
                off_x,off_y = 0-re[0][0],0-re[0][1]
                for idx in range(len(re)):
                    re[idx] = (re[idx][0]+off_x,re[idx][1]+off_y)
                hashSet.add(tuple(re))

    return len(hashSet)






grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
numDistinctIslands(grid)
