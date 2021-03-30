"""
Variation of longestCommonSubsequence, that is to find the longestCommonSubsequence of itself, but i!=j

if i==-1 or j==-1: return 0
elif x[i]==x[j] and i!=j return f(i-1,j-1)+1
else: return max( f(i,j-1),f(i-1,j)

"""

def lrs(string):
    visited=dict()
    def longestCommonSubsequence(string,idxA,idxB,visited):
        if(idxA,idxB) in visited:
            return visited[(idxA,idxB)]
        if idxA==-1 or idxB==-1:
            return (0,{str()})

        if string[idxA] == string[idxB] and idxA!=idxB:
            re = longestCommonSubsequence(string,idxA-1,idxB-1,visited)
            visited[(idxA,idxB)] = (re[0]+1,{i+string[idxA] for i in re[1]})
            return visited[(idxA,idxB)]

        re1 = longestCommonSubsequence(string,idxA-1,idxB,visited)
        re2 = longestCommonSubsequence(string,idxA,idxB-1,visited)
        if re1[0]>re2[0]:
            visited[(idxA,idxB)] = re1
        elif re1[0]==re2[0] and re1[1] != re2[1]:
            visited[(idxA,idxB)] = (re1[0],re1[1].union(re2[1]))
        else:
            visited[(idxA,idxB)] = re2

        return visited[(idxA,idxB)]

    return longestCommonSubsequence(string,len(string)-1,len(string)-1,visited)

a="ATACTCGGA"
b="ATACTCGBGBA"
c="BEBCEFCDFGDG"
d = "EBECFFDGGBCD"
e="BCDEFGEFGBCD"
# b="ATABCETFBCEIGFGIA"
lrs(a)
lrs(c)
lrs(d)
lrs(e)


