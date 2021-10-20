import typing
"""
Problem1: 

Undirected Graph, detected if there is a cycle

use dfs, keep track of "visited vertices" and "parent of cur_vertice", For every visited vertex v, 
when we have found any adjacent vertex u, such that u is already visited, 
and u is not the parent of vertex v. Then one cycle is detected.
         
"""
numOfVertices = 6
# graph = {0:[1,2],1:[0,5],2:[0,3,4],3:[2,4,6],4:[2],5:[1,6],6:[3,5]}
graph = {0:[1,2],1:[0,5],2:[0,3,4],3:[2,4],4:[2,3],5:[1]}
def hasCycle(parent, cur_vertice,visited):
    visited[cur_vertice] = True
    for neighbor in graph[cur_vertice]:
        if visited[neighbor] and neighbor != parent:
            return True

        elif not visited[neighbor] and hasCycle(cur_vertice, neighbor,visited):
            return True
    return False

hasCycle(None, 0,set())

def graphHasCycle(graph):
    visited = [False for _ in range(numOfVertices)]
    for cur_node in range(numOfVertices):
        if not visited[cur_node] and hasCycle(None, cur_node,visited):
            return False
    return True