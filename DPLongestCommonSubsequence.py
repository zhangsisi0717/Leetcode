
"""
https://www.techiedelight.com/longest-common-subsequence/
    if end with the same element:
        LCS(A[1,2..m],B[1,2,3...n]) = LCS(A[1,2,3...m-1],B[1,2,3...n-1]) + A[m]/B[n]

    if end with different element:
        LCS(A[1,2..m],B[1,2,3...n]) = longer one of (LCS(A[1,2,3...m-1],B[1,2,3...n]), LCS(A[1,2,3...m], B[1,2,3...n-1]))
"""
def longestCommonSubsequence(stringA,stringB):
    visited = dict()
    def LCS2(stringA,stringB,idxA,idxB,visited): ####recursion
        if(idxA,idxB) in visited:
            return visited[(idxA,idxB)]
        if idxA==-1 or idxB ==-1:
            return 0,[None]

        if stringA[idxA] == stringB[idxB]:
            re = LCS2(stringA,stringB,idxA-1,idxB-1,visited)
            if re[0]:
                visited[(idxA,idxB)] =(re[0]+1,[i+stringA[idxA] for i in re[1]])
            else:
                visited[(idxA,idxB)] = (1,[stringA[idxA]])
            return visited[(idxA,idxB)]

        re1 = LCS2(stringA,stringB,idxA-1,idxB,visited)
        re2 = LCS2(stringA,stringB,idxA,idxB-1,visited)
        if re1[0]>re2[0]:
            visited[(idxA,idxB)] = re1

        elif re1[0]==re2[0] and re1[1]!= re2[1]:
            visited[(idxA,idxB)] = (re1[0],re1[1]+re2[1])

        else:
            visited[(idxA,idxB)] =  re2
        return visited[(idxA,idxB)]
    return LCS2(stringA,stringB,len(stringA)-1,len(stringB)-1,visited)

testS1 = "BECFDG"
testS2 = "BCDEFG"
longestCommonSubsequence(testS1,testS2)


def LCSBottomUp(stringA,stringB):
    table=[[0 for i in range(len(stringA)+1)]for j in range(len(stringB)+1)]
    largest=0
    for i in range(1,len(stringB)+1):
        for j in range(1,len(stringA)+1):
            if stringB[i-1] == stringA[j-1]:
                table[i][j] = table[i-1][j-1]+1
                if table[i][j] > largest:
                    largest = table[i][j]
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])

    def readsubsequence(table, stringA, stringB, col, row):
        if col ==0 or row ==0:
            return [str()]

        if stringA[col - 1] == stringB[row - 1]:
            re =  readsubsequence(table, stringA, stringB, col - 1, row - 1)
            return [i + stringA[col - 1] for i in re]
        if table[row][col-1]> table[row-1][col]:
            return readsubsequence(table, stringA, stringB, col - 1, row)
        elif table[row][col-1]< table[row-1][col]:
            return readsubsequence(table, stringA, stringB, col, row - 1)
        else:
            return readsubsequence(table, stringA, stringB, col - 1, row) + readsubsequence(table, stringA, stringB, col, row - 1)

    return largest,readsubsequence(table,stringA,stringB,len(stringA),len(stringB))



stringA = "ABCBDAB"
stringB = "BDCABA"

X = "MZJAWXU"
Y = "XMJYAUZ"
LCSBottomUp(stringA,stringB)



