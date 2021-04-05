from type_checking import *
import  copy
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordlength=dict()

    def addWord(self, word: str) -> None:
        if not self.wordlength.get(len(word)):
            cur_dict={}
            for idx in range(len(word)-1,-1,-1):
                if idx == len(word)-1:
                    cur_dict = {word[idx]:True}
                else:
                    cur_dict = {word[idx]:cur_dict}
            self.wordlength[len(word)]= cur_dict
        else:
            cur_dict=self.wordlength[len(word)]
            index=0
            while(index<len(word)):
                if index == len(word)-1 and not cur_dict.get(word[index]):
                    cur_dict[word[index]] = True

                elif not cur_dict.get(word[index]):
                    cur_dict[word[index]] = {}

                cur_dict = cur_dict[word[index]]
                index +=1

    def search(self, word: str) -> bool:
        if not self.wordlength.get(len(word)):
            return False

        index=0
        cur_dictList = [self.wordlength[len(word)]]
        while(index<len(word)):
            new_dictList=[]
            if word[index] != ".":
                found=False
                for dictionary in cur_dictList:
                    if dictionary.get(word[index]):
                        found= True
                        new_dictList.append(dictionary[word[index]])
                if found == False:
                    return False
                else:
                    cur_dictList = new_dictList
            else:
                cur_dictList = [values for dicts in cur_dictList for _, values in dicts.items()]


            index +=1

        return True



