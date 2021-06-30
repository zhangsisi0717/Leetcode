##https://leetcode.com/problems/binary-trees-with-factors/
from collections import defaultdict
"""
given list of numbers, return number of potential binary trees (parent must be product of left and right children)

step 1: sort the number array, create a hashmap to store the number of possible trees if using this "key" as a root
step 2: starting from the smallest number to largest number, and calculate and update number of possible trees one by one

  400
  / \
  40 10
  
400 = 40 * 10, therefore, number of 400 += 2*number(40) * number(20)
find all the combination of (fac1,fac2) for 400, and 
if fac1 != fac2: final_result +=  2 * num(fac1) * num(fac2) 
            else: final_result += num(fac1) * num(fac2) 
"""
def numFactoredBinaryTrees(arr: List[int]) -> int:
    sorted_arr = sorted(arr)
    num_trees = defaultdict(lambda:0)
    final=0
    for idx in range(len(sorted_arr)):
        # print(f"idx={idx},sorted_arr[idx]={sorted_arr[idx]}")
        num_trees[sorted_arr[idx]] +=1
        # print(f"num_trees={num_trees}")
        candi = set(sorted_arr[:idx])
        while(candi):
            cur = candi.pop()
            if sorted_arr[idx] % cur == 0 and sorted_arr[idx]/cur in num_trees:
                fac = 2 if sorted_arr[idx]/cur != cur else 1
                num_trees[sorted_arr[idx]] += fac*num_trees[cur] * num_trees[sorted_arr[idx]//cur]
                if sorted_arr[idx]//cur in candi:
                    candi.remove(sorted_arr[idx]//cur)
        final += num_trees[sorted_arr[idx]]
        # print(f"num_trees[sorted_arr[idx]]={num_trees[sorted_arr[idx]]}")
    return final%(10**9 + 7)
