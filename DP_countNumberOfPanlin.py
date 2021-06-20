##https://leetcode.com/problems/palindromic-substrings/
from typing import List
"""
count number of panlindrom in a string
i=pre
j=sur
if isPanlin[i-1][j+1] and s[i] == s[j] => then isPanlin[i][j] == True
elif i+1 == j and s[i] == s[j] => then isPanlin[i][j] == True
"""
def countSubstrings(s: str) -> int:
    isPanlin = [[1 if i==j else 0 for i in range(len(s))] for j in range(len(s))]
    total = len(s)
    for c in range(1,len(s)):
        pre = 0
        sur = c
        while(sur<len(s)):
            if pre + 1 == sur and s[pre] == s[sur]:
                isPanlin[pre][sur] = 1
                total +=1

            elif isPanlin[pre+1][sur-1] and s[pre] == s[sur]:
                isPanlin[pre][sur] = 1
                total +=1

            pre +=1
            sur +=1
    return total
