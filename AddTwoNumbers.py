#https://leetcode.com/problems/add-two-numbers/

##19999999 + 19999 can be regarded as:
##   19999999 num1
## + 00019999 num2
##starting from the last digits:
##init_add =0
##while(not digit1 or not digit2):
###
##    new_sum = digit 1 + digit 2 + add
##    if new_sum >10, add =1 else 0
##After all the iterations, if add = 1, we need to add another "1" to the result
##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_l1 = l1
        cur_l2 = l2
        add = 0
        all_nodes = deque([])
        head,tail = None,None
        while cur_l1 or cur_l2:
            l1_value = 0 if not cur_l1 else cur_l1.val
            l2_value = 0 if not cur_l2 else cur_l2.val
            temp_sum = add + l1_value + l2_value
            new_node = ListNode(temp_sum%10)
            if all_nodes:
                last = all_nodes.pop()
                last.next = new_node
            if not head:
                head = new_node
            tail = new_node
            all_nodes.append(new_node)
            add = 0 if temp_sum <10 else 1

            cur_l1 = cur_l1.next if cur_l1 else None
            cur_l2 = cur_l2.next if cur_l2 else None

        tail.next = ListNode(val=1) if add ==1  else None
        return head


##https://leetcode.com/problems/add-two-numbers-ii/ reversed order
"""
if the order is reversed, either change its order to make the least significant digit to be the first one, 
or copy the orginal value
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list,l2_list,new_list = [],[],[]
        while(l1 or l2):
            if l1:
                l1_list.append(l1.val)
                l1 = l1.next
            if l2:
                l2_list.append(l2.val)
                l2 = l2.next
        i,j=len(l1_list)-1,len(l2_list)-1
        add = 0
        prev_node = None
        while(i>=0 or j>=0):
            l1_val = l1_list[i] if i>=0 else 0
            l2_val = l2_list[j] if j>=0 else 0
            temp_sum = (l1_val + l2_val + add) % 10
            add = (l1_val + l2_val + add) // 10
            cur_node = ListNode(val=temp_sum,next=prev_node)
            prev_node = cur_node
            i-=1
            j-=1
        return ListNode(val=1,next=prev_node) if add ==1 else cur_node
