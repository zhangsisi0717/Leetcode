"""

Brute force solution + memoization

a = "catsandog" dict =  ["cat","cats","and","sand","dog"]

"""


#https://leetcode.com/problems/word-break-ii
from type_checking import *
import functools
def wordBreak2(s: str, wordDict: List[str]) -> bool:
    wordDict = set(wordDict)

    @functools.lru_cache(maxsize=None)
    def recursion(start):
        if start == len(s):
            return [""]
        re = []
        for end in range(start+1, len(s)+1):
            print(f"start = {start}, end = {end}")
            if s[start:end] in wordDict:
                sub_string = recursion(end)
                if sub_string:
                    new_sub_s = [s[start:end] + " "+i if i else s[start:end] for i in sub_string]
                    print(f"new_sub_s = {new_sub_s}")
                    re += new_sub_s
        print(f"re = {re}")
        return re
        # return False,None

    return recursion(0)

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

# s = "catsdog"
# wordDict = ["cats","and","sand","dog"]
wordBreak2(s, wordDict)


###https://leetcode.com/problems/word-break/

import functools
def wordBreak(s: str, wordDict: List[str]) -> bool:
    wordDict = set(wordDict)

    @functools.lru_cache(maxsize=None)
    def recursion(start):
        if start == len(s):
            return True
        for end in range(start+1, len(s)+1):
            if s[start:end] in wordDict and recursion(end):
                return True

        return False

    return recursion(0)

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
wordBreak(s, wordDict)



# from collections import defaultdict
#
# f = lambda: defaultdict(f)
