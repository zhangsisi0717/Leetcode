##https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
from collections import deque
"""
nums = [1,5,0,10,14]
for an unsortedd array, change at most k of the values into any values, and make (largest_val - minimal_val) minimal

step 1: sorted the array 
step 2: for a sorted array, each move we have two choice, 
        
        1.either make the smallest become anyvalue between(second_min,max), popleft the smallest value in array

        2. make the largest become smaller, somewhere between (min, second_max) , popout the larget value in array
minDiff(leftstep) return mindifference we can get given number of leftstep


"""
def minDifference(nums: List[int]) -> int:
    num_queue = deque(sorted(nums))

    def minDiff(leftstep):
        if leftstep == 0 or num_queue[-1]-num_queue[0] == 0:
            return num_queue[-1]-num_queue[0]

        mini = num_queue[0]
        num_queue.popleft()
        pop_min_steps = minDiff(leftstep-1)

        num_queue.appendleft(mini)
        maximum = num_queue[-1]
        num_queue.pop()
        pop_max_steps = minDiff(leftstep-1)

        num_queue.append(maximum)
        return min(pop_min_steps,pop_max_steps)

    return minDiff(3)
