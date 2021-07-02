##https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
from collections import Counter
"""
sorted_frequecy = [1,1,2,3,3,3,3,6,7]
we add the sorted frequency one by one
each time if this fre already exist ,then move pointer to the next available frequency, num_del += (cur_frequency - pointer),
if move to 0 and all the frequencies are not available, then num_del += cur_frequency
for next frequency, if next_frequency == pre_frequecy and then pointer does not change position , else pointer move to next_frequency

"""


def minDeletions(s: str) -> int:
    s_to_count = Counter(s)
    fre_to_count = Counter([i for i in s_to_count.values()])
    sorted_fre = sorted([i for i in s_to_count.values()])
    unique_fre = set()
    num_del = 0
    prev_num=None
    pointer=None
    cur_index = 0
    print(f"fre_to_count={fre_to_count}")
    print(f"sorted_fre={sorted_fre}")
    while(cur_index<len(sorted_fre)):
        print(f"cur_index = {cur_index}")
        cur_f = sorted_fre[cur_index]
        if cur_f not in unique_fre:
            unique_fre.add(cur_f)
            fre_to_count[cur_f]-=1
            prev_num,pointer=cur_f,cur_f
            cur_index +=1
            print(f"add_directly no del")
            print(f"prev_num={prev_num}, pointer={pointer}")
            continue

        pointer = pointer if cur_f == prev_num else cur_f
        if pointer<=1:
            print(f"cur pointer <=1 ={pointer}")
            num_del += fre_to_count[cur_f]*cur_f
            cur_index += fre_to_count[cur_f]
            fre_to_count[cur_f]=1
            continue

        else:
            add = cur_f - pointer
            print(f"cur pointer > 1 ={pointer}")
            while(pointer>=1 and pointer in unique_fre):
                print(f"scanning cur_pointer = {pointer}")
                pointer -=1
                add +=1
            unique_fre.add(pointer)
            num_del += add
            fre_to_count[cur_f]-=1
        print(f"finish scanning cur_pointer = {pointer}")
        print(f"num_del = {num_del}")
        cur_index +=1

    return num_del

s ="aaabbbccdddddeeeefffggghhhrrrfhfhfhfhffffjjjjjjjjjjjiiiiiiiooooooolldahjkshdljkashdadhdhdhdhdhdhdhdhdhhhhryue"
minDeletions(s)
