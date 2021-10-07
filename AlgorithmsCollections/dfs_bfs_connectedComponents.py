import typing
"""
question 1:  find the shortest bridge to connect two connected-components
##https://leetcode.com/problems/shortest-bridge/

"""

def shortestBridge(self, grid: List[List[int]]):
    n_r = len(grid)
    n_c = len()
    label = [[-1 for _ in range(len)]]
    visited = [[..]..]

    to_island_1 = [..]
    to_island_2 = [..]


    def dfsLabel(r,c,label):
        visited[r][c] = True
        label[r][c] = label
        neighbors = [(),(),(),()]
        for n_r,n_c in neighbors:
            if gridn_r,n_c==1:
                dfsLabel(r,c,label)

    label = 1
    for i in n_r:
        for j in n_c:
            if grid[i][j] == 1 and not visited;
                dfsLabel(r,c,label)
                label +=1








