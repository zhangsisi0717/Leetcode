class Solution: ##https://leetcode.com/problems/continuous-subarray-sum/
    """
    iterate from idx=0 to end of the array:
    if a1+a2+a3 % k ==2 and a1+a2+a3+a4+a5 % k == 2 , then a4+a5 % k ==0
    so use moddict to save the mod to dictionary as dict[mod] = idx i, and if that mod shows up again at idx j, then if idx j- idx i>=2, then return true
    Need to initialize modditc[0] = -1
    """
    
    def checkSubarraySum(nums: int, k: int) -> bool:
        moddict=dict()
        moddict[0] = -1
        cur_mode=0
        for idx in range(len(nums)):
            cur_mode += nums[idx]
            cur_mode = cur_mode % k
            if cur_mode not in moddict:
                moddict[cur_mode] = idx
            elif idx-moddict[cur_mode] >= 2:
                return True

        return False