##https://leetcode.com/problems/the-maze/
from type_checking import *
def hasPath(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    visited = set()
    numRows = len(maze)
    numCols = len(maze[0])
    def dfs(s,d):
        print(f"current visit: {s}")
        visited.add(s)
        neighbors = findNeighbors(s[0],s[1],numRows,numCols,maze)
        print(f"current neighbors is : {neighbors}")
        if d in neighbors:
            return True
        for i in neighbors:
            if i not in visited and dfs(i,d):
                return True

        return False

    return dfs(tuple(start),tuple(destination))

def findNeighbors(r,c,numRows,numCols,maze):
    neighbors = set()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cur_r, cur_c = r, c
        while 0 <= cur_r+dr < numRows and 0 <= cur_c+dc < numCols and maze[cur_r+dr][cur_c+dc] != 1:
            cur_r += dr
            cur_c += dc
        if cur_c != c or cur_r != r:
            neighbors.add((cur_r, cur_c))
    return neighbors

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
hasPath(maze, start, destination)

# findNeighbors(0,4,5,5,maze)

