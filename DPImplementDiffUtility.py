def implementDiffUtility(a,b):
    """
    this is similar to finding common largest sequence:
    Step1: filled out the largest common subsequence table first
    Step2: Run recursion to get the implementDiffUtilit string
        if a[i-1] == b[j-1] -> return lcs(a,b,table,i-1,j-1)+a[i-1] + " "
        elif table[i-1][j] > table[i][j-1] -> means a[i-1] not in the common subsequence and we need to - a[i-1]
        elif table[i-1][j] <= table[i][j-1]  -> means b[j-1] not in the commonsub, then we need to + b[j-1]

    need to pay extra attention when (i== 0 and j>0)->added "+b[j]" and (i>0 and j==0) ->delete a[j],
    """

    def fillLCStable(a,b):

        table = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
        for i in range(1,len(a)+1):
            for j in range(1,len(b)+1):
                print(i,j)
                if a[i-1] == b[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j],table[i][j-1])
        return table

    def lcs(a,b,table,i,j):

        if i>0 and j>0 and a[i-1] == b[j-1]:

            return lcs(a,b,table,i-1,j-1)+a[i-1] + " "

        elif i>0 and (j==0 or table[i][j-1]<table[i-1][j]):
            return lcs(a,b,table,i-1,j) + "-" + a[i-1]+ " "

        elif j>0 and (i==0 or table[i][j-1]>=table[i-1][j]):
            return lcs(a,b,table,i,j-1) + "+" + b[j-1] + " "

        return str()

    table = fillLCStable(a,b)
    return lcs(a,b,table,len(a),len(b))



a="ACB"
b="BC"
lcs(a,b,table,len(a),len(b))





# x = "XMJYAUZ"
# y = "XMJAATZ"
#
# a="ABCBDAB"
# b="BDCABAE"

a="AB"
b="BC"

implementDiffUtility(x,y)

implementDiffUtility(a,b)

implementDiffUtility(d,e)


