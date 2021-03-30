 ##https://www.techiedelight.com/longest-palindromic-subsequence-using-dynamic-programming/
##keep track of two indexes, prefix, and suffix, prefix starting from 0, suffix starting from len(string)-1,
###if string[prefix] == string[suffix], then lps(string, prefix, suffix) == lps(string, prefix-1, suffix+1) + 2
###if string[prefix] != string[suffix], then lps(string, prefix, suffix)== max(lps(string, prefix-1, suffix), lps(string,prefix,suffix+1)

def lps(string): #######recursion version#######
    def lps2(string,prefix,surffix,table):
        if table.get((prefix,surffix)):
            return table[(prefix,surffix)]

        if prefix>surffix:
            table[(prefix,surffix)] = (0,[str()])
            return (0,[str()])
        if prefix == surffix:
            table[(prefix,surffix)] = (1,[string[prefix]])
            return (1,[string[prefix]])

        if string[prefix]==string[surffix]:
            num, re = lps2(string,prefix+1,surffix-1,table)
            table[(prefix,surffix)] = (num+2, [string[prefix]+i+string[prefix] for i in re])
            return table[(prefix,surffix)]

        else:
            sub1=lps2(string,prefix+1,surffix,table)
            sub2=lps2(string,prefix,surffix-1,table)
            if sub1[0]==sub2[0]:
                table[(prefix,surffix)] =(sub1[0],sub1[1]+sub2[1])
                return table[(prefix,surffix)]

            elif sub1[0]>sub2[0]:
                table[(prefix,surffix)] =(sub1[0],sub1[1])
                return (sub1[0],sub1[1])

            else:
                table[(prefix,surffix)] =(sub2[0],sub2[1])
                return (sub2[0],sub2[1])
    return lps2(string,0,len(string)-1,dict())

s="ABBDCACB"

lps(s)