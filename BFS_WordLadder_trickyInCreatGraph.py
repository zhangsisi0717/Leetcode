#https://leetcode.com/problems/word-ladder/

from collections import defaultdict
from collections import deque
"""
a very naive way is to create a graph by pair-wisely compare if two words are neighbor,
however, this way time complexity == O(N2 * M), N is number of words, M is length of words

A Better way to create graph:
e.g. l = ["hot","dot","dog","lot","log","cog"]
for "hot", its neighbor are => [ "*ot", "h*t", ho*]
fot "dot", its neighbor are =>[ "*ot", "d*t", "do*"]
for "dog", its neighbor are => ["*og", "d*g", "do*"]
therefore, we only need to iterate the wordList once, and create a map where
key is a generic pattern of word, value is list of words that match that pattern, such as
key: "ot", value: ["hot", "dot"]

so for any word, such as "dog", it neighbors has pattern ["*og", "d*g", "do*"], 
so neigbors are Graph["*og"] + Graph["d*g"]  + Graph["do*"]

In this way, the time complexity == O(M2 * N), N is number of words, M is length of words
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        graph = self.createGraph(wordList)
        queue = deque([[beginWord,1]])
        visited = set()
        while(queue):
            cur_word, step = queue.popleft()
            visited.add(cur_word)
            for i in range(len(beginWord)):
                pattern = cur_word[:i] + "*" + cur_word[i+1:]
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        return step + 1
                    if neighbor not in visited:
                        queue.append([neighbor, step+1])
        return 0


    def createGraph(self, wordList):
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(wordList[0])):
                graph[word[:i] + "*" + word[i+1:]].append(word)


        return graph
