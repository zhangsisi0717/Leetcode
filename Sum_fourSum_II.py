from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_12 = dict()
        for i in nums1:
            for j in nums2:
                if (i+j) not in sum_12:
                    sum_12[i+j] = 1
                else:
                    sum_12[i+j] +=1
        sum_34 = dict()
        for k in nums3:
            for l in nums4:
                if (k+l) not in sum_34:
                    sum_34[k+l] = 1
                else:
                    sum_34[k+l] +=1

        total = 0
        for value,fre in sum_12.items():
            if -value in sum_34:
                total += fre * sum_34[-value]
        return total



