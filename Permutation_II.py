##https://leetcode.com/problems/permutations-ii/
from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_to_count = defaultdict(lambda:0)
        """
        array with duplicates: just use a hashmap to store the nums key: nums val: occurence of key
        when doing recursion,each time to iterate the unique key and generate the results, this way, we could avoid duplicate results
        """
        for i in nums:
            nums_to_count[i]+=1
            def gen_permu(nums_to_count):
                if not nums_to_count:
                    return [[]]
                result = []
                for j in nums_to_count.keys():
                    copy_dict = nums_to_count.copy()
                    copy_dict[j] -=1
                    if copy_dict[j] == 0: copy_dict.pop(j)
                    next_permu = gen_permu(copy_dict)
                    temp = [[j] + k for k in next_permu]
                    result += temp

                return result

        return gen_permu(nums_to_count)
