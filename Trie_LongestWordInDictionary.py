#https://leetcode.com/problems/longest-word-in-dictionary/
class Solution:
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

