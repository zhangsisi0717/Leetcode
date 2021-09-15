"""
###https://leetcode.com/problems/median-of-two-sorted-arrays/
explaination:
a=[0, 1, 1, 2||, 4, 5, 6]
b=[0, 0, 0||, 1, 2, 3, 4, 5]

the point is to find a partition index i,j on both a and b such that
    a[:i] and b[:j] is left half part, and a[i+1:],b[j+1:] are right half part

do a binary search on shorter list

half_length = (len(a) + len(b)) //2
lb,ub = 0,len(a)
mid = (lb + ub) // 2

since we know  "half_length", if partition pos on a is at "mid", then partition pos on b must be
   j =  (half_length - mid - 2)

if a[i]<= b[j+1] and b[j]<=a[i+1], then we found the correct partition point on a
if a[i] > b[j+1] => ub = mid -1
if a[i+1] < b[j] => lb = mid + 1

Note: if i or j <0 a[i] and a[j] = "-inf"
        if i or j > len(a) or len(b) => a[i] and a[j] = "inf"

We will eventually find the partition position and return
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2
        if len(a) >len(b):##binary search in shorter list "a" to find the partition position
            a,b = b,a

        half_length = (len(a) + len(b)) // 2
        lb,ub = 0, len(a)-1
        while True:
            mid = (lb + ub) // 2
            j = half_length-mid-2

            l_a = a[mid] if mid >= 0 else float("-inf")
            r_a = a[mid+1] if mid+1 < len(a) else float("inf")

            l_b = b[j] if j>= 0 else float("-inf")
            r_b = b[j+1] if j+1<len(b) else float("inf")

            if l_a <= r_b and l_b<=r_a:
                if (len(a)+len(b)) % 2==1:
                    return min(r_a,r_b)
                else:
                    return (max(l_a,l_b) + min(r_a,r_b)) / 2

            elif l_a > r_b:
                ub = mid -1

            else:
                lb = mid + 1










