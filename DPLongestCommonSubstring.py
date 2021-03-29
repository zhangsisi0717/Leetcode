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