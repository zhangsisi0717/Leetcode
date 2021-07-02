from typing import List
"""

if unique subset of sub_list before idx-1  [list 1] ,[list 2], [list 3]
 then unique subset of sub_list considering numbers before index "idx"
  == [[list 1] ,[list 2], [list 3], [list 1,s[idx]] ,[list 2,s[idx]], [list 3,s[idx]]
  
len(s)==1 => number of result: 2
len(s)==2 => number of result: 4
len(s)==3 => number of result: 8
len(s)==4 => number of result: 16

each time, double the number of the result, for idx, we need to read 2 + 2^2 + 2^3 + 2^4 + ....2^n (n==len(s))

formula of the geometry sequence == a1 * ((q^n)-1)  // (q-1)   => 2 * (2^n) // 1 == 2^(n+1)
therefore time comlexity  == O(2**(n+1))  n == len(s)

"""
def subsets(nums: List[int]) -> List[List[int]]:
    def uniqueSet(idx): ##return unique subset considering numbers before index "idx"(include idx)
        if idx == 0:
            print(f"idx={idx}, len = 2")
            return [[],[nums[0]]]

        result = []
        temp_re = uniqueSet(idx-1)
        for i in temp_re:
            result.append(i+[nums[idx]])

        print(f"idx={idx},len = {len(result + temp_re)}")
        return result + temp_re

    return uniqueSet(len(nums)-1)


nums = [i for i in range(5)]
subsets(nums)



