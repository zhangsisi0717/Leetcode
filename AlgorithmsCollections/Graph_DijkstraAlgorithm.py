
"""
https://www.youtube.com/watch?v=pVfj6mxhdMw&t=542s
## Dijsktra shortest path algorithm
we can get shortest path from "A" to all the other nodes

this is a "Greedy alogrithm" each step, we choose the "node with the SMALLEST known distance" in order to find a global optimal solution

step 1:
    visit_node = set()
    unvisited_nodes = {A,B,C,D}
    shortest_distance_from_A_to = {A:0,B:inf,C:inf,D:inf}
    previous_node = {A:None,B:None,C:None,D:None}

step 2:
    visit the unvisited node with the SMALLEST known distance from the start node "A".
    so at first, we start to visit from node "A" since the initial distance from A to A is 0,
    unvisited.pop("A")
    visited.add("A")

step 3:
    for the current node "A", we then "examine"(not visit) its "UNVISITED NEIGHBORS", and update shortest_distance_from_A_to
    the "UNVISITED NEIGHBORS"
    distance_from_a_to_"unvisited_node" = min(distance_from_A[unvisited_node], distance_from_A[cur_node]+ edge(cur_node, its unvisited_neighbor))

step 4:
    repeat step 2 and step 3
"""

"""
Leetcode: https://leetcode.com/problems/the-maze-ii/

O(nlgn) => general dijkstra algorithm (using priority queue to optimize the time compelxity )
The algorithm consists of the following steps:

1. Assign a tentative distance value to every node: set it to zero for our startstart node and to infinity for all other nodes.

2. Set the startstart node as currentcurrent node. Mark it as visited.

3. For the currentcurrent node, consider all of its neighbors and calculate their tentative distances. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one to all the neighbors. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B (through A) will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, keep the current value.

4. When we are done considering all of the neighbors of the current node, mark the currentcurrent node as visited. A visited node will never be checked again.

5. If the destinationdestination node has been marked visited or if the smallest tentative distance among all the nodes left is infinity(indicating that the destinationdestination can't be reached), then stop. The algorithm has finished.

6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new currentcurrent node, and go back to step 3.
"""