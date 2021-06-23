from typing import List
from collections import defaultdict
##https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""
pre,sur = 0,0
TRICK HERE: use a hashmap to keep updating the current maximum index of letter i
key: letter i, val: current maximum index of this letter
1. we iterate sur from 0 to the end and each time we update the hashmap
if current len(hashmap)<=k => continue
else: 
    we found the letter with minimum index in the hashmap, and we then set the current prefix to (min_index + 1)

update the current longest substring

complexity O(N)
"""
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    if not s or k == 0:
        return 0
    g_longgest = 1
    pre= 0
    s_to_idx = defaultdict()
    for i in range(len(s)):
        s_to_idx[s[i]] = i ##keep update the current largest index of letter s[i]
        if len(s_to_idx) > k:
            min_idx = min(s_to_idx.values())
            s_to_idx.pop(s[min_idx])
            pre = min_idx+1
        g_longgest = max(g_longgest,i-pre+1)

    return g_longgest
