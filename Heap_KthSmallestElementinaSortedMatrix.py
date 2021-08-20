import heapq
"""
step 1: use first element in all rows to create a min-heap
step 2: each time, pop out the smallest value, cur = min-heap.pop() and insert the next larger value of "cur", until we 
        find the kth smallest value
"""

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    heap = [[matrix[r][0],r,0] for r in range(len(matrix[0]))]
    heapq.heapify(heap)
    re = None
    while(k>0):
        cur,cur_r,cur_c = heap[0]
        re = cur
        if cur_c+1 < len(matrix):
            cur_c +=1
            heapq.heapreplace(heap,[matrix[cur_r][cur_c],cur_r,cur_c])
        else:
            heapq.heappop(heap)
        k-=1
    return re