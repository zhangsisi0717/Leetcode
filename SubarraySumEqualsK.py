from type_checking import *
def subarraySum(self, nums: List[int], k: int) -> int:
    """
    iterate from index 0 to end, and keep track of the cumulative sum and the frequency of each SumToIndex
    When we firstly met sumToIndex == k , total +=1, then keep iterating,
    if (Sum[0,1...i] - k) show up previously, then numTotal += valueFrequencydic[Sum[0,1...i] - k], and save current Sum[0,1...i] to dictionary

    """
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


