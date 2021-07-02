#https://leetcode.com/problems/add-bold-tag-in-string/
from typing import List
from collections import defaultdict
from collections import deque
def addBoldTag(s: str, words: List[str]) -> str:
    f = lambda: defaultdict(f)
    wordTrie = f()
    for w in words: ##create trie
        cur_dic = wordTrie
        for idx in range(len(w)):
            cur_dic[w[idx]]
            cur_dic = cur_dic[w[idx]]
            if idx == len(w)-1:
                cur_dic["end"]

    idx_interval=deque([])
    for i in range(len(s)):
        cur_dic = wordTrie
        for j in range(i,len(s)):
            if s[j] not in cur_dic:
                break
            if s[j] in cur_dic:
                cur_dic = cur_dic[s[j]]

            if "end" in cur_dic:
                if idx_interval and idx_interval[-1][1]+1 >= i: ##need to merge
                    pre,sur = idx_interval.pop()
                    idx_interval.append([min(pre,i),max(sur,j)])

                else:
                    idx_interval.append([i,j])

    result = ""
    pre,sur = {e[0] for e in idx_interval},{e[1] for e in idx_interval}
    for idx in range(len(s)):
        if idx in pre:
            result +="<b>"
        result += s[idx]
        if idx in sur:
            result +="</b>"
    return result

words=["abc","bcd","abd","123"]
s = "abcdef123"
addBoldTag(s, words)














