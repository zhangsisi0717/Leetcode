from type_checking import *
from collections import Counter
import random
import heapq
##https://leetcode.com/problems/top-k-frequent-words/


"""
approach 1: heap (nlogk) => if we want to get most frequent k words, we need to keep track of a "min_heap" with size k
"""
##https://leetcode.com/problems/top-k-frequent-elements/
def topKFrequent(nums, k):
    num_to_count = Counter(nums)
    num_list = [(j,i) for i,j in num_to_count.items()]
    min_heap = num_list[:k]
    heapq.heapify(min_heap)
    for idx in range(k,len(num_list)):
        if num_list[idx][0]>min_heap[0][0]:
            heapq.heapreplace(min_heap,num_list[idx])
    return [re[1] for re in min_heap]

"""
approach 2: quick sort(keep track of k smallest elements)
"""

def topKFrequent(words: List[str], k: int) -> List[str]:
    counter = Counter(words)
    unique = [i for i in counter.keys()]

    def quickSort(l,k):
        if k==0:
            return []
        if len(l) ==1 or not l:
            return l
        pivot = random.randint(0,len(l)-1)
        pre,sur=[],[]
        for i in range(len(l)):
            if i != pivot:
                if counter[l[i]]>counter[l[pivot]]:
                    pre.append(l[i])
                elif counter[l[i]] == counter[l[pivot]] and l[i] < l[pivot]:
                    pre.append(l[i])
                else:
                    sur.append(l[i])

        if len(pre)>=k:
            pre = quickSort(pre,k)
            return pre
        if len(pre) < k:
            pre = quickSort(pre,k)
            sur  = quickSort(sur,k-len(pre)-1)
            return pre + [l[pivot]] + sur

    return quickSort(unique,k)
a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
topKFrequent(a, 4)

