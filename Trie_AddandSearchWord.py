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
        def has(idx,cur_dict,word):
            if idx == len(word) and "end" in cur_dict: return True
            if idx == len(word)  and "end" not in cur_dict: return False
            for i in range(idx,len(word)):
                if word[i] != "." and word[i] in cur_dict:
                    cur_dict = cur_dict[word[i]]

                elif word[i]!= "." and word[i] not in cur_dict:
                    return False

                elif word[i] == ".":
                    for sub_dict in cur_dict.values():
                        if sub_dict != True and has(i+1,sub_dict,word):
                            return True
                    return False

                if i == len(word)-1 and "end" not in cur_dict:
                    return False
            return True

        return has(0,self.wordDict,word)
