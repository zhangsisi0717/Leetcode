def lpSubstringBottomUp(string):
    """
    1.create a table with i==index of prefix == rows, j==surffix==cols, diagonal should all be 1 where i==j.
    2.Update table only i<j, should update diagonal, (0,1)(1,2),(2,3),(3,4), then (0,2)(1,3)..then (0,3)(1,4)..then(0,4).
    3.If i+1==j and string[i] == string[j], table[i][j]==2
    4.If string[i] == string[j] and table[i+1][j-1]>0, then table[i][j] = table[i+1][j-1]+2

    """
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


