##https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/
from typing import List
"""
use recursion to solve this problem
##[3,10,19,9,6]
def numOfMoves(prev,isIncrease,index) return number of moves needs to change given "prev number",
 "next number nums[index]", "if next step is increase or decrease"
 
    if (next step == increase and nums[index]> prev)  => return numOfMoves(nums[index],decrease, index+1)
    if (next step == decrease and nums[index]< prev)  => return numOfMoves(nums[index],increase, index+1)
    
    if (next step == increase and nums[index] <= prev)  => we need to decrease prev number to "nums[index]-1"
            so we  return (prev-nums[index]+1) + numOfMoves(nums[index],1-isIncrease,index+1)
            
    if (next step == decrease and nums[index] > prev)  => we need to decrease next number  nums[index] to "prev-1"
           so we return (nums[index]-prev+1) + numOfMoves(prev-1,1-isIncrease,index+1)
    
take [3,10,19,9,6] as an example

movesToMakeZigzag == min ( numOfMoves(3,"increase",1) , numOfMoves(3,"increase",1) )
"""
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        ##[3,10,19,9,6]
        def numOfMoves(prev,isIncrease,index): #return all possible moves
            if index > len(nums)-1:
                return 0

            if (isIncrease and nums[index] > prev) or (not isIncrease and nums[index] < prev):
                return numOfMoves(nums[index],1-isIncrease,index+1)

            elif isIncrease and nums[index] <= prev:
                return (prev-nums[index]+1) + numOfMoves(nums[index],1-isIncrease,index+1)

            elif not isIncrease and nums[index] >= prev:
                return (nums[index]-prev+1) + numOfMoves(prev-1,1-isIncrease,index+1)


        return min(numOfMoves(nums[0],1,1), numOfMoves(nums[0],0,1))










