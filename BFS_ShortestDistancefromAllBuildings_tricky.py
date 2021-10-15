#https://leetcode.com/problems/shortest-distance-from-all-buildings/

from collections import deque
from collections import defaultdict

"""
 1. for a certain building  B(r,c), use BFS to get all the shortestPath from building  B(r,c) to all empty block
 2. do step 1 for all the buildings and return the minimal result
"""
class Solution:
    def shortestDistance(grid: List[List[int]]) -> int:
        ##value[0]: cumulative sum from building i to this empty block
        ##value[1]: number of buildings that could reach out to this empty block
        land_to_distance = defaultdict(lambda:[0,0])
        n_r,n_c = len(grid),len(grid[0])
        def shortestDisToAllLands(row,col):
            queue = deque([[row,col,0]])
            visited = set()
            while(queue):
                cur_r,cur_c,step = queue.popleft();
                neighbors = [(cur_r+1,cur_c),(cur_r-1,cur_c),(cur_r,cur_c-1),(cur_r,cur_c+1)]
                for r,c in neighbors:
                    if 0<=r<n_r and 0<=c<n_c and grid[r][c] == 0 and (r,c) not in visited:
                        queue.append([r,c,step+1])
                        visited.add((r,c))
                        land_to_distance[(r,c)][0]+= (step+1)
                        land_to_distance[(r,c)][1] +=1


        num_b = 0
        for i in range(n_r):
            for j in range(n_c):
                if grid[i][j] == 1:
                    num_b +=1
                    shortestDisToAllLands(i,j)

        mini = float("inf")
        for val in land_to_distance.values():
            if val[1] == num_b:
                mini = min(mini,val[0])

        return mini if mini<float("inf") else -1



