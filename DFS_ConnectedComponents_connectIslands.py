from typing import List
from collections import deque
def shortestBridge(grid: List[List[int]]) -> int:
    num_r,num_c = len(grid),len(grid[0])
    visited = [[False for _ in range(num_c)] for _ in range(num_r)]

    def dfs(r,c):
        visited[r][c] = True
        result = set([(r,c)])
        neighbors = [[r,c-1],[r,c+1],[r-1,c],[r+1,c]]
        for i,j in neighbors:
            if 0<=i<num_r and 0<=j<num_c and not visited[i][j] and grid[i][j]==1:
                result = result.union(dfs(i,j))

        return result

    re = []
    for i in range(num_r):
        for j in range(num_c):
            if not visited[i][j] and grid[i][j]==1:
                re.append(dfs(i,j))

    other = re[1]
    def findClosest(r,c):
        print(f"r,c = {r,c}")
        queue = deque([[r,c,0]])
        visited.add((r,c))
        while(queue):
            cur_r,cur_c,steps = queue.popleft()
            print(f"cur_r = {cur_r},cur_c={cur_c},steps={steps}")
            neighbors = [[cur_r,cur_c-1],[cur_r,cur_c+1],[cur_r-1,c],[cur_r+1,cur_c]]
            for i,j in neighbors:
                if (i,j) in visited:continue
                if not 0<=i<num_r or not 0<=j<num_c:
                    continue
                if (i,j) in other:
                    print(f"found r,c {r,c} is connected to other island {i,j}, steps = {steps}")
                    return steps
                if grid[i][j] == 0:
                    queue.append([i,j,steps+1])
                visited.add((i,j))
        return float("inf")

    min_step = float("inf")
    for r,c in re[0]:
        visited = set()
        min_step = min(findClosest(r,c),min_step)

    return min_step


grid = [[0,1,0],[0,0,0],[0,0,1]]
# grid=[[1,1,1,1,1],[1,0,0,0,1],[0,0,1,0,0],[1,0,0,0,1],[1,1,1,1,1]]
shortestBridge(grid)



