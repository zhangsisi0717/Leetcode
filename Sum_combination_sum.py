##https://leetcode.com/problems/combination-sum/
from functools import cache
def combinationSum(candidates, target):
    @cache
    def combi(target):
        if target<0:
            return False,[]
        if target ==0:
            return True,[[]]
        re=[]
        for c in candidates:
            found,combo = combi(target-c)
            if found:
                for i in combo:
                    temp = i + [c]
                    re.append(temp)
        if re:
            return True,re
        return False,[]

    unique_result={tuple(sorted(i)) for i in combi(target)[1]}
    return list(unique_result)
candidates=[2,3,6,7]
target=7
combinationSum(candidates, target)[1]
