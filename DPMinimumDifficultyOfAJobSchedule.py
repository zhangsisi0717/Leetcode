"""
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
explaination:
 dp(idx, days_left) == min( dp(j+1,days_left -1 ) j->(idx to n - days_left + 1) ) + maximum difficulty between index(i,j) if finish job i->j
 in one single day.

 dp(idx, days_left = [finish job from i to j in a day] + mini( dp(j+1, end) )

 so we iterate j to determine how many jobs do we need to do this day besides job i in order to get minimal difficulty
"""
def minDifficulty(jobDifficulty,d): ##https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
    n = len(jobDifficulty)

    if n < d:
        return -1

    large_number = float('inf')
    diff = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        diff[i][i] = jobDifficulty[i]
        for j in range(i+1,n):
            diff[i][j] = max(diff[i][j-1], jobDifficulty[j])

    memo = {}
    def dp(idx, days_left):
        if n - idx < days_left:
            return large_number

        if days_left == 1:
            return diff[idx][n-1]

        if (idx, days_left) not in memo:
            memo[(idx, days_left)] = min(dp(j + 1, days_left - 1) + diff[idx][j] for j in range(idx, n - days_left + 1))

        return memo[(idx, days_left)]

    return dp(0,d)


jobDifficulty = [13,22,4,16,5]
d = 3
minDifficulty(jobDifficulty,d)