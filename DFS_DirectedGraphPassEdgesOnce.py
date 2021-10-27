##https://leetcode.com/problems/reconstruct-itinerary/
import copy
"""
Eulerian path
directed graph: 
A directed graph has an Eulerian trail if and only if at most one vertex has (out-degree) − (in-degree) = 1 (start point), 
at most one vertex has (in-degree) − (out-degree) = 1 (end point), every other vertex has equal in-degree and out-degree, 
if (out-degree)-(in-degree)==1, then it has to be start point
if (in-degree)-(out-degree)==1, then it has to be the end point

so in this case, 
step 1: we use sort the neighbors of each vertice in a lexical order
step 2: use dfs to pick a valid path in order, and output the result
(for each neighbor of current node, if current neighbor has no valid neighors (all its edges have been used) and left_edge > 0, then this path is a dead end), then 
we check next neighbor of this node

we need to note that there are replicate edges, so we need to create a dictionary left_edge => key: edge value: how many edges left
"""

from collections import defaultdict
def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    left_edge = defaultdict(lambda:0)
    for e in tickets:
        graph[e[0]].append(e[1])
        left_edge[(e[0],e[1])] +=1

    for key in graph.keys():
        graph[key] = sorted(graph[key])

    def dfs(v,left_edge):
        if len(left_edge) == 0:
            return [v]
        if v not in graph:
            return []
        for neighbor in graph[v]:
            if (v,neighbor) in left_edge:
                new_left_edge = copy.deepcopy(left_edge)
                new_left_edge[(v,neighbor)] -=1
                if new_left_edge[(v,neighbor)] ==0: new_left_edge.pop((v,neighbor))
                re = dfs(neighbor,new_left_edge)
                if re:
                    return [v] + re
        return []
    return dfs("JFK",left_edge)

tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
findItinerary(tickets)
