##https://leetcode.com/problems/concatenated-words/submissions/
from typing import List
"""
example: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
1. sort list by length and items [catdog,cat, dog] -> [cat, dog, catdog]

['cat','dog','rat','cats','dogcatsdog','catsdogcats','ratcatdogcat','hippopotamuses']
2. for word in list, firstly check if current word is is_concatenated_word, if is, then continue, if not, then added this
    word to pre-fix tree.
    
How to check if it is a concatenated word? "catsdogcats"
    root->d -> O -> g(ends_here)
     |
     c
     |
     a
     |
     t(ends_here)
     |
     s(ends_here)  
dsf ->  def is_concatenated_word(w, idx) -> return: if w[idx:] if a concatenated word
search from tree root:
if w[idx] is not a children of tree root  ->return false
if idx  == len(w), means already iterate all the letters in w, then -> return True
if w[idx] is a children of the tree root, then current_node become this child

for "catsdogcats", iterate c->a->t(ends_here), t(ends_here), however subword = sdogcats is not a concatenated word, so keep going,
c->a->t->s(ends_here),  s ends_here and subword = "dogcats" is a concatenated word, so "catsdogcats" is a concatenated word.

"""


class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = dict()
        self.ends_here = False

    def add(self, word: str):
        cur_node = self
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode(c)
            cur_node = cur_node.children[c]
        cur_node.ends_here = True

def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    # sort the list by (length, item)
    words.sort(key=lambda item: (len(item), item))

    trie_root = TrieNode(None)

    def is_concatenated_word(w, idx):
        """
        Is w[idx:] a concatenated word?
        :param w: word
        :param idx: index
        :return: True/False
        """
        if idx == len(w):
            return True

        if w[idx] not in trie_root.children:
            return False

        # below we ensure cur_node.value == w[idx]
        cur_node = trie_root.children[w[idx]]
        while True:
            if cur_node.ends_here and is_concatenated_word(w, idx+1):
                return True

            idx += 1
            if idx >= len(w) or w[idx] not in cur_node.children:
                return False

            cur_node = cur_node.children[w[idx]]

    results = []
    for w  in words:
        if not w:
            continue
        if is_concatenated_word(w, 0):
            results.append(w)
        else:
            trie_root.add(w)

    return results

print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
