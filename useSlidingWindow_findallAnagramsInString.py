##https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List
from collections import Counter
def findAnagrams(s: str, p: str) -> List[int]:
    ns, np = len(s), len(p)
    if ns < np:
        return []

    p_count = Counter(p)
    s_count = Counter()

    output = []
    # sliding window on the string s
    for i in range(ns):
        # add one more letter
        # on the right side of the window
        s_count[s[i]] += 1
        # remove one letter
        # from the left side of the window
        if i >= np:
            if s_count[s[i - np]] == 1:
                del s_count[s[i - np]]
            else:
                s_count[s[i - np]] -= 1
        # compare array in the sliding window
        # with the reference array
        if p_count == s_count:
            output.append(i - np + 1)

    return output


s= "cbaebabacd"
p = "abc"
findAnagrams(s, p)





