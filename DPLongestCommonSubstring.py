from typing import List
##https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""
find longest common substring: set i,j as suffix of nums2 and nums1
create a table to keep track of the longest common string ending at index i and j
 if num1[j] == num2[i] => then lcs[i][j] == lcs[i-1][j-1] + 1 else 0
"""
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    lcs_suffix = [[0 for i in range(len(nums1)+1)] for j in range(len(nums2)+1)]
    lcs = 0
    for i in range(1,len(nums2)+1): ##i => nums2 , j => nums1
        for j in range(1,len(nums1)+1):
            lcs_suffix[i][j] = lcs_suffix[i-1][j-1]+1 if nums2[i-1] == nums1[j-1] else 0
            if lcs_suffix[i][j] >lcs:
                lcs = lcs_suffix[i][j]

    return lcs

def lcsubstring(stringA, stringB): ###https://www.techiedelight.com/longest-common-substring-problem/
    table =[[0 for i in range(len(stringA)+1)]for j in range(len(stringB)+1)]
    curLongest=0
    longestSuffix=set()
    for i in range(1,len(stringB)+1):
        for j in range(1,len(stringA)+1):
            if stringB[i-1] == stringA[j-1]:
                table[i][j] = table[i-1][j-1] + 1
                if table[i][j]>curLongest:
                    curLongest = table[i][j]
                    longestSuffix = {i-1}
                elif table[i][j]==curLongest:
                    longestSuffix.add(i-1)
            else:
                table[i][j] = 0
    # print(longestSuffix)
    # print(table)
    re = [stringB[i+1-curLongest:i+1] for i in longestSuffix]
    return re

stringA="ABABC"
stringB = "BABCA"

a="ABAB"
b="BABA"
lcsubstring(stringA, stringB)
lcsubstring(a, b)

# def lcsubstringrecur(stringA, stringB):
#     longest=0
#     surffix={}
#     def lcsubstring2(StringA, StringB, idxA, idxB,longest=0,surffix={}):
#         if idxA<0 or idxB<0:
#             return 0,{}
#         if StringA[idxA] == StringB[idxB]:
#             num,subString = lcsubstring2(StringA, StringB, idxA-1, idxB-1)
#             return num+1, [i+StringA[idxA] for i in subString]
#
#         else:
#             num1,subString1 = lcsubstring2(StringA, StringB, idxA-1, idxB)
#             num1,subString1 = lcsubstring2(StringA, StringB, idxA-1, idxB)
#
#
#     return lcsubstring2(stringA, stringB, len(stringA)-1, len(stringB)-1)
#
# stringA="ABABC"
# stringB = "BABCA"
#
# lcsubstring(stringA, stringB)