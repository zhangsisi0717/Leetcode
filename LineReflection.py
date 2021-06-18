#https://leetcode.com/problems/line-reflection/
from typing import List
"""
(x1,y1), (x2,y2),(x3,y3)....(Xn,Yn)
if there is such a line parallel to y-axis that reflect the given points symmetrically
then the x-center == sum(x1+x2+x3...Xn)/n
then iterate all the points and check if its corresponding symmetrical point exist in the original point set
  (x1,y1) corresponding symmetrical point(x2,y2)  =>  X2 = 2*x-center - x1 (beacause x-center = (x1+x2)/2)
                                         y-coordinate =>  y

if (x1,y1) and (x2,y2) are center symmetric, then x-center = (x1+x2)/2, y-center = (y1+y2)/2                              
"""
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        point_set = set(tuple(i) for i in points)
        x_center = sum(x for (x, y) in point_set) / len(point_set)
        for x, y in point_set:
            if (int(2*x_center - x), y) not in point_set:
                return False
        else:
            return True
