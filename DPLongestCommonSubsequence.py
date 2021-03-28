
"""
https://www.techiedelight.com/longest-common-subsequence/
    if end with the same element:
        LCS(A[1,2..m],B[1,2,3...n]) = LCS(A[1,2,3...m-1],B[1,2,3...n-1]) + A[m]/B[n]

    if end with different element:
        LCS(A[1,2..m],B[1,2,3...n]) = longer one of (LCS(A[1,2,3...m-1],B[1,2,3...n]), LCS(A[1,2,3...m], B[1,2,3...n-1]))
"""
def LCS(StringA,StringB,idxA,idxB):
    if idxA==-1 or idxB ==-1:
        return 0,[None]

    if StringA[idxA] == StringB[idxB]:
        length,sub = LCS(StringA,StringB,idxA-1,idxB-1)
        if length:
            return length+1,[i+StringA[idxA] for i in sub]
        else:
            return 1,[StringA[idxA]]
    else:
        length1, sub1 = LCS(StringA,StringB,idxA-1,idxB)
        length2, sub2 = LCS(StringA,StringB,idxA,idxB-1)
        if length1>length2:
            return length1,sub1
        elif length1 == length2:
            return length1,sub1 + sub2
        else:
            return length2,sub2

StringA = "ABCBDAB"
StringB = "BDCABA"
LCS(StringA,StringB,len(StringA)-1,len(StringB)-1)