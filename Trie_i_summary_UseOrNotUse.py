from functools import lru_cache
"""
Example 0: exmaple that we'd better use the "TRIE":

https://leetcode.com/problems/longest-word-in-dictionary/
words = ["a","banana","app","appl","ap","apply","apple"], find longest word in words that can e built one character at 
a time by other words in words.

def longestWord(self, words: List[str]) -> str:
    trie = dict()
    for w in words: ##build trie
        cur = trie
        for idx in range(len(w)):
            if w[idx] not in cur:
                cur[w[idx]] = dict()
            cur = cur[w[idx]]
            if idx == len(w)-1:
                cur["end"] = True
                
    l_word = ""
    for w in words:
        cur = trie
        valid = True
        for idx in range(len(w)):
            if w[idx] in cur and "end" in cur[w[idx]]:
                cur = cur[w[idx]]
            else:
                valid = False
                break
        if valid:
            l_word = w if (not l_word) or (len(w)>len(l_word)) or (len(w)==len(l_word) and w<l_word) else l_word
    
    return l_word
"""

"""
example 1: exmaple that we'd better use the "TRIE":
##https://leetcode.com/problems/word-search-ii/submissions/

given board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] and words = ["oath","pea","eat","rain"]
output all the words in words that can be constructed from board

if we simply do dfs for each word in words on board, we could do a lot repetitive words if the word in words are more like:
["aaaaaaaaaa","aaaaaaaaab","aaaaaaaaac"]
so we'd better create a trie based on the words provided
"""


"""
examples that looks like trie, but in fact, do not use Trie
"""


"""
example 1: Word Break: wordDict = ["leet","code"] , s = "leetcode" if s can be concatenated by words in wordDict
https://leetcode.com/problems/word-break/

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)
    
    @cache
    def ifValid(start):
        if start >= len(s):
            return True
        
        for j in range(start, len(s)):
            if s[start:j+1] in wordSet and ifValid(j+1):
                return True
        
        return False
    
    return ifValid(0)

"""



"""
example 2: Concatenated Words
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"] ,return
concatenated words: which is a word that can be concatenated by words in the list that are shorter than the word
https://leetcode.com/problems/concatenated-words/
"""



"""
https://leetcode.com/problems/search-suggestions-system/
example 3:
Search Suggestions System:
input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
output: 
[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]

from bisect import bisect_left
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    products = sorted(products)
    result = []
    for i in range(1,len(searchWord)+1):
        temp=[]
        index = bisect_left(products,searchWord[:i])
        for j in range(index, min(len(products),index+3)):
            if products[j][:i] == searchWord[:i]:
                temp.append(products[j])
        result.append(temp)
        
    return result        
"""