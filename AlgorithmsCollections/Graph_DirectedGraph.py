import typing
"""
Problem1: 

Directed Graph, detected if there is a cycle
#https://leetcode.com/problems/course-schedule/

use dfs : keep track of cur_vertex, visited, recursion stack, if cur_vertex already in recursion_stack , then there is a cycle
         
"""

"""
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