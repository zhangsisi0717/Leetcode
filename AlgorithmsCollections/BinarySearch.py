from bisect import bisect_left
from collections import deque
a = deque([2.5, 3, 6, 77, 334, 777])
bisect_left(a,2.6)
a.insert(1,2.6)


from bisect import bisect_right
a = [[10,20]]
bisect_right(a,[20,30])


l = [1,2,2,2,3,4,5,6]
"""
bisectRight is just the regular binary search
"""
def bisectRight(lb,ub,num,l):
    while(lb<ub):
        print(f"lb={lb},ub={ub}")
        mid = int((lb + ub)/2)
        print(f"mid={mid}")
        if l[mid]>num:
            ub = mid-1
        else:
            lb = mid +1
    return lb if l[lb] == num else -1
"""
Recursive binary Search
"""
def recursiveBS(lb,ub,num,l):
    if lb == ub and l[lb] == num:
        return lb
    if lb == ub and l[lb] != num:
        return -1

    mid = (lb + ub) //2
    if num <=l[mid]:
        ub = mid
    else:
        lb = mid + 1

    return recursiveBS(lb,ub,num,l)

"""
bisect_left
"""
def bisectLeft(lb,ub,num,l):
    while(lb<ub):
        mid = int((lb + ub)/2)
        if l[mid]>num:
            ub = mid-1
        elif l[mid]==num:
            """
            only difference here
            """
            ub = mid
        else:
            lb = mid +1
    return lb if l[lb] == num else -1


bisectLeft(0,len(l)-1,2,l)

"""
!!Search in Rotated Sorted Array ##https://leetcode.com/problems/search-in-rotated-sorted-array/


"""