from typing import List
"""
Permulation I: assume there is no duplicates in the list
"""
#https://leetcode.com/problems/permutations/
"""

brute force solution: use recursion to enumerate all the 
comlexity: O(N*N!)

"""
def permute(nums: List[int]) -> List[List[int]]:
    num_set = set(nums)
    def gen_permu(num_set):
        if len(num_set) == 0:
            return [[]]
        result = []
        for i in num_set:
            copy_set = num_set.copy()
            copy_set.remove(i)
            next_permu = gen_permu(copy_set)
            temp = [[i] + j for j in next_permu]
            result += temp

        return result

    return gen_permu(num_set)

nums = [1,2,3]
permute(nums)


"""
approach 2: starting from the smallest permutation, and keep find the next larger permutation until it is the largest one
"""
from typing import List
from bisect import bisect_right

def next_permutation(l: List[int]):

    n = len(l)
    i = n - 1
    while i > 0 and l[i] <= l[i-1]:
        i -= 1
    if i == 0:
        raise StopIteration

    # now l[i-1] < l[i]
    l[i:] = l[:i-1:-1]
    idx = bisect_right(l, l[i-1], lo=i)
    l[i-1], l[idx] = l[idx], l[i-1]

    return l

l = [0, 1, 2, 3]
while True:
    try:
        print(l)
        l = next_permutation(l)
    except StopIteration:
        break
