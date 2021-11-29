import math
"""
1. Pour Water:https://leetcode.com/problems/pour-water/

step 1: create two stacks for both "move right", "move left" , only push "first strictly decreasing block" into the stack (eg. if [4,3,3,2,2,2,1,1] then start from "4", we only push first 3, first 2 and first 1)

step 2: Then the position we need to fill water is on top of the stack(if left_stack is not empty, then fill left, else: fill right stack, if both empty, just fill water right on index "k")

step 3: once we found the position to fill water and height(stack[-1]) + 1, we need to update the left_stack and right_stack,

"""
def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
    n = len(heights)
    left_stack = []
    right_stack = []
    def update_left(idx):
        if idx == 0 or heights[idx - 1] > heights[idx]: # stop
            return
        # now idx > 0 and heights[idx - 1] <= heights[idx]:
        if heights[idx - 1] < heights[idx]:
            left_stack.append(idx - 1)
        update_left(idx - 1)
    def update_right(idx):
        if idx == n-1 or heights[idx + 1] > heights[idx]:
            return
        if heights[idx + 1] < heights[idx]:
            right_stack.append(idx + 1)
        update_right(idx + 1)

    update_left(k)
    update_right(k)
    for i in range(volume):
        if left_stack: # move to left
            idx = left_stack[-1]
            heights[idx] += 1
            if idx < n - 1 and heights[idx] == heights[idx + 1]:
                left_stack.pop()
            update_left(idx)
        elif right_stack: # move to right
            idx = right_stack[-1]
            heights[idx] += 1
            if idx > 0 and heights[idx] == heights[idx - 1]:
                right_stack.pop()
            update_right(idx)
        else:  # stay at k
            idx = k
            heights[idx] += 1
            update_left(idx)
            update_right(idx)

    return heights
"""
------------------------------------------------------
"""

