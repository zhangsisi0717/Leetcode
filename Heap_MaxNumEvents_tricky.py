from collections import deque
from functools import total_ordering
from typing import List
import heapq
"""
only trick here is to decide which event to join at current day? so we attend whichever event ends first


step 1: sort the list by start date  (events = [[1, 1], [1, 4], [2, 2], [3, 4], [4, 4]])
step 2: create a min-heap based on ending date
    next_day = events[0][0]=1
 
    if heap is not empty:
        heap.pop(), num_events +=1
        pop out all the events in the heap whose end date > next_day
        
    push all the events whose start data = next_day into the heap
    next_day +=1
        

"""

@total_ordering
class Event:
    def __init__(self, times):
        self.start, self.end = times

    def __lt__(self, other):
        return self.end < other.end

    def __eq__(self, other):
        return self.end == other.end


def maxEvents(events: List[List[int]]) -> int:
    sorted_events = deque(sorted(events))
    heap = []
    num_event=[]
    next_day = sorted_events[0][0]
    while(sorted_events or heap):
        if heap:
            num_event.append(heapq.heappop(heap))
            while(heap and heap[0].end<next_day): ## pop out all the events whose end dates < next_day
                heapq.heappop(heap)

        while(sorted_events and sorted_events[0][0]==next_day): ##push all the events whose start date == next_day
            heapq.heappush(heap,Event(sorted_events.popleft()))

        next_day = next_day+1
    return len(num_event)
