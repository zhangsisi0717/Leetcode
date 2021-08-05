from functools import cache
"""
dfs(idx) return mini_cost starting from "idx"
each idx, either choose day_1,day_7 or day_30,
it is like a three-way tree (triple tree)
O(time complex approximately) == number of nodes in the tree, 
deepest layer of this tree == len(days)
shallowest layer of this tree == always buy day_30 each time

time complexity == (3 ^ average layers)  - 1
"""
##https://leetcode.com/problems/minimum-cost-for-tickets/
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(idx):
            if idx == len(days)-1:
                return min(costs)
            if idx > len(days)-1:
                return 0

            day_1 = costs[0] + dfs(idx+1)     ##1-day pass
            day_7_idx = float("inf")
            day_30_idx = float("inf")
            for i in range(idx+1,len(days)):
                if days[i] >= days[idx]+7:
                    day_7_idx = i
                    break

            if day_7_idx < float("inf"):
                for j in range(day_7_idx,len(days)):
                    if days[j] >= days[idx]+30:
                        day_30_idx = j
                        break

            day_7 = costs[1] + dfs(day_7_idx)
            day_30 = costs[2] + dfs(day_30_idx)

            return min(day_1,day_7,day_30)

        return dfs(0)
