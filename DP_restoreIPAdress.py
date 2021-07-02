from functools import cache

"""
"25525511135"
2. + valid ip of "5525511135" (left integer == 3)
25. + valid ip of "525511135" (left integer == 3)
255. + valid ip of "25511135" (left integer == 3)
"""
def restoreIpAddresses(s: str) -> List[str]:
    if len(s)>12: return []
    @cache
    def validIp(idx,num): #return list of valid ip starting from index "idx", with left number of left integers
        if num == 1:
            if (idx==len(s)-1) or ((int(s[idx])>0 and 10<=int(s[idx:])<=255)):
                return [s[idx:]]
            else:
                return []

        result = []
        for i in range(idx+1,idx+4):
            if (i<len(s)) and ((i == idx+1) or (int(s[idx])>0 and 10<=int(s[idx:i])<=255)):
                for re in validIp(i,num-1):
                    if re:
                        result.append(s[idx:i]+"."+re)
        return result
    return validIp(0,4)


