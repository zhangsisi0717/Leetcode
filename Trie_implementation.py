from typing import List
class Trie:

    def __init__(self):
        self.trie = dict()


    def insert(self, word: str) -> None:
        cur = self.trie
        for idx in range(len(word)):
            if word[idx] not in cur:
                cur[word[idx]] = dict()

            cur = cur[word[idx]]
            if idx == len(word)-1:
                cur["end"] = word


    def search(self, word: str) -> bool:
        cur = self.trie
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]

        if "end" not in cur: return False
        return True



    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]

        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)