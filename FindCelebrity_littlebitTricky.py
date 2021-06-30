#https://leetcode.com/problems/find-the-celebrity/
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from collections import deque

""""
gurantee number of calling knows(a,b) less than 3N

queue = [0,1,2,3,4...n]

cur_candi = queue[0]
if knows(queue[0],queue[1]) => if queue[0] knows queue[1], then queue[0] is not a celebrity, pop out queue[0]
if not knows(queue[0],queue[1]) =>if queue[0] does not know queue[1], then if queue[1] is not cele, pop out queue[1]

repeatly do this, until there is only one left in the queue
then check if this person knows others and if others know this person, then return the final result
"""
def findCelebrity(self, n: int) -> int:
    candi = deque([i for i in range(n)])
    while(len(candi)>=2):
        # print(candi)
        i= candi[0]
        if knows(i, candi[1]): #if i knows candi[1], then i is not cele
            candi.popleft()

        else:
            candi.remove(candi[1])

            # print(candi)
    for j in range(n):
        if j!=candi[0] and knows(candi[0], j):
            return -1

        if j!=candi[0] and not knows(j,candi[0]):
            return -1

    return candi[0]