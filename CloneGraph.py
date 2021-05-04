#https://leetcode.com/problems/clone-graph/submissions/
##DFScopy
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return node
    graph_dict = dict()

    def dfsCopy(node):
        graph_dict[node] = Node(node.val,None)
        for i in node.neighbors:
            if i not in graph_dict:
                dfsCopy(i)

            graph_dict[node].neighbors.append(graph_dict[i])

        return

    dfsCopy(node)
    return graph_dict[node]