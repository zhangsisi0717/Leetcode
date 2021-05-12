"""
Greedy MST algorithm:

##1. Kruskal's algorithm:
##Step1: sort all the edges in ascending order
##Step2: add next edge to tree unless two vertices are already connected(need to use union-find)

Why greedy works?
A simple way to consider it is, use all the edges in the list, and then you cut this graph in half, A cut in a graph could partition its vertices into two sets,
and the smallest crossing edges must be in the minimal spanning tree (crossing edges connect a vertex in one set with a vertex in the other)

Property: Given any cut, the minimal weight crossing edge should be in the minimal spanning tree
Proof: if minmal crossing edge e not in the MST, then adding e to MST creates a cycle, some other edge f in the cycle must be
a crossing edge, then remove f and add e is also a spanning tree with smaller weight
"""

from type_checking import *

def minimumCost2(N: int, connections: List[List[int]]) -> int:
    if len(connections) < N-1:
        return -1
    connections.sort(key=lambda x:x[2], reverse=False)
    parent = [i for i in range(0,N+1)]
    cost = 0

    def union(v1,v2):
        root1 = findRoot(v1)
        root2 = findRoot(v2)
        parent[root1] = root2

    def connected(v1,v2):
        if findRoot(v1) == findRoot(v2):
            return True
        return False

    def findRoot(v): ###path_halving way
        cur = v
        while(parent[cur] != cur):
            parent[cur] = parent[parent[cur]]
            cur = parent[cur]
        return cur

    for edge in connections:
        if connected(edge[0],edge[1]):continue
        union(edge[0],edge[1])
        cost += edge[2]


def minimumCost(N: int, connections: List[List[int]]) -> int:
    """
    if sub_graph1 is label 1
       sub_graph2 is label 2
       in order to connect them, change all the labels in sub_graph2 to label 1

       find ifConnected : O(1)
       connect: O(N)
    """
    if len(connections) < N-1:
        return -1
    connections.sort(key=lambda x:x[2], reverse=False)
    vertice_label = [i for i in range(0,N+1)]
    label_to_vertice = {i:[i] for i in range(0,N+1)}
    cost = 0
    for edge in connections:
        if vertice_label[edge[0]] == vertice_label[edge[1]]:
            continue

        label_e_1 = vertice_label[edge[0]]
        label_e_2 = vertice_label[edge[1]]
        label_to_vertice[label_e_1] += label_to_vertice[label_e_2]
        for v in label_to_vertice[label_e_2]:
            vertice_label[v] = label_e_1

        label_to_vertice.pop(label_e_2)
        cost += edge[2]
    return cost
