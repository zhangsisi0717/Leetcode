from collections import defaultdict
from bisect import bisect_right
import copy
"""
step 1: record idx of each letter in string "s"
step 2: for each letter in each word , use "bisect_right" to find current index
"""


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hashmap = defaultdict(list)
        for idx in range(len(s)):
            hashmap[s[idx]].append(idx)

        count = 0
        for w in words:
            found = True
            cur_idx = -1
            for l in w:
                if (l not in hashmap) or (l in hashmap and cur_idx >= hashmap[l][-1]):
                    found = False
                    break

                elif l in hashmap:
                    idx = bisect_right(hashmap[l],cur_idx)
                    cur_idx = hashmap[l][idx]

            if found:
                count +=1

        return count





