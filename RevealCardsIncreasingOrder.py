import math
import copy
"""
a=[1,2,3,4,5,6]
firstly, order the list,then
if len(list) == 3: such as [1,2,3], just return [1,3,2]
if len(list) <= 2: such as [1,2], just return the list
else:
cut current list in half such as a = [1,2,3,4,5,6]

first half is [1,2,3], second half is [4,5,6], if len(list) is odd, then first half -1 == second half

reveal_order_second_half = recursion(second_half), for example recursion([4,5,6]) return [4,6,5]

if len(first half) == len(second_half) => insert  "reveal_order_second_half" into order first half one by one
if len(first half) > len(second_half) => put last element in the "reveal_order_second_half" to the front and insert it
into first half one by one

first half = [1,2,3]
reveal_order_second_half = [4,6,5]
return [1,4,2,6,3,5]

if first half = [1,2,3]
reveal_order_second_half = [4,5]
return [1,5,2,4,3]
"""
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        def reveal(orderList):
            # print(f"orderList={orderList}")
            if len(orderList) <= 2:
                return orderList
            if len(orderList) == 3:
                return [orderList[0],orderList[2],orderList[1]]

            mid = int(int(len(orderList)/2) + len(orderList) % 2)
            # print(f"mid={mid}")
            new_list = copy.deepcopy(orderList[mid:])
            re = reveal(new_list)
            re = [re[-1]] + re[0:len(re)-1] if len(orderList) % 2==1 else re
            reveal_list = []
            for idx in range(mid):
                reveal_list.append(orderList[idx])
                if idx < len(re):
                    reveal_list.append(re[idx])
            return reveal_list
        return reveal(deck)


