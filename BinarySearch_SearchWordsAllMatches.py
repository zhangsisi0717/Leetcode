#https://leetcode.com/problems/search-suggestions-system/
from typing import List
from bisect import bisect_left
"""
approach 1: Binary Search

wordList = ['apple','baggage', 'bags', 'banner', 'box', 'cloths']

search word = "bagg"
lb,ub = 0,len(wordList)

step 1: sort the list  {{ nlg(n) }}
step 2: start the prefix search from prefix = bagg[:i] (i from 1 to len(w)) 
step 3: prefix = bagg[:i], start left_binary_search(between lb and ub), once we found the first index matching the prefix, we start to 
        check the three words after it, then update the lb
        
time complexity
n == number of all words
m == length of the search words
 nlg(n) +  m * lg(n)
"""
def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    lb,ub = 0,len(products)
    result=[]
    for i in range(len(searchWord)):
        temp=[]
        prefix = searchWord[:i+1]
        index = bisect_left(products[lb:ub],prefix)
        for j in range(index,index+3):
            if products[j][:i+1] == prefix:
                products.append(temp)
        result.append(temp)
        lb = index

    return result

"""
Approach 2: Trie + DFS

"""
def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    wordTrie = dict()
    products.sort()
    for w in products: ##create trie
        cur_dic = wordTrie
        for idx in range(len(w)):
            if w[idx] not in cur_dic:
                cur_dic[w[idx]]
            cur_dic = cur_dic[w[idx]]
            if idx == len(w)-1:
                cur_dic["end"] = w

    def wordTrans(cur):
        result = []
        for key in cur.keys():
            if key == "end":
                result.append(cur["end"])
            else:
                result += wordTrans(cur[key])
        return result[:min(len(result),3)]

    final = []
    for i in range(len(searchWord)):
        no_match = False
        cur_dic = wordTrie
        for j in searchWord[:i+1]:
            if j not in cur_dic:
                final.append([])
                no_match = True
                break
            cur_dic = cur_dic[j]
        if no_match:
            continue
        final.append(wordTrans(cur_dic))

    return final



# def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
#     products.sort()
#     result = []
#     candi = products
#     for i in range(len(searchWord)):
#         temp = []
#         for j in candi:
#             if j[:i+1] == searchWord[:i+1]:
#                 temp.append(j)
#
#         candi = temp
#         result.append(temp[:min(len(temp),3)])


