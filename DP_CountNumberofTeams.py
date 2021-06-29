from typing import List
"""
in order to count valid increasing or decreasing triplet
core idea it to keep track of number of numbers that are smaller/larger than current element
for i in range(1,end):
    for j in range(0,i):
        if num[j]<num[i]:
            result += number of values that are smaller than num[j] (if we include both num[j],num[i] in this triplet)
            
        if nums[j]>nums[i]:
            result += number of values that are larger than num[j] (if we include both num[j],num[i] in this triplet)
"""
def numTeams(rating: List[int]) -> int:
    l = len(rating)
    lg,sm,res = [0]*l,[0]*l,0
    for i in range(1,l):
        for j in range(i):
            if rating[i]<rating[j]:
                lg[i] += 1
                res += lg[j]
            else:
                sm[i] += 1
                res += sm[j]
    return res

ratings = [72, 66, 17, 80, 50, 16, 98, 84]
numTeams(ratings)

