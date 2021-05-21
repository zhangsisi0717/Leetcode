#https://leetcode.com/problems/3sum/
"""
[-1,0,1,2,-1,-4] without sorting
result = set()
for i to (0,end):
    seen = set()
    for j to (i+1,end):
        complement = -value_i-value_j
        if you have seen complement in the seen:
            add tuple(sorted([val_i,val_j,complement])) to set, sort could avoid duplicates

        if not seen:
            seen.add(val_j)

"""

def threeSum(nums):
    res= set()
    for i, val1 in enumerate(nums):
        seen = set()
        for j, val2 in enumerate(nums[i+1:]):
            complement = -val1 - val2
            if complement in seen:
                res.add(tuple(sorted((val1, val2, complement))))
            seen.add(val2)
    return res

