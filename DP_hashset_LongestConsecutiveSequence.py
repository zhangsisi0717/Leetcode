def longestConsecutive(self, nums: List[int]) -> int:
    numset = set(nums)
    leftnum = set(nums)
    longest = 0

    @cache
    def maxLength(num):
        if num not in numset:
            return 0

        leftnum.remove(num)
        return 1 + maxLength(num-1)

    maximum=0
    for i in nums:
        if i in leftnum:
            maximum = max(maximum,maxLength(i))

    return maximum






