#https://leetcode.com/problems/next-permutation/
def nextPermutation(nums) -> None: #modify in-place
    """
    example: ## 26541, then swith 2 with 4 => 46521 => 41256
    explaination: in order to found the next largest order, we need to find the first descending element, so we iterate from end to the begining, in the example, 1<4, then continue, 4<5, then continue, 5<6, then continue, then 6>2,
    then we need to find the smallest number in "6541" that is larger than 2, then we swap 2 with 4 => 46521 => and reverse the list after "4" to become 41256
    """
    def rever(start,end):
        b= nums[start:end]
        b.reverse()
        nums[start:end] = b

    found = False
    for index in range(len(nums)-1,0,-1):
        if nums[index] <= nums[index-1]:
            continue
        for j in range(index,len(nums)):
            if nums[index-1] >= nums[j]:
                temp = nums[j-1]
                nums[j-1] = nums[index-1]
                nums[index-1] = temp
                rever(index,len(nums)+1)
                found = True
                break
            elif nums[index-1] < nums[len(nums)-1]:
                temp = nums[len(nums)-1]
                nums[len(nums)-1] = nums[index-1]
                nums[index-1] = temp
                rever(index,len(nums)+1)
                found = True
                break
        if found:
            break

    if not found: nums.reverse()

a = [86, 83, 38, 5, 90, 76, 8, 51, 47, 74, 71, 7, 53, 49, 87, 79, 51, 37, 90, 33]
nextPermutation(a)