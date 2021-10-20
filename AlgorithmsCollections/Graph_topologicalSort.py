from collections import deque
"""
https://leetcode.com/problems/course-schedule-ii/
pesudo-code: https://en.wikipedia.org/wiki/Topological_sorting
"""
"""
approach 1: BFS
Kahn's algorithm

step 1: keep track of two dictionaries, one ancestors[e1] = [e2,e3,e4] (e2,e3,e4 points to e1), descendants[e5] = set([e1,e2,e3]) (e5 points to e1,e2,e3)
step 2: add all the nodes that do not have descendants into the queue
step 3: run bfs, trick here is, only if you have added all the descendants of cur_node, then you can add cur_node into the queue!! 
"""
def findOrder(numCourses: int, prerequisites) -> List[int]:
    ancestors= [[] for _ in range(numCourses)]
    descendants = [set() for _ in range(numCourses)]

    for course, prereq in prerequisites:  ##create ancestors and descendants dictionary
        ancestors[prereq].append(course)
        descendants[course].add(prereq)

    toProcess = deque()
    for course, descendant in enumerate(descendants):
        if not descendant:##add all the nodes that do not have descendants into the queue
            toProcess.append(course)

    outputOrder = []
    while toProcess:
        cur_course = toProcess.popleft()
        outputOrder.append(cur_course)
        for ances in ancestors[cur_course]: ##for all the ancestors of the cur_node
            descendants[ances].remove(cur_course) ##remove "cur_node" from the descendants list of the ancestor_node
            if not descendants[ances]: ## if all the descendents of the "ances" have been added to the queue
                toProcess.append(ances) ##then we add the "ances" to the queue


    return outputOrder if len(outputOrder) == numCourses else []

"""
approach 1: DFS
(visited(permanant), recursion_stack, cur_node)

step 1: start dfs from all the nodes that do not have ancestors 
step 2: need to detect if there is any cycle
"""
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    descendants = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        descendants[course].append(prereq)

    orderList = []
    def visit(visited, recursion_stack, cur_node):
        nonlocal orderList
        if visited[cur_node]:
            return True

        if cur_node in recursion_stack:
            return False

        recursion_stack.add(cur_node)  ###mark cur_node as a temporary mark

        for des in descendants[cur_node]:
            if not visit(visited, recursion_stack, des):
                return False

        recursion_stack.remove(cur_node)  ###remove temporary mark
        visited[cur_node] = True
        orderList.append(cur_node)
        return orderList

    visited = [False for _ in range(numCourses)]
    for idx in range(numCourses):
        if not visited[idx]:
            if not visit(visited, set(), idx):
                return []
    return orderList







