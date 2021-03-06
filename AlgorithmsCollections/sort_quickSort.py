import random
"""
Average Time complexity: O(n*log(n))
Best Time complexity: O(n*log(n))
Worst Case: n2 (each time you picked the smallest or the largest element)
"""

def quickSort(array):
    if len(array)==1 or not array:
        return array
    pivot = array[random.randint(0,len(array)-1)]
    l,r = [],[]
    for i in array:
        if i<=pivot:
            l.append(i)
        else:
            r.append(i)
    l = quickSort(l)
    r = quickSort(r)
    return l+r

"""
time complexity: complicated, has sysmetric structure where f(k) == f(n-k), and argmax => k==n//2
"""
def kthSmallestQuickSelect(k,array):
    pivot = array[random.randint(0,len(array)-1)]
    l,r = [],[]
    for i in array:
        if i<=pivot:
            l.append(i)
        else:
            r.append(i)
    if len(l) == k:
        return pivot

    elif len(l)< k:
        return kthSmallestQuickSelect(k-len(l),r)

    else:
        return kthSmallestQuickSelect(k,l)









