def maxProduct(nums) -> int: ###https://leetcode.com/problems/maximum-product-subarray/submissions/
    curMax=nums[0]
    curMin = nums[0]
    gMax = nums[0]
    for i in range(1,len(nums)):
        temp = curMax
        curMax = max(nums[i],curMax*nums[i],curMin*nums[i])
        curMin = min(nums[i],temp*nums[i],curMin*nums[i])

        if curMax>gMax:
            gMax = curMax
    return gMax


maxProduct([-1,2,3,-1,-2,-3,-5,3,2,-5,-1,2,5,4,6,3,-6,-4,-5,3])