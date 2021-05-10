##https://leetcode.com/problems/asteroid-collision/submissions/
"""
explain: [-1,1,2,3]
use stack data structure to store the result
re = [-1], if re[-1] <0 or re[idx]>0 or re is empty, we should just add the new element directly
else: if re[-1]>0 and re[idx] <0:
    keep comparing the new planet with planets in the stack until planets in the stack <0 or abs(planet) > abs(new planet)
     or  abs(planet) == abs(new planet)

"""
from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        idx=1
        re = deque([asteroids[0]])
        while(idx<n):
            if not re or re[-1] <0 or asteroids[idx]>0:
                re.append(asteroids[idx])
                idx +=1
                continue

            elif re[-1]>0 and asteroids[idx] <0:
                if abs(re[-1]) < abs(asteroids[idx]):
                    add = True
                    while(re and re[-1]>0):
                        if abs(re[-1]) < abs(asteroids[idx]):
                            re.pop()
                        elif abs(re[-1]) > abs(asteroids[idx]):
                            add = False
                            break
                        else:
                            add = False
                            re.pop()
                            break

                    if add:
                        re.append(asteroids[idx])

                elif abs(re[-1]) == abs(asteroids[idx]):
                    re.pop()

            idx +=1

        return re

