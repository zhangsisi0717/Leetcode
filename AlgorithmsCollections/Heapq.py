import heapq

class Node:
    def __init__(self,val1,val2):
        self.val1 =val1
        self.val12 = val2


node1 = Node(1,-1)
node2 = Node(-2,3)
node3 = Node(0,2)

lists = [node1,node2,node3]
setattr(Node, "__lt__", lambda self, other: self.val1+self.val12 <= other.val1+other.val2)
for l in lists:
    if l:
        heapq.heappush(pq,  l)

heapq.heapify(l)
print(heapq.heappop(l))




