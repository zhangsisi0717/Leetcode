def memoization(func): ###https://www.techiedelight.com/implement-diff-utility/
    called = dict()
    def memoizedFunc(*args):
        if args not in called:
            called[args] = func(*args)
        return called[args]

    return memoizedFunc

def implementDiffUtility(stringA,stringB):

    @memoization
    def lcs(i,j):
        if i==-1 or j==-1:
            return 0,str()

        if stringA[i] == stringB[j]:
            num,sub = lcs(i-1,j-1)
            return num+1,sub+stringA[i]

        num1,re1 = lcs(i-1,j)
        num2,re2 = lcs(i,j-1)
        if num1 > num2:
            return num1,re1 + "-"+stringA[i]+ " "
        else:
            return num2,re2 + "+"+stringB[j]+ " "

    return lcs(len(stringA)-1,len(stringB)-1)


x = "XMJYAUZ"
y = "XMJAATZ"

implementDiffUtility(x,y)