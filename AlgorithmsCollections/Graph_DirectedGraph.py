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

"""
problem 2: output all the courses in a correct order
topological sort (BFS)
https://leetcode.com/problems/course-schedule-ii/submissions/

"""
"""
topological sort (Kahn's algorithm: BFS) 
step 1: put all the courses that do not have any required courses into the queue, visited.add()
step 2: do the BFS(Note: only if all the prerequisite courses have been added to outputResult, 
        then we can add this course to output).
"""
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    requires = [[] for _ in range(numCourses)] ##key: prerequisite
    requiredBy = [set() for _ in range(numCourses)] ##key: courses that have prerequisite
    for course, prereq in prerequisites:
        requires[prereq].append(course)  #[2,3] must take 3 before taking 2  require[3] = [2]
        requiredBy[course].add(prereq)   #requiredBy[2] = [3]

    toProcess = deque()
    for course, prereqs in enumerate(requiredBy):
        if not prereqs:
            toProcess.append(course)

    outputOrder = []
    while toProcess:
        prereq = toProcess.popleft()
        outputOrder.append(prereq)
        for course in requires[prereq]:
            requiredBy[course].remove(prereq)
            if not requiredBy[course]:
                """
                only if all the prerequisite courses have been added to outputOrder, then we can add this course to process
                """
                toProcess.append(course)

    return outputOrder if len(outputOrder) == numCourses else []

"""
topological sort (DFS) 
"""
