from typing import List
import copy
#https://leetcode.com/problems/beautiful-arrangement/
"""
fill the list one by one
fillList(idx) would fill the list starting from index "idx"
global variable used = [False for _ in range(n+1)]  to keep track of all the numbers that have been used
then for i in range(1 to n):
    if i has not beed used and current (idx % i ==0 or i%idx==0):
        then we fill this position idx using i
        used[i] = True
        fillList(idx+1) => recursively fill the list starting from idx+1
        used[i] = False  => after the recursion, we need to reset used[i] to False
        ##if we have filled out all the positions, then count +=1##

"""
def countArrangement(n: int) -> int:
    counter = 0
    used = [False for _ in range(n+1)] ##if number i has been used
    def fillList(idx):
        if idx > n: ##if we have filled out all the positions, then count +=1
            nonlocal counter
            counter +=1
        for i in range(1,n+1):
            if not used[i] and (i%idx == 0 or idx%i ==0):
                used[i]=True
                fillList(idx+1)
                used[i] = False
    fillList(1)
    return counter





















