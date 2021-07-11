import math
import numpy as np
from functools import cache
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = 0
        largest = 0

        piles = np.array(piles, dtype=np.float)

        for p in piles:
            total += p
            if largest < p:
                largest = p

        lb,ub = 1, min(largest, math.ceil(largest / max(math.floor(h / len(piles)) - 1, 1)))
        while lb < ub:
            mid = math.floor((ub + lb) / 2)
            if np.sum(np.ceil(piles/mid))<=h:
                ub = mid

            else:
                lb = mid + 1

        return lb