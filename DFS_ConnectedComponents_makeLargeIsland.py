#https://leetcode.com/problems/making-a-large-island/
from collections import  defaultdict
"""
explain: iterate througth all the blocks one by one, once found 0, then check all neighbors, if the neighbor is 1, then
do a dfs from the neighbor and found all the connected components, label this component, and keep track of the size of
the connected_components. for example: if (2,2)==0 and (2,3)==1 and (3,3)==1, then dfs(2,3),dfs(3,3), if (2,3) and (3,3)
belong to different components, then sum = size of (2,3)components  + size of (3,3) components + 1


Another approach, a little bit tedious is:
1. do dfs to find all the connected components and label it, keep track of two hashmaps, one is 
"x_y_to_id", another one is "id_to_size"

2. iterate through all the grid and once it is a "0", we check its neighbors, and if the neighbors belong to different 
    group, we add its size
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_to_id = dict()
        id_to_size = defaultdict(lambda :0)
        visited = set()
        def _dfs(x,y,id):
            if x<0 or x>=n or y<0 or y>=n:
                return
            if grid[x][y] ==0:
                return
            if (x,y) in visited:
                return
            xy_to_id[(x,y)] = id
            id_to_size[id] +=1
            visited.add((x,y))

            _dfs(x+1,y,id)
            _dfs(x-1,y,id)
            _dfs(x,y+1,id)
            _dfs(x,y-1,id)

        cur_max=0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    _dfs(x,y,len(id_to_size))

                else:
                    id_collection=set() ##keep track of all the unique ids that are connected to this "0"
                    for i,j in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
                        if i<0 or i>=n or j<0 or j>=n:
                            continue
                        if grid[i][j] ==0:
                            continue
                        if (i,j) not in xy_to_id:
                            _dfs(i,j,len(id_to_size))
                        id_collection.add(xy_to_id[(i,j)])
                    cur_max = max(cur_max, sum([id_to_size[index] for index in id_collection])+1)

        if id_to_size:
            return max(cur_max, max(id_to_size.values()))

        return cur_max
