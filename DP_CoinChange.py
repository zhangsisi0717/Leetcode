from functools import cache
#https://leetcode.com/problems/coin-change/
"""
purpose: smallest number to make up to certain amount
f(x) returns smallest number of coins to make up to amount "x"
   f(x) => min( 1+f(x-C0), 1+f(x-C1), 1+f(x-C2), .....1+f(x-C3))
"""
import math
def coinChange(coins: List[int], amount: int) -> int:
    @cache
    def minCoins(left):
        if left == 0:
            return 0
        if left < 0:
            return float("inf")

        minimal = float("inf")
        for i in coins:
            if i <= left:
                minimal= min(minCoins(left-i),minimal)
        return minimal+1

    re = minCoins(amount)

    return -1 if math.isinf(re) else re

