##https://leetcode.com/problems/coin-change-2/
"""
sum(amount,k) returns the number of unique combinations if only considering first "K" elements, with sum to amountx`x``

sum(amount,k) = summmation of (sum(amount - i*coins[k], k-1) , i from 0 to amount//coins[k]
"""
from typing import *
def change(amount, coins):
    def sum(amount,k):
        if k ==0:
            return 1 if amount % coins[0] == 0 else 0

        if amount <0:return 0
        if amount ==0: return 1

        total=0
        for i in range(0,amount//coins[k]+1):
            total += sum(amount-i*coins[k],k-1)

        return total

    return sum(amount,len(coins)-1)



amount = 500
coins=[1,2,5]
change(amount, coins)
