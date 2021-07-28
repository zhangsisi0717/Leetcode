"""
two pointer: prefix=i, surffix=j and keep track of number of zeros between i and j (length of i,j == number of ones in the list), and return minimal number of zeros, because we're actually filling ones into the zero postions
"""
#https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_to_pos = defaultdict(set)
        for idx in range(len(data)):
            num_to_pos[data[idx]].add(idx)
            numOnes = len(num_to_pos[1])

        numZero = [None for _ in range(len(data)-numOnes + 1)]
        count = 0
        for idx in range(numOnes):
            if data[idx] == 0:
                count +=1
        numZero[0] = count

        min_swaps = float("inf")
        for idx in range(0,len(data)-numOnes + 1):
            if idx>0:
                numZero[idx] = numZero[idx-1] - (1-data[idx-1]) + (1-data[idx+numOnes-1])

            min_swaps = min(min_swaps,numZero[idx])
        return min_swaps



