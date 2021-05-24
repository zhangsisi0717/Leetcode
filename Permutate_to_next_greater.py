#https://leetcode.com/problems/next-permutation/
def nextPermutation(nums) -> None: #modify in-place
    def rever(start,end):
        b= nums[start:end]
        b.reverse()
        nums[start:end] = b

    ## 16541, then swith 1 with 4 => 46511 => 41156
    found = False
    for index in range(len(nums)-1,0,-1):
        if nums[index] <= nums[index-1]:
            continue
        for j in range(index,len(nums)):
            if nums[index-1] >= nums[j]:
                temp = nums[j-1]
                nums[j-1] = nums[index-1]
                nums[index-1] = temp
            elif j == len(nums) -1 and nums[index-1] < nums[j]:
                temp = nums[j]
                nums[j] = nums[index-1]
                nums[index-1] = temp

            rever(index,len(nums)+1)
            found = True
            break
        else:
            break

    if not found: nums.reverse()
