##https://leetcode.com/problems/design-add-and-search-words-data-structure/
from collections import defaultdict
class WordDictionary:
    def __init__(self):
        f = lambda: defaultdict(f)
        self.wordDict = f()

    def addWord(self, word: str) -> None:
        cur_dict = self.wordDict
        for idx in range(len(word)):
            cur_dict = cur_dict[word[idx]]
            if idx == len(word)-1:
                cur_dict["end"] = True

    def search(self, word: str) -> bool:
        def has(w,cur_dict):
            if not w and "end" in cur_dict:return True
            if not w and "end" not in cur_dict:return False
            for i in range(len(w)):
                if w[i] != "." and w[i] in cur_dict:
                    cur_dict = cur_dict[w[i]]

                elif w[i]!= "." and w[i] not in cur_dict:
                    return False

                elif w[i] == ".":
                    for sub_dict in cur_dict.values():
                        if sub_dict != True and has(w[i+1:],sub_dict):
                            return True
                    return False

                if i == len(w)-1 and "end" not in cur_dict:
                    return False
            return True

        return has(word,self.wordDict)
