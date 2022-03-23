##https://leetcode.com/problems/contiguous-array/submissions/

"""
cumulatively count diff = (number of 0's - number of 1's) from i = 0 to end
if diff[i] == diff[j], then nums[i:j] must have the same number of 1's and 0's

for example, at index i=5, num_1 = 5, num_0 = 10
             at index i=10, num_1 = 6, num_0 = 11
             then nums[5:10] has num_1 = 6-5=1 , num_0 = 11-10=1

X0, X1 => cumulative sum number of 0 and 1
Y0, Y1

"""
def findMaxLength(nums: List[int]) -> int:
    diff = {0:-1}
    num_0, num_1 = 0,0
    max_length = 0
    for idx in range(len(nums)):
        if nums[idx] == 0:
            num_0 +=1
        else:
            num_1 +=1

        if (num_1 - num_0) not in diff:
            diff[num_1 - num_0] = idx
        else:
            max_length = max(max_length, idx-diff[num_1 - num_0])

    return max_length
