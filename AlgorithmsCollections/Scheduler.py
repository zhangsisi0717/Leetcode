from typing import *
"""
1. https://leetcode.com/problems/course-schedule-iii/
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
x[0]:duration of the course 
x[1]: end day of this course[x1]
return: number of maximum course we can take 
"""


"""
2.https://leetcode.com/problems/maximum-profit-in-job-scheduling/
startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
give startTime, endTime, and profit of each task
return Maximum profit we can get (tasks should have overlap)

solution(DP):
step 1: sort the list by startTime
step 2: maxProfit(i): max profit we can get starting considering from index i
    maxProfit(i) = max( profit[i] + maxProfit(j) , maxProfit(i+1) )
                       (j is the smallest index after index i that is not overlapped with task i)

"""

"""
3.https://leetcode.com/problems/course-schedule/
Given a list of prerequisites of courses, determine if a student can finish all the courses
solution: directed graph, if there is a cycle, then can not finish all the courses 
dfs : keep track of "cur_vertex", "visited", "recursion stack", if cur_vertex already in recursion_stack , then there is a cycle
"""

"""
Given a list of prerequisites of courses, output all the courses in correct order
4. https://leetcode.com/problems/course-schedule-ii/
pesudo-code: https://en.wikipedia.org/wiki/Topological_sorting
solution: topological sort(BFS, DFS)

BFS: topological sort (Kahn's algorithm: BFS) 
step 1: put all the courses that do not have any required courses into the queue, visited.add()
step 2: do the BFS(Note: only if all the prerequisite courses have been added to outputResult, 
        then we can add this course to output).
        
DFS:
approach 1: DFS
(visited(permanant), recursion_stack, cur_node)

step 1: start dfs from all the nodes that do not have ancestors
step 2: need to detect if there is any cycle

PESUDO-CODE(DFS):
    L ← Empty list that will contain the sorted nodes
    while exists nodes without a permanent mark do
        select an unmarked node n
        visit(n)
    
    function visit(node n)
        if n has a permanent mark then
            return
        if n has a temporary mark then
            stop   (not a DAG)
    
        mark n with a temporary mark
    
        for each node m with an edge from n to m do
            visit(m)
    
        remove temporary mark from n
        mark n with a permanent mark
        add n to head of L
"""
