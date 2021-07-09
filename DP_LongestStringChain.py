from functools import cache
from collections import List
"""
if want to find the longest string,
ba -> bac -> dbac -> edbac

we could do it reversely. starting from the longest string and
maxLength(w) return the max length of word chain staring from word "w"
then maxLength(w) == max(maxLength(w2) + 1)  w2 = w[:i] + w[i+1:] i from 0 to length(w)
    if w2 not in wordSet, then return maxLength(w2) return 0 directly
"""
def longestStrChain(words: List[str]) -> int:
    wordset = set(words)

    @cache
    def maxLength(w):
        if w not in wordset:
            return 0
        return max([maxLength(w[:i]+w[i+1:]) + 1 for i in range(len(w))])

    max_length=0
    for j in words:
        max_length = max(max_length, maxLength(j))
    return max_length