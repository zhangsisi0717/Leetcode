def lpSubstringBottomUp(string):
    """
    1.create a table with i==index of prefix == rows, j==surffix==cols, diagonal should all be 1 where i==j.
    2.Update table only i<j, should update diagonal, (0,1)(1,2),(2,3),(3,4), then (0,2)(1,3)..then (0,3)(1,4)..then(0,4).
    3.If i+1==j and string[i] == string[j], table[i][j]==2
    4.If string[i] == string[j] and table[i+1][j-1]>0, then table[i][j] = table[i+1][j-1]+2

    """

    """
    https://leetcode.com/problems/longest-palindromic-substring/solution/
    Another faster way is to enumerate all possible center(a,b) and expand the interval gradually such as (a-1,b+1),(a-2,
    b+2), once s[a] != s[b], just stop. This would be faster when the longest palindromic ==1
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        p, q = 0, 1
        longest = 1
        center = [(x, x) for x in range(n)] + [(x, x+1) for x in range(n-1)]
        for (a, b) in center:
            i, j = a, b
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i-1, j+1
            i, j = i+1, j-1
            if j - i + 1 > longest:
                longest = j - i + 1
                p, q = i, j+1
                
        return s[p:q]
    
    """
##https://leetcode.com/problems/longest-palindromic-substring/
    curLargest=0
    curPrefix=set()
    table =[[1 if i==j else 0 for i in range(len(string))]for j in range(len(string))]
    for nums in range(1,len(string)):
        i=0
        j=i+nums
        while(j<len(string)):
            if i+1==j and string[i]==string[j]:
                table[i][j] == 2
            if string[i] == string[j] and table[i+1][j-1]>0:
                table[i][j] = table[i+1][j-1] + 2
            if curLargest<table[i][j]:
                curLargest=table[i][j]
                curPrefix={i}
            elif curLargest == table[i][j]:
                curPrefix.add(i)
            i+=1
            j+=1
    return curLargest,[string[i:i+curLargest] for i in curPrefix]

# b="abcdefghiihgfedcbaqwqabcdedcbaturdhasjdhkashdkabcdefghiihgfedcbauiyuiaaaedcbaqwqabcdeaaa"
# a="abcdefggfeaerwer"
# c="abcba"
# lpSubstringBottomUp(b)




def lpSubstring(string): ##recursion version
    panlin=dict()
    def ifpanlin(string,i, j,panlin):
        if (i,j) in panlin.keys():
            return panlin[(i,j)]
        if i==j:
            return True
        if i+1 ==j and string[i] == string[j]:
            return True
        if string[i] == string[j] and  ifpanlin(string,i+1, j-1,panlin):
            return True

        return False
    cur_largest=0
    prefix={}
    for i in range(0,len(string)-1):
        for j in range(i+1,len(string)):
            if (i,j) not in panlin.keys():
                boolean = ifpanlin(string,i,j,panlin)
                panlin[(i,j)] = boolean
            else:
                boolean = panlin[(i,j)]

            if boolean and j-i+1>cur_largest:
                cur_largest = j-i+1
                prefix={i}
            elif boolean and j-i+1 == cur_largest:
                prefix.add(i)
    return cur_largest,prefix

# b="abcdefghiihgfedcbaqwqabcdedcbaturdhasjdhkashdkabcdefghiihgfedcbauiyui"
# a="abcdefggfeaerwer"
# lpSubstring(b)


