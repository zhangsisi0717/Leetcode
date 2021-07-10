from typing import List
from collections import defaultdict
"""
nums = [4,5,0,-2,-3,1] k =5
keep track of mod of nums:
    mod[4,4,0,2,4,5]
mod[0] == mod[1] == mod[4] == 4, which means sum of 

subarray between (0,4) and (1,4) can both be dividble by 5

first time we meet 4, number +=0
second time we meet 4, number +=1
third time we meet 4, number +=2
fourth time we meet 4, number +=3
so for mod other than 0: number = 0+1+2+3+....+n-1

Howerver, mod=0 is different,
first time we meet 0, number +=1
second time we meet 0, number +=2
third time we meet 0, number +=3
fourth time we meet 0, number +=4
so for mod 0: number  = 1+2+3+4.....+n
......

so we only need to count the frequency of mods and then we can  get the final result 

"""
def subarraysDivByK(nums: List[int], k: int) -> int:
    mod_to_count = defaultdict(lambda:0)
    summation = 0
    for num in nums:
        summation += num
        mod_to_count[summation%k] +=1

    final=0
    for mod in mod_to_count:
        if mod == 0:
            final += (1+mod_to_count[mod])*mod_to_count[mod]/2

        else:
            final += (1+mod_to_count[mod]-1)*(mod_to_count[mod]-1)/2

    return int(final)



