"""
https://www.techiedelight.com/shortest-common-supersequence-introduction-scs-length/
very similar to DPImplementDiffUtility
"""

def fillLCStable(a,b):

    table = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            # print(i,j)
            if a[i-1] == b[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
    return table


def lcs(a,b,table,i,j):

    if i>0 and j>0 and a[i-1] == b[j-1]:

        return [s + a[i-1] for s in lcs(a,b,table,i-1,j-1)]

    elif i>0 and (j==0 or table[i][j-1]<table[i-1][j]):
        return  [s+ a[i-1] for s in lcs(a,b,table,i-1,j)]

    elif j>0 and (i==0 or table[i][j-1]>table[i-1][j]):
        return [s+ b[j-1] for s in lcs(a,b,table,i,j-1)]

    elif j>0 and (i==0 or table[i][j-1]==table[i-1][j]):
        sub1 = [s+ a[i-1] for s in lcs(a,b,table,i-1,j)]
        sub2 = [s+ b[j-1] for s in lcs(a,b,table,i,j-1)]
        return sub1+sub2

    return [str()]




x="ABCBDAB"
y="BDCABA"

table=fillLCStable(x,y) ##fill the LCS table first
lcs(x,y,table,len(x),len(y)) ##
