"""
A larger words can only be concatenated by smaller words,
start from the short words to long words, if this word can be concatenated in current wordSet, then add it to current set,
otherwise continue.
(use recursion to check if current word can be concatenated by current wordSet)
"""


from type_checking import *
import functools
def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    # sort the list by (length, item)
    words.sort(key = lambda x:len(x))

    @functools.lru_cache(maxsize=None)
    def concateRecursion(start,s,wordSet):
        wordSet = set(wordSet)
        if not wordSet:
            return False
        if start == len(s):
            return True
        for end in range(start+1, len(s)+1):
            if s[start:end] in wordSet and concateRecursion(end,s,tuple(wordSet)):
                return True

        return False

    re = []
    wordSet = []
    for idx in range(len(words)):
        # wordSet = tuple(words[idx+1:])
        s = words[idx]
        if concateRecursion(0,s,tuple(wordSet)):
            re.append(words[idx])
        else:
            wordSet.append(words[idx])

    return re


words=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
findAllConcatenatedWordsInADict(words)