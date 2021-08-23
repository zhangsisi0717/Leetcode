#https://leetcode.com/problems/the-kth-factor-of-n/submissions/
import heapq
"""
compexity: lg(n)*ln(k), from i = 1 to n
create a maximum heap(with length of at most k), then after iterations, heap[0] is the kth smallest factor
    if n%i ==0:
        if i not in factor_set, factor_set.add(i),  if len(heap)<k: heap.push(i) else: heapq.heapreplace(heap,i*(-1))
        if (n//i) not in factor_set, factor_set.add(i),  if len(heap)<k: heap.push(n//i), else:heapq.heapreplace(heap,i*(-1))

"""
import heapq
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fac_set = set()
        heap = []
        for i in range(1,n+1):
            if n % i == 0:
                if i in fac_set:
                    break
                if i not in fac_set:
                    fac_set.add(i)
                    if len(heap)<k:
                        heapq.heappush(heap,i*(-1))
                    elif len(heap)>=k and i*(-1) > heap[0]:
                        heapq.heapreplace(heap,i*(-1))

                if (n // i) not in fac_set:
                    fac_set.add(n//i)
                    if len(heap)<k:
                        heapq.heappush(heap,(n//i)*(-1))
                    elif len(heap)>=k and (n//i)*(-1) > heap[0]:
                        heapq.heapreplace(heap,(n//i)*(-1))
        return heap[0]*(-1) if len(heap)>=k else -1


