##https://leetcode.com/problems/find-median-from-data-stream/
import heapq
"""
step 1: create max_heap and min_heap
step 2: always make sure the len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
step 3: if len(max_heap) == len(min_heap)=> median == (max_heap[0]  + min_heap[0])/2
        else:  median == max_heap[0]
        
Tricky part here is how to addNum to make sure the size of max_heap and min_heap is banlanced
Solution: 
always add the new number into max_heap first, and popout the largest number in max_heap to min_heap
after that, if len(max_heap) < len(min_heap), then pop out the smallest number in min_heap to push into max_heap

"""
class MedianFinder:

    def __init__(self):
        self.max_heap = [] ##max_heap
        self.min_heap = [] ##min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,num*(-1))
        heapq.heappush(self.min_heap,(-1)*heapq.heappop(self.max_heap))
        if len(self.max_heap)<len(self.min_heap):
            heapq.heappush(self.max_heap, (-1)*heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap)>len(self.min_heap):
            return self.max_heap[0] * (-1)

        else:
            return (self.max_heap[0] * (-1) + self.min_heap[0])/2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
