import typing
"""
use dictionary to implement the "Trie" data structure

https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/
"""

def buildTrie(words):
    trie = dict()
    for w in words:
        cur_dic = trie
        for e in w:
            if e not in cur_dic:
                cur_dic[e] = dict()

            cur_dic = cur_dic[e]

        cur_dic["end"] = dict()

    return trie
def isInTheTrie(trie,word):
    """
    without "." in the search word
    """
    for idx,e in enumerate(word):
        if e in trie:
            trie = trie[e]

        else:
            return False

    return True if "end" in trie else False


def search(wordDict,word: str) -> bool:
    """
    there "." in the search word e.g "a.p"
    Then we use dfs to search the word
    """
    def dfs(curDict, word, index):
        if index >= len(word):
            return True if "end" in curDict else False

        if word[index] == ".":
            for val in curDict.values():
                if dfs(val, word, index+1):
                    return True

        if word[index] !="." and word[index] in curDict:
            if dfs(curDict[word[index]], word, index+1):
                return True

        return False

    return dfs(wordDict, word, 0)


words = ["beautiful","apple","applepie","cat","cats","catslitter"]
trie = buildTrie(words)
