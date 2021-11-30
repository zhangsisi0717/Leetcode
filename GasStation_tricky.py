import math
#https://leetcode.com/problems/gas-station/submissions/
"""
O(n2) solution:

"""
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    def canFinish(start):
        cur_pos = start
        cur_gas = gas[start]
        while cur_pos<start+len(gas):
            if cur_gas - cost[cur_pos % len(gas)] < 0:
                return False

            cur_gas = cur_gas - cost[cur_pos % len(gas)] + gas[(cur_pos+1)%len(gas)]
        return True

    for i in range(len(gas)):
        if canFinish(i):
            return i

    return -1

"""
O(n) solution
gas = [1,2,3,4,5], cost = [3,4,5,1,2]

step 1 = gas-cost => diff = [delt1, delta2, delt3, delta4...deltaN]  => diff[index] is  gas[i]-cost[i]

step 2: if we start from station i, each time, we travel to next station, the left gas would be:
        subarray_1: delta_i 
        subarray_2: delta_i + delta_i+1
        subarray..: delta_i + delta_i+1+....delta_N
        subarray..: delta_i + delta_i+1+....delta_N + delta_1 + delta_2 + ....delta_i-1

step 3: create "min_sum_starting_at_index_i" "max_sum_starting_at_index_i" to find the min_subarray in a circular array => reason for this step is as follows
         
In the whole trip, as long as the left_tank >=0 when we reach each station, we could finish the trip, 
so the point is to find the "least left gas" in the whole trip, which means we need to find the "minimum_sum_subarray" for each starting point i.

as long as there is one  starting_point_i whose minimum_sum_subarray > 0 => We could finish the trip

Tricky thing here is, since it is circular,  the minimum_sum_subarray could be [3,4,5] or [3,4,5,1]

So we need first find min_sum_subarray for all points as regular array => min_starting_at_index_i 
then find max_sum_subarray for all points as regular (max_ending_at_index_i) => the min will be total - max_sum_subarray
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i]-cost[i] for i in range(len(gas))]
        total = sum(diff)
        if total < 0:
            return -1

        min_subarray, max_subarray = self.findMinMaxSubArray(diff)
        # print(f"min_subarray={min_subarray}, max_subarray={max_subarray}")
        for j in range(len(diff)):
            if j == 0:
                if min_subarray[j]>=0:
                    return j
            else:
                if min(min_subarray[j], total-max_subarray[j-1], total)>=0:
                    return j

        return -1





    def findMinMaxSubArray(self,diff):
        min_starting_at_index_i = [None for _ in range(len(diff))]
        max_ending_at_index_i = [None for _ in range(len(diff))]
        for i in range(len(diff)):
            if i==0:
                min_starting_at_index_i[len(diff)-1-i] = diff[len(diff)-1-i]
                max_ending_at_index_i[i]  = diff[i]

            else:
                min_starting_at_index_i[len(diff)-1-i] = min(min_starting_at_index_i[len(diff)-i]+diff[len(diff)-1-i],diff[len(diff)-1-i])
                max_ending_at_index_i[i] = max(max_ending_at_index_i[i-1]+diff[i],diff[i])

        return min_starting_at_index_i,max_ending_at_index_i









