from collections import deque
"""
1.sort number of abc by increasing order, if it is a < b < c
2. then add abcabcabc....  number of abc == number of a
3. then count left b, add bcbcbcbcbc...    number of bc equals number of left "b"
4. now, there is only "c" left 
5. insert c into current result abcabcabcabcbcbcbcbc, iterate from idx =0 to the end of this string, we 
need to evaluate  if [idx-2,idx-1,c] === ccc, and [c,idx,idx+1] === ccc and [idx-1,c,idx] === c, if not, we could insert 
this c into current index, and then index +=1
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        l = [(a,"a"),(b,"b"),(c,"c")]
        l.sort()
        re = ""
        string = deque([l[0][1], l[1][1], l[2][1]]) * l[0][0]

        left_2nd = l[1][0]-l[0][0]
        left_3rd = l[2][0]-l[0][0]

        string += (l[1][1] + l[2][1]) * left_2nd

        left_3rd = l[2][0]-l[0][0]-left_2nd

        forbid = [["a","a","a"],["b","b","b"],["c","c","c"]]
        idx = 0
        while(idx<len(string) and left_3rd>0):
            couldAdd=True
            if idx < len(string)-2 and [l[2][1],string[idx],string[idx+1]] in forbid:
                couldAdd = False
            if idx> 0 and [l[2][1],string[idx-1],string[idx]] in forbid:
                couldAdd = False
            if idx >= 2 and [l[2][1],string[idx-1],string[idx-2]] in forbid:
                couldAdd = False

            if couldAdd:
                string.insert(idx,l[2][1])
                left_3rd-=1

            idx +=1

        return "".join(string)
