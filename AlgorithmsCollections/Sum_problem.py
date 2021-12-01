import math
"""
Two sum with multiple solutions: return  "list of (i,j), i,j is index and i<j"

Solution: 
step1: sort list  first

step2: use two pointer to generate all the (i,j) tuples, O(nlgn)
"""


"""
step1: 
    create a dictionary, key: num, value: number of that value
    create a set containing all the keys
step2: 
        num=0
        while(set is not empty):
            cur = set.pop()
        
            if cur == target/2:
                num += dict[cur] * (dict[cur]-1)/2   => formula for n choose 2
                
            elif (target-cur) in all_mods:
                set.remove(target-cur)
                num += dict[cur] * dict[target-cur]
             
        return int(num)
        
"""




