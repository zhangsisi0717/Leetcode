#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    """
    iterate from index 0 to end, and keep track of the cumulative sum and the frequency of each SumToIndex
    When we firstly met sumToIndex == k , total +=1, then keep iterating,
    if (current_sum - k) show up previously at index i, which means, sum([i+1,current_sum_idx]) == k, so numTotal += valueFrequencydic[current_sum - k], and save current {{current_sum - k}} to dictionary

    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        curSum = 0
        valueFrequency = dict()
        for i in nums:
            curSum += i
            if curSum ==k:
                total +=1
            if curSum-k in valueFrequency:
                total += valueFrequency[curSum-k]

            if curSum in valueFrequency:
                valueFrequency[curSum] +=1

            else:
                valueFrequency[curSum] =1
        return total






