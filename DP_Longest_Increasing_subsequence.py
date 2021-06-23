from typing import List
"""
keep updating a list of longest_subsequence_starting_at_index = []
longest_subsequence_starting_at_index[i] = max(longest_subsequence_starting_at_index[j])+1  (iterate all the j s.t j>i and nums[j]>nums[i], and find the max j)

"""


def lengthOfLIS(nums: List[int]) -> int:
    max_length=1
    lngest_seq_starting_at = [1 for _ in range(nums)]
    for i in range(len(nums)-2,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i]:
                lngest_seq_starting_at[i] = max(lngest_seq_starting_at[i],lngest_seq_starting_at[j]+1)

        max_length = max(max_length,lngest_seq_starting_at[i])

    return max_length



