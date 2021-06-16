from collections import Counter
"""
p
"""
def fourSum(nums, target):
    num_to_count = Counter(nums)
    unique_num = [i for i in num_to_count.keys()]
    num_count = [j for j in num_to_count.values()]
    print(unique_num)
    print(num_count)
    def sumToIdx(idx, target, num_left, num_count):
        print(f"idx = {idx}, target = {target},num_left = {num_left},num_count = {num_count}")
        if idx == 0:
            return [num_left*[unique_num[0]]] if num_count[0]>=num_left and num_count[0]*num_left == target else False
        # if target<0: return False
        # if target == 0: return []
        if num_left<=0 and target !=0: return False
        if num_left == 0 and target == 0: return [[]]
        ub = min(num_left, num_count[idx])
        print(f"ub={ub}")
        re = []
        for i in range(0,ub+1):
            print(f"i = {i}")
            num_count_copy = num_count.copy()
            num_count_copy[idx] = num_count_copy[idx]-i
            temp_re = sumToIdx(idx - 1, target-i*unique_num[idx], num_left-i, num_count_copy)
            print(f"temp_result={temp_re}")
            if temp_re != False:
                new_re = [j + i*[unique_num[idx]] for j in temp_re if j != False]
                re += new_re
        return re if re else False

    return sumToIdx(len(unique_num)-1, target, 4, num_count)

nums = [1,0,-1,0,-2,2]
# nums = [1,-1,-2,2]
target = 0
fourSum(nums, target)


"""
brute force solution
"""
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    sort_nums = sorted(nums)
    def twoSum(lb,ub,target):
        re =[]
        while(lb<ub):
            if sort_nums[lb] + sort_nums[ub] >target:
                ub -=1

            elif sort_nums[lb] + sort_nums[ub] <target:
                lb +=1

            else:
                re.append([sort_nums[lb],sort_nums[ub]])
                ub -= 1
                lb +=1
        return re
    final = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            temp = twoSum(j+1,len(nums)-1,target-sort_nums[i]-sort_nums[j])
            four_sum = [[sort_nums[i],sort_nums[j]] + k for k in temp] if temp else []
            final += four_sum

    return final
