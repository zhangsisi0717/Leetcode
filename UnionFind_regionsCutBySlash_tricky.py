from typing import List
"""
explaination:
step 1: for each block grid[r][c], we create four nodes [edge west, edge north, edge east, edge south]
step 2: 
for r in range(n):
    for j in range(n):
    
        if meet "\\", union (west,south edge),  union (north,east edge)
        if meet "/" , union (west,north edge),  union (south,east edge)
        if meet " ", union(west, north, east, south)
        
        if not in first row, union(south edge from last row, north edge)
        if not in first col, union(east edge from last col, west edge)
"""
class Node:
    count = 0
    def __init__(self): ##dir: 0:E, 1:S, 2:W, 3:N
        Node.count += 1
        self.parent = self

    def findRoot(self):
        cur_node = self
        while(cur_node != cur_node.parent):
            cur_node = cur_node.parent
        return cur_node

    def join(self, other):
        self_r = self.findRoot()
        other_r = other.findRoot()
        if self_r != other_r:
            Node.count -= 1
            other_r.parent = self_r

class Solution:
    def regionsBySlashes(self, grid):
        Node.count = 0
        n = len(grid)
        edges = [[[Node() for _ in range(4)] for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == "\\":
                    edges[r][c][0].join(edges[r][c][3])
                    edges[r][c][1].join(edges[r][c][2])

                elif grid[r][c] == "/":
                    edges[r][c][0].join(edges[r][c][1])
                    edges[r][c][2].join(edges[r][c][3])

                else:
                    edges[r][c][0].join(edges[r][c][1])
                    edges[r][c][1].join(edges[r][c][2])
                    edges[r][c][2].join(edges[r][c][3])

                if c>0:
                    edges[r][c-1][2].join(edges[r][c][0])

                if r>0:
                    edges[r-1][c][3].join(edges[r][c][1])
        return Node.count

