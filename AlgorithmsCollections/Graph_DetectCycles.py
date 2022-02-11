"""
Problem1:

Directed Graph, detected if there is a cycle
#https://leetcode.com/problems/course-schedule/

use dfs : keep track of cur_vertex, visited, recursion stack, if cur_vertex already in recursion_stack , then there is a cycle

"""

"""
Directed Graph, detected if there is a cycle
ifhascycle(cur_vertex, visited, recursion_stack): return if could detect a cycle starting dfs from "cur_vertex"
peudo-code as follows:
"""
numOfVertices = 10
graph = {i:[] for i in range(numOfVertices)}

def ifhascycle(cur_vertex, visited, recursion_stack):
    if cur_vertex not in recursion_stack and not visited[cur_vertex]:
        recursion_stack.add(cur_vertex)
    elif cur_vertex in recursion_stack:
        return True
    else:  # elif i already visited, then return False
        return False

    for neighbor in graph[cur_vertex]:
        if ifhascycle(neighbor, visited, recursion_stack):
            return True
    recursion_stack.remove(cur_vertex)  #####this step is important!!!!Has to remove the cur_vertex from recursion_stack
    visited[cur_vertex] = True
    return False

def graphHasCycle(graph):
    recursion_stack = set()
    visited = [False for _ in range(numOfVertices)]
    for idx in range(numOfVertices):
        if not visited[idx] and ifhascycle(idx, visited, recursion_stack):
            return False
    return True


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
        if visited[neighbor] and neighbor is not parent:
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