##https://leetcode.com/problems/minimize-max-distance-to-gas-station/
from functools import total_ordering
import heapq
"""
stations_positions = [1,2,3,4,5,6,7,8,9,10]
purpose: insert k stations at any postion in stations_positions, minimize the maximum distance between adjacent stations

"""
"""
approach one: Heap
step 1: create the intervals(interval_val, number_of_stations inserted), interval_val is always the original interval value,
 only need to record number of stations inserted,   make it a Max Heap
 
step 2: while(k>0): each time ,pop out the current_maximum_intervals,  and add a new stations inside this interval, to make
a new interval, with val = current_maximum_intervals.valv, number_of_stations = current_maximum_intervals.point + 1

time complexity: (K* lg n)  n== number of intervals
"""
from functools import total_ordering
import heapq
@total_ordering
class Interval():
    def __init__(self, val,p):
        self.val = val
        self.p = p

    def __eq__(self, other):
        return (self.val/(self.p+1) == other.val/(self.p+1))

    def __ne__(self, other):
        return not (self.val/(self.p+1) == other.val/(self.p+1))

    def __lt__(self, other):
        return self.val / (self.p+1) > other.val/(other.p+1)

def minmaxGasDist(stations: List[int], k: int) -> float:
    intervals = [Interval(stations[i+1]-stations[i],0) for i in range(len(stations)-1)]
    heapq.heapify(intervals)
    while(k>0):
        cur = heapq.heappop(intervals)
        newInterval = Interval(cur.val,(cur.p+1))
        heapq.heappush(intervals, newInterval)
        k -= 1


    final = heapq.heappop(intervals)
    return final.val / (final.p + 1)

"""
approach 2: Binary Search

we actually need to find the smallest distance(D) such that number of inserted stations <= k

Summation all the i  { ceil[(Interval i /D) -1] }  <= k 

timeComlexity lg(max_interval) * n

"""
import numpy as np
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        intervals = np.array([stations[i+1]-stations[i] for i in range(len(stations)-1)])
        lb,ub = 0,max(intervals)
        while(lb+10**(-6)<ub):
            mid = (lb+ub) / 2
            if np.sum(np.ceil(intervals/mid-1))<=k:
                ub = mid

            else:
                lb = mid

        return lb



