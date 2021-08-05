from collections import defaultdict
from collections import deque
##https://leetcode.com/problems/longest-repeating-character-replacement/
"""
s="AABABBA"

step 1: keep track of the (start,end,length) of the repeating letters
'A': [[0, 1, 2], [3, 3, 1], [6, 6, 1]], 'B': [[2, 2, 1], [4, 5, 2]]

step 2: for each letter, use two queues, and keep track of how many k left, end_idx,
the first element in the queue_2 is always the start point, the first element in queue_1 is always the subarray of letters that need to be combined with subarray in queue_1
queue_1:'A': [[0, 1, 2], [3, 3, 1], [6, 6, 1]]
queue_2: []
if queue_two is empty, queue_2.append(queue_1.popleft)
if distance between first subarray in queue_1 and end_idx <= left, we just combine the
subarray in queue_1 and update the left_k, end_idx,cur_max

if not: means we don't and enough k to combine the 1st subarray in queue_1 and queue_2,
then end_idx += left_k, left_k=0

if left_k == 0, then we just cut the 1st subarray in queue_2, and make more left_k

until we pop out all elements in queue_1,
max_length = min (current_max + left_k, len(string))
"""
class Solution:
    def maxLength(self,s,k)->int:
        pre = None
        pre_idx = None
        letter_to_idx = defaultdict(list)
        for idx,e in enumerate(s):
            if (not pre and not pre_idx) or (pre and pre != e):
                pre = e
                pre_idx = idx
                letter_to_idx[e].append([idx,idx,1])

            elif pre and pre == e:
                letter_to_idx[pre][-1][1] += 1
                letter_to_idx[pre][-1][2] += 1

        global_max=0
        for key,val in letter_to_idx.items():
            queue = deque(val)
            queue_2 = deque([queue.popleft()])
            end,cur_max = queue_2[0][1],queue_2[0][2]
            left = k
            while(queue):
                if left == 0:
                    if len(queue_2)>=2:
                        intv = queue_2[1][0]-queue_2[0][1]-1
                        left += intv
                    queue_2.popleft()

                if not queue_2:
                    end = queue[0][1]
                    left = k
                    queue_2.append(queue.popleft())

                else:
                    interval = queue[0][0]-end-1
                    if queue[0][0]-end-1 <= left: ##interval <= left
                        end = queue[0][1]
                        left -= interval
                        queue_2.append(queue.popleft())
                    else: ##interval > left
                        end += left
                        left = 0

                cur_max = max(cur_max,end-queue_2[0][0]+1)

            cur_max = max(cur_max, min(end-queue_2[0][0]+1+left,len(s)))
            global_max = max(global_max,cur_max)
        return global_max

    def characterReplacement(self, s: str, k: int) -> int:
        return self.maxLength(s,k)