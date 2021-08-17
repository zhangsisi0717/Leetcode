import copy
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
    
step 4:
    repeat step 2 and step 3
"""
