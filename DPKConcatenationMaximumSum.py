class kConcatenationMaxSum:  # https://leetcode.com/problems/k-concatenation-maximum-sum/
    def kConcatenationMaxSum(self, arr, k):
        base = 10 ** 9 + 7
        curMax = 0
        globalMax = 0
        sumAllArr = sum(arr)
        if k >= 2:
            N = len(arr) * 2
        else:
            N = len(arr)
        realIdx = 0  # idx in real arr
        for idx in range(0, N):
            if realIdx >= len(arr):
                realIdx -= len(arr)
            if curMax <= 0:
                curMax = arr[realIdx]
            else:
                curMax += arr[realIdx]

            if idx == len(arr) and k > 2 and sumAllArr > 0:
                curMax += sumAllArr * (k - 2)

            if curMax > globalMax:
                globalMax = curMax

            realIdx += 1
        return globalMax % base

"""
Kadane's algorithms: keep track of current_Max_sum and global_Max_Sum, scan array from i=0 to (N-1), 
if current_Max_sum (ending at index i) = array[i]:
    current_Max_Sum<=0
else:
    current_Max_Sum += array[i]
if current_Max_Sum > global_Max_Sum:
    global_Max_Sum = current_Max_Sum
"""
