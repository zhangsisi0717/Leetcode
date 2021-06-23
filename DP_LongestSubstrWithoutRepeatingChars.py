#https://leetcode.com/problems/longest-substring-without-repeating-characters/
from type_checking import *
def lengthOfLongestSubstring(s: str) -> int:
    letter_to_idx = dict()
    longest = 0
    cur_start_end = [0,-1]
    cur_length=0 ##current means longest substring ending at index i
    cur_set = set()
    for i in range(len(s)):
        print(f"cur_stirng = {s[cur_start_end[0]:int(cur_start_end[1]+1)]}")
        print(f"cur_set = {cur_set}")
        print(f"longest = P={longest}")
        if s[i] not in cur_set:
            cur_set.add(s[i])
            cur_length +=1
            letter_to_idx[s[i]] = i
            cur_start_end[1] = i
        else:
            cur_start_end[0] = letter_to_idx[s[i]]+1
            cur_start_end[1] = i
            letter_to_idx[s[i]] = i
            cur_length = cur_start_end[1]-cur_start_end[0] + 1
            cur_set = set(list(s[cur_start_end[0]:int(cur_start_end[1]+1)]))

        if cur_length > longest:
            longest = cur_length

    return longest


lengthOfLongestSubstring("abcabcbb")

