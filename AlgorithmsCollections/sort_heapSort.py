import random
import heapq
heapq.heapify(l)
heapq.heappop(l)
heapq.heappush(l, 7)
heapq.heapreplace(l,3)
"""
Time complexity: O(n*log(n))
parent = n
left_child = 2n + 1
right_child = 2n + 2
parent_nodes = [0,1,2,3....len(a)//2-1], so if there are 10 nodes in the binary-tree,then the parent would be 0,1,2,3,4
"""
"""
@:assume node.left and node.right are already the heap, and if node.left is the smallest, then exchange node and node.left, then heapify(node.left), recursively do that 
"""
def minHeapify(heap,node,heapSize): ###lg(n): n is number of layers from node to the bottom
    l = 2*node + 1
    r = 2*node + 2

    min = l if l <heapSize and heap[l]<heap[node] else node
    min = r if r<heapSize and heap[r]<heap[min] else min

    if min != node:
        heap[node],heap[min] = heap[min],heap[node]
        minHeapify(heap,min,heapSize)

def buildMinHeap(heap):
    n = len(heap)
    for idx in range(n//2-1,-1,-1):
        minHeapify(heap,idx,n)


def heapSort(heap):
    buildMinHeap(heap) ## O(nlgn)
    for idx in range(len(heap)-1,0,-1): ## O(nlgn)
        heap[idx],heap[0] = heap[0],heap[idx]  ##exchange last node with the root
        minHeapify(heap,0,idx)

    return heap[::-1]



















