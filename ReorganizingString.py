#https://leetcode.com/problems/reorganize-string/
from collections import Counter
from collections import deque
"""
insert the 
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        count = Counter(S)
        count_s = deque(sorted([[j,i] for i,j in count.items()]))
        re = deque([])
        while(len(count_s)>1):
            cur_idx = 0
            while(cur_idx<len(count_s)):
                re.appendleft(count_s[cur_idx][1])
                count_s[cur_idx][0] -= 1
                if count_s[cur_idx][0] == 0:
                    count_s.popleft()
                    cur_idx=0
                else: cur_idx +=1

        if len(count_s)==0:return "".join(re)
        left,temp_s = count_s[0][0],count_s[0][1]
        idx = 0
        while(idx<len(re) and left>0):
            if idx!=len(re)-1 and re[idx] != temp_s and re[idx+1] != temp_s:
                re.insert(idx+1,temp_s)
                left -=1
                idx+=2
            elif idx==len(re)-1 and re[idx] != temp_s:
                re.insert(idx+1,temp_s)
                idx += 2
                left -=1
            else: idx +=1

        return "".join(re) if left==0 else ""
