from functools import cache
"""
step 1: sort the list by startTime
step 2: maxProfit(i): max profit we can get starting considering from index i
    maxProfit(i) = max( profit[i] + maxProfit(j) , maxProfit(i+1) )
                       (j is the smallest index after index i that is not overlapped with task i)
timeComplexity O(n2)                 
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        tasks = [[startTime[i],endTime[i],profit[i]] for i in range(len(profit))]
        tasks = sorted(tasks)

        @cache
        def maxProfit(index):
            if index==len(profit)-1:
                return tasks[index][2]

            if index >=len(profit):
                return 0

            include, not_include = tasks[index][2],0
            if tasks[index+1][0] < tasks[index][1]: #there is overlap
                for i in range(index+2, len(profit)): ##this step is O(n)
                    if tasks[i][0] >= tasks[index][1]: # no overlap
                        include += maxProfit(i)
                        break
            else:
                include += maxProfit(index+1)
            not_include = maxProfit(index+1)
            return max(include, not_include)

        return maxProfit(0)