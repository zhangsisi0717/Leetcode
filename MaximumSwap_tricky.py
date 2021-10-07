import typing
##https://leetcode.com/problems/maximum-swap/
"""
swap only once to make the number largest

step 1: keep track of all the digits and its corresponding last index, and sort the number in descending order [6,5,4,3,2,1]
we want to make the index of largest number as small as possible to make the number largest
iterate the num, if cur_digit < cur_max_number, then we just switch cur_digit and the last index of cur_max_number
                if cur_digit == cur_max_number, then we check if cur_digit is the last index, if not, we continue, 
                                if cur_digit is already the last index of the cur_max_number, we then make next_largest_number the cur_max_number  
"""
def maximumSwap(self, num: int) -> int:
    str_num = [i for i in str(num)]
    num_to_lastIdx = dict()
    for idx,e in enumerate(str_num):
        num_to_lastIdx[e] = idx

    sorted_num = sorted([i for i in num_to_lastIdx.keys()],reverse=True)
    cur_max_idx = 0
    for j, n in enumerate(str_num):
        last_idx = num_to_lastIdx[sorted_num[cur_max_idx]]
        if n<sorted_num[cur_max_idx]:
            str_num[j],str_num[last_idx] = str_num[last_idx],str_num[j]
            break

        else:
            if j==last_idx:
                cur_max_idx+=1

    return int("".join(str_num))


