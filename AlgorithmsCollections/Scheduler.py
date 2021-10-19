import typing
"""
1. https://leetcode.com/problems/course-schedule-iii/
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
x[0]:duration of the course 
x[1]: end day of this course[x1]
return: number of maximum course we can take 
"""


"""
2.https://leetcode.com/problems/maximum-profit-in-job-scheduling/
startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
give startTime, endTime, and profit of each task
return Maximum profit we can get (tasks should have overlap)

solution(DP):
step 1: sort the list by startTime
step 2: maxProfit(i): max profit we can get starting considering from index i
    maxProfit(i) = max( profit[i] + maxProfit(j) , maxProfit(i+1) )
                       (j is the smallest index after index i that is not overlapped with task i)

"""