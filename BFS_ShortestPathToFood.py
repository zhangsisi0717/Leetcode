###https://leetcode.com/problems/shortest-path-to-get-food/
from type_checking import *
from collections import deque
def getFood(grid: List[List[str]]) -> int:
    numSteps = dict()
    numRows = len(grid)
    numCols = len(grid[0])
    queue = deque([])
    cur,found=None,False
    for i in range(numRows):
        if found:
            break
        for j in range(numCols):
            if grid[i][j] == "*":
                print(i,j)
                queue.append((i,j))
                numSteps[(i,j)] =0
                found = True
                break

    while(queue):
        r,c = queue.popleft()
        for n_r,n_c in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if 0<=n_r<numRows and 0<=n_c<numCols and (n_r,n_c) not in numSteps and grid[n_r][n_c] != "X":
                if grid[n_r][n_c] == "#":
                    return numSteps[r][c] + 1
                queue.append((n_r,n_c))
                numSteps[n_r][n_c] = numSteps[r][c] + 1

    return -1

grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]

getFood(grid)