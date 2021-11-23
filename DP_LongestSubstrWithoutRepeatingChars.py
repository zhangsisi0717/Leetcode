#https://leetcode.com/problems/longest-substring-without-repeating-characters/
import typing
"""
s = "abcabcbb"
1. keep track of map1: key: char  value: currently seen largest index of that character
2. max_length_ending_at_index_j

iterate from j = 0 to the end:
    if s[j] in the charater_to_index:  => we have seen this characer
        go back to check the starting index of substring with max_length_ending_at_index[j-1] , eg. "abca", s[3]=a, and we have seen "a", max_length_ending_at_2 is 3, and the prefix index of that substring 0. so the max_length_ending_at_3 = 3-(0+1)+1=3
        if the prev index of this character <  j-1-max_length_ending_at_index[j-1]:
            then max_length_ending_at_index[j] = max_length_ending_at_index[j-1] + 1
            
        else:
            max_length_ending_at_index[j] = j-string_to_index[s[j]]
    
    else: (havent seen the characer)
        max_length_ending_at_index[j] = max_length_ending_at_index[j-1] + 1
    
"""
def lengthOfLongestSubstring(s: str) -> int:
    max_length_ending_at_index = dict()
    string_to_index = dict()
    max_length= 0
    j = 0
    while j<len(s):
        if s[j] in string_to_index:
            if string_to_index[s[j]] < (j-1-max_length_ending_at_index[j-1]):
                max_length_ending_at_index[j] = max_length_ending_at_index[j-1] + 1
            else:
                max_length_ending_at_index[j] = j-string_to_index[s[j]]

        else:
            max_length_ending_at_index[j] = 1 if j == 0 else max_length_ending_at_index[j-1] + 1

        string_to_index[s[j]] = j

        max_length= max(max_length, max_length_ending_at_index[j])
        j+=1
    return max_length


lengthOfLongestSubstring("abcabcbb")

