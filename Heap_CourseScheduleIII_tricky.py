#https://leetcode.com/problems/course-schedule-iii/
import heapq
from typing import List
"""
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
step 1: sort course lists by last day x[1]
step 2: create a max heap (by during), and keep track of current day 
step 3: for c in sorted_course, 
    if current_day + duration of c <= last day of c:
            then push "c" directly into the heap
    else:
            max_duration in heap = heap[0].duration
            if this max_duration < c.duration, then continue, we ignore c 
            else:
                heap.pop()  {pop out max duration and add it to 
                heap.push(c)
                current_day = current_day - max_duration + c.duration
        {{because we want to make sure the cur_day as small as possible if we add a new c}}

"""
def scheduleCourse(courses: List[List[int]]) -> int:
    courses=sorted(courses,key=lambda x:(x[1],x[0]))
    heap = []
    heapq.heapify([])
    # print(courses)
    cur_day = 0
    for c in courses:
        # print(stack)
        if not heap and c[0]<=c[1]:
            heapq.heappush(heap,[(-1)*c[0],c[1]])
            cur_day += c[0]
        elif heap:
            if c[0] + cur_day > c[1] and abs(heap[0][0]) > c[0]:
                duration = abs(heap[0][0])
                heapq.heapreplace(heap,[(-1)*c[0],c[1]])
                cur_day = cur_day - duration + c[0]

            elif c[0] + cur_day <= c[1]:
                heapq.heappush(heap,[(-1)*c[0],c[1]])
                cur_day += c[0]

    return len(heap)
