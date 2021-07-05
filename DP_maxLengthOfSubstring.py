#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
from functools import cache
"""
pick any number of string from an array and concatanet it to make new string which only contains unique letter

maximumLength(idx,avai_letters) return maximum length we can get considering all the strings before index "idx" given 
avai_letters we can use

maximumLength(idx,avai_letters) = max( include string[idx] into final result, not include string[idx])

we need to first determine if we could include current string[idx] given avai_letters,
if not,  include string[idx] into final result = 0
else: we update avai_letters and include_idx_max = len(arr[idx]) + maximumLength(idx-1, updated_avail)

not_include_max = maximumLength(idx-1, old_avail)

max(include_idx_max, not_include_idx_max)
"""
def maxLength(arr: List[str]) -> int:
    letters = tuple(string.ascii_lowercase)

    @cache
    def maximumLength(idx,avai_letters):
        avail = set(i for i in avai_letters)
        if idx < 0:
            return 0

        couldInclude = True
        for e in arr[idx]:
            if e not in avail:  ##idx can not be included
                couldInclude = False

            else:
                avail.remove(e)

        include_idx=0
        if couldInclude:
            avail = list(avail)
            avail.sort()
            avail = tuple(avail)
            include_idx = len(arr[idx]) + maximumLength(idx-1, avail)

        not_include_idx = maximumLength(idx-1, avai_letters)
        return max(include_idx,not_include_idx)

    return maximumLength(len(arr)-1,letters)