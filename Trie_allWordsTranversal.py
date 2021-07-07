from typing import List
products = ["bags","baggage","banner","box","cloths"]
"""
create a the trie first
"""
wordTrie = dict()
products.sort()
for w in products: ##create trie
    cur_dic = wordTrie
    for idx in range(len(w)):
        if w[idx] not in cur_dic:
            cur_dic[w[idx]] = dict()
        cur_dic = cur_dic[w[idx]]
        if idx == len(w)-1:
            cur_dic["end"] = w

"""
after create the Trie, we try to traverse all the words using DFS starting from current_dict
"""
products = ["bags","baggage","banner","box","cloths"]
def wordTrans(cur):
    result = []
    print(cur)
    print(f"cur_dic keys = {[i for i in cur.keys()]}")
    for key in cur.keys():
        print(f"cur_key={key}")
        if key == "end":
            result.append(cur["end"])

        else:
            result += wordTrans(cur[key])

    return result

wordTrans(wordTrie)



