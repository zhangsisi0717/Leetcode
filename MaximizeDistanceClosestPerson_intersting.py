##https://leetcode.com/problems/maximize-distance-to-closest-person/
"""
only keep track of the seats that are occupied,
 seats = [1,0,0,0,1,0,1]
prev = None,
iterate seats one by one,
if seat ==1 and prev == None, then no person one the left, re = max(re, cur_seat_idx), prev = idx

if seat == 1 prev is not None, then there there is one person on the left, just seat in the middle of this two person, re = max(re, (idx-prev)//2), prev=idx

after iterating all seats, if seats[-1] == 0, means there is no person on the right,
 re = max(re, len(seats)-1-prev)
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        re = 0
        prev = None
        for idx,s in enumerate(seats):
            if s == 1 and prev is None: #no person on the left
                re = max(re,idx)
                prev = idx

            elif s == 1 and prev != None: ##there is person on the left
                re = max(re, (idx-prev)//2)
                prev = idx

        if seats[-1] == 0 and prev is not None:
            re = max(re,len(seats)-1-prev)


        return re






