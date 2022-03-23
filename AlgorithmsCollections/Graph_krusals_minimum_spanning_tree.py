##https://leetcode.com/problems/connecting-cities-with-minimum-cost/
import math
"""
##1. Kruskal's algorithm:
##Step1: sort all the edges in ascending order
##Step2: add next edge to tree unless two vertices are already connected
"""
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        if len(connections) < N-1:
            return -1
        connections.sort(key=lambda x:x[2], reverse=False)
        parent = [i for i in range(0,N+1)]
        cost = 0

        def union(v1,v2):
            root1 = findRoot(v1)
            root2 = findRoot(v2)
            parent[root1] = root2

        def connected(v1,v2):
            if findRoot(v1) == findRoot(v2):
                return True
            return False

        def findRoot(v): ###path_halving way
            cur = v
            while(parent[cur] != cur):
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            return cur

        for edge in connections:
            if connected(edge[0],edge[1]):continue
            union(edge[0],edge[1])
            cost += edge[2]
        return cost

