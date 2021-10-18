##https://leetcode.com/problems/design-add-and-search-words-data-structure/
class WordDictionary:
    def __init__(self):
        self.wordDict = dict()


    def addWord(self, word: str) -> None:
        cur = self.wordDict
        for e in word:
            if e not in cur:
                cur[e] = dict()
            cur = cur[e]

        cur["end"] = dict()


    def search(self, word: str) -> bool:
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

        return dfs(self.wordDict, word, 0)













# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
