#https://leetcode.com/problems/furthest-building-you-can-reach/
import heapq
"""
min heap:
step 1: we use up all the ladders first and push the difference we've seen into the min-heap
step 2: after use up all the ladders, whenever we met new "difference"(idx+1>idx), we compare this diff with the min-heap[0](smallest diff we've seen).
        1. if min-heap[0] > cur_diff, that means we should've used up bricks when we met min-heap[0], so we exchange these two, heap.replace(),
        and we also need to {{bricks -= min-heap[0]}}, if we do not have enough bricks, we then return Index, 
        
        2. if min-heap[0] <= cur_diff, we bricks -= cur_diff, idx +=1 , if not enough bricks, return Index
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        useLadder = [] ##min heap
        heapq.heapify(useLadder)
        idx = 0
        while(idx<len(heights)-1):
            if heights[idx] < heights[idx+1]:
                diff = heights[idx+1] - heights[idx]
                if ladders >0:  ##if ladders are not used up
                    heapq.heappush(useLadder,diff)
                    ladders -=1

                else:
                    if not useLadder:
                        if bricks - diff <0:
                            return idx
                        bricks -= diff
                    else:
                        if useLadder[0]<diff and bricks - useLadder[0] < 0:
                            return idx
                        elif useLadder[0]<diff and bricks - useLadder[0] >= 0:
                            bricks -= useLadder[0]
                            heapq.heapreplace(useLadder,diff)
                        elif useLadder[0]>=diff and bricks - diff <0:
                            return idx
                        elif useLadder[0]>=diff and bricks - diff >=0:
                            bricks -= diff

            idx +=1

        return len(heights)-1
