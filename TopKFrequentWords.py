##https://leetcode.com/problems/top-k-frequent-words/
from type_checking import *
from collections import Counter
import random
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

