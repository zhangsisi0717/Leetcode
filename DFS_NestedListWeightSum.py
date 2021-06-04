#https://leetcode.com/problems/nested-list-weight-sum-ii/
class Solution:
    def depthSumInverse(nestedList) -> int:
        max_layer = 0
        def recursion(nestInteger,layer):
            nonlocal max_layer
            max_layer = max(layer,max_layer)
            if nestInteger.isInteger(): return [(nestInteger.getInteger(),layer)]
            temp_l = nestInteger.getList()
            result = []
            for e in temp_l:
                result += recursion(e,layer+1)

            return result
        final = []
        for i in nestedList:
            final += recursion(i,1)
        total = 0
        for num,n_layer in final:
            total += (max_layer - n_layer + 1) * num
        return total
