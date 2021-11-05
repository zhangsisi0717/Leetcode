from typing import List
class MinimalJumpsToHome: #https://leetcode.com/problems/minimum-jumps-to-reach-home/
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        from collections import deque
        queue = deque([(0,True,0)]) #queue[0]:curPosition;#queue[1]:ifcanmoveBack; queque[2]:steps
        history= {(0, True)}
        while queue:
            cur = queue.popleft()

            if cur[0] + a == x or (cur[1] and cur[0] - b == x):
                return cur[2]+1

            if cur[1] and cur[0] - b not in forbidden and cur[0] - b >= 0 and (cur[0]-b, False) not in history: #prev:F, nex:B
                history.add((cur[0]-b,False))
                queue.append((cur[0]-b, False, cur[2]+1))

            if cur[0] + a not in forbidden and cur[0]+a < 6000 and (cur[0]+a,True) not in history: #prev:F, next:F
                history.add((cur[0]+a,True))
                queue.append((cur[0]+a,True,cur[2]+1))

        return -1


