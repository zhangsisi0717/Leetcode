#https://leetcode.com/problems/next-greater-element-iii/
"""
number = 12485321
increasing_number = []
keep iterate from end_idx to 0, if it is always increasing order, then return -1

if we found decreasing order, then we go back to check visited number, and find the smallest digit that is larger than "this digit"
for example:
number = 12485321,
increasing_number = [1,2,3,5,8], 4 is smaller than "8", then we go to check the smallest number in "'increasing_number" that is larger than "4". here is 5
so "increasing_number"  becomes  ["5",1,2,3,"4",8]
return as "12" + "512348"
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = str(n)
        number = []
        found = False
        idx = 0
        for idx in range(len(num)-1,0,-1):
            if int(num[idx]) <= int(num[idx-1]):
                number.append(num[idx])

            else:
                found = True
                number.append(num[idx])
                number = [num[idx-1]] + number
                for j in range(1,len(number)):
                    if int(number[j])>int(number[0]):
                        number[0],number[j] = number[j],number[0]
                        break
                break
        re = num[:idx-1] + "".join(number)
        return int(re) if found and int(re)<=2**31-1 else -1



