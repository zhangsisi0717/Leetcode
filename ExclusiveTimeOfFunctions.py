from type_checking import *
"""
["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
in the stack, if the top func current = 0, no matter the next is (start or end), we need to cumulate the time on function 0
then, we decide if we need to pop() or add the new one to the stack

"""


from collections import deque
def exclusiveTime(n,logs):
    stack = deque()
    ex_time = [0 for _ in range(n)]
    prev_time =0
    for idx in range(len(logs)):
        cur_func, action, cur_time = logs[idx].split(":")
        func = int(func)
        cur_time = int(cur_time)
        if action == "end":
            cur_time +=1
        if stack:
            prev_func = stack[-1]
            ex_time[prev_func] += cur_time - prev_time ##prev_time is the time for logs[idx-1]

        if action == "start":
            stack.append(cur_func)

        else:
            stack.pop()

        prev_time = cur_time




