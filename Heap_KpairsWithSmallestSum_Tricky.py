#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
import heapq
class Solution:
    """
    i,j => nums1, nums2
    step 1: put element [nums1[0],nums2[0]] into minheap
    step 2: each time, we pop out the current smallest [i,j], and put all possible candidates into minheap, the next candidates are either [i+1,j] or [j+1,i]

    step 3: keep pop out until we have k elements

    Time Comlexity: each time we need to add at most 2 elements into min-heap, and add K times
        =>k * lg(k*2)
        =>O(klgk)

    Note: extention:
    if there are m list of ordered arrays(M1,M2,M3...Mn), we can also use minheap same as above solution,
    ONLY DIFFERENCE IS THAT: there are M candidates: [M1_idx+1,M2_idx,M3_idx,...Mn_idx],
    [M1_idx,M2_idx+1,M3_idx,...Mn_idx],[M1_idx,M2_idx,M3_idx+1,...Mn_idx]....[M1_idx,M2_idx,M3_idx,...Mn_idx+1]
    """
def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = [[nums1[0]+nums2[0],0,0]]
    heapq.heapify(heap)
    heap_set = {(0,0)}
    result = []

    while(k>0 and heap):

        cur_sum,cur_i,cur_j = heapq.heappop(heap)
        result.append([nums1[cur_i],nums2[cur_j]])
        k-=1
        next_candi = []
        if cur_i < len(nums1)-1:
            next_candi.append([nums1[cur_i+1]+nums2[cur_j],cur_i+1,cur_j])

        if cur_j < len(nums2)-1:
            next_candi.append([nums1[cur_i]+nums2[cur_j+1],cur_i,cur_j+1])

        for c in next_candi:
            if (c[1],c[2]) not in heap_set:
                heapq.heappush(heap,c)
                heap_set.add((c[1],c[2]))
    return result






