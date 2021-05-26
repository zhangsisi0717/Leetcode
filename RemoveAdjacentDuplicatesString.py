# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii
#
"""
##s = "pbbcggttciiippooaais", k = 2
Stack: stack = [[p,1]], iterate from idx = 0 to end,
if s[idx] == top element on the stack and stack[-1][1] + 1 == k:
    then stack.pop(),
elif s[idx] == top element on the stack and stack[-1][1] + 1 < k:
    then stack[-1][1] += 1
if stack is empy or s[idx] != top element on the stack:
    append [s[idx],1]

"""
from collections import deque
def removeDuplicatesStack(self, s: str, k: int) -> str:
    stack = deque([[s[0],1]])
    for i in range(1,len(s)):
        if s[i] == stack[-1][0] and stack[-1][1] + 1 == k:
            stack.pop()
        elif s[i] == stack[-1][0] and stack[-1][1] + 1 < k:
            stack[-1][1] +=1
        else:
            stack.append([s[i],1])

    result = ""
    for i in stack:
        result += i[0] * i[1]
    return result

s = "deeedbbcccbdaa"



def removeDuplicates(self, s: str, k: int) -> str:
    string = s
    change = True
    while(change):
        new_s = ""
        change = False
        prev = string[0]
        count = 1
        for i in range(1,len(string)):
            if string[i] == prev:
                count += 1
                if count == k:
                    count =0
                    change = True
                continue


            new_s += count*prev
            prev = string[i]
            count = 1

        new_s = new_s + count*prev
        string = new_s

    return new_s
