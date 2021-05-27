from bisect import bisect_right
from collections import deque
from collections import defaultdict

##https://leetcode.com/problems/daily-temperatures/
from collections import deque
"""
temperatures = [73, 75, 71, 76, 73]
result = [0,0,0,0,0,0,0]
use a stack to solve this problem:
iterate from 0 to end,
stack = [(73,0)], then 75(next element) > top element in stack, then we result[index of top_element] = index of next element - index of top_element in stack, then we pop(), append
(next_element, index of next_element) to stack, so stack = [(75,1)], then nex element is 71, 71 less than 75, add directly to top of stack , stack = [(75,1),(71,2)], then
next element 76 is larger than top element in stack: 71, we keep pop out and update the result until pop out all the elements in the stack that is smaller than the new
element. So the temperatures in the stack is always in a descending order from bottom to top
"""
def dailyTemperatures(temperatures):
    stack = deque([])
    result = [0 for _ in range(len(temperatures))]
    for idx,temp in enumerate(temperatures):
        while(stack and temp>stack[-1][0]):
            result[stack[-1][1]] = idx-stack[-1][1]
            stack.pop()
        stack.append((temp,idx))
    return result


