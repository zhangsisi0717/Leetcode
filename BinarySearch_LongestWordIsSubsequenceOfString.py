from typing import List
from collections import deque
from bisect import bisect_right
import copy
from collections import deque
from bisect import bisect_right
import copy
#https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
find longest word in dictionary that is subsequence of s

step 1: create a hashmap (letter_to_index) for s, key: letter, value=[ordered index of this letter in s]
step 2: determine if a word in dictionary is a subsequence
        cur_idx = -1
        for each word, index from i=0 to end, find the smallest index of word[i] in s that is larger than cur_idx using BINARY SEARCH(bisect_right)
        if can not found => break
        if found => cur_idx = found_new_idx
if we could find all the increasing indexes of this word, then this word is a subsequence of string s, record its length update the result
"""
def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    s_to_idx = dict()
    for idx in range(len(s)):
        if s[idx] not in s_to_idx:
            s_to_idx[s[idx]] = deque([idx])
        else:
            s_to_idx[s[idx]].append(idx)

    result=[]
    max_len=0
    for word in dictionary:
        new_word_dic=s_to_idx
        cur_max_idx=-1
        for idx in range(len(word)+1):
            if idx == len(word):
                if max_len<len(word):
                    max_len = len(word)
                    result=[word]
                elif max_len == len(word):
                    result.append(word)

            else:
                if word[idx] not in new_word_dic or not new_word_dic[word[idx]] or cur_max_idx>=new_word_dic[word[idx]][-1]:
                    break
                elif cur_max_idx < new_word_dic[word[idx]][0]:
                    cur_max_idx = new_word_dic[word[idx]][0]

                else:
                    cur_max_idx = new_word_dic[word[idx]][bisect_right(new_word_dic[word[idx]],cur_max_idx)]

    return sorted(result)[0] if result else ""

