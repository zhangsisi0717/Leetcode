import copy
#https://leetcode.com/problems/is-graph-bipartite/
"""
since it is binary category, either set A or B for a node
no matter how you label it, as long as you meet conflicts, return False
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
unvisited = [0,1,2,3]
queue = []
use BFS to keep adding node to the queue, and label it, if cur_node = "0", then all of its neighbors 
shold be "1", if current neighbor already visited and label of current neighbor == label of cur_node,
return False (meet conflicts), 
If no conficts after visiting all nodes, then return True

"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        unvisited = {i for i in range(len(graph))}
        node_to_label = dict()
        queue = deque([])
        while(queue or unvisited):
            if not queue:
                queue.append(unvisited.pop())
                node_to_label[queue[0]] = 0
                continue
            cur_node = queue.popleft()
            for neighbor in graph[cur_node]:
                if neighbor in node_to_label and node_to_label[neighbor] == node_to_label[cur_node]:
                    return False

                if neighbor in unvisited:
                    unvisited.remove(neighbor)
                    queue.append(neighbor)
                    node_to_label[neighbor] = 1 - node_to_label[cur_node]

        return True
















