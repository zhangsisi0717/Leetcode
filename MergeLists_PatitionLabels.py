#https://leetcode.com/problems/partition-labels/
from collections import defaultdict
from collections import deque
"""
purpose: partition a string into as many parts as possible so that no letter shows up in multiple parts
s = "ababcbacadefegdehijhklij"
step1: keep track of the index of all the letters, and save the lb_idx and ub_idx of this letter
step2: sort all the intervals by lb_idx
step3: merge overlapped interval 
step4: return the result
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_to_idx =  defaultdict(list)
        for idx,c in enumerate(s):
            s_to_idx[c].append(idx)

        idx_lists = sorted([[i[0],i[-1]] for i in s_to_idx.values()])
        print(idx_lists)
        stack = deque([idx_lists[0]])
        for idx in range(1,len(idx_lists)):
            if stack[-1][1]>idx_lists[idx][0]:
                lb,ub = stack.pop()
                stack.append([lb,max(ub,idx_lists[idx][1])])

            else:
                stack.append(idx_lists[idx])

        return [right-left+1 for left,right in stack]