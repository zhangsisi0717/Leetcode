#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        unvisited = set()
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            unvisited.add(edge[0])
            unvisited.add(edge[1])

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor in unvisited:
                    unvisited.remove(neighbor)
                    dfs(neighbor)

        num = 0
        while(unvisited):
            cur = unvisited.pop()
            num +=1
            dfs(cur)

        return num + n - len(graph)

