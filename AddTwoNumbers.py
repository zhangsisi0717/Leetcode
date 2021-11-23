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
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    i,j = l1,l2
    head,prev = None,None
    add = 0
    while i or j:
        i_val = i.val if i else 0
        j_val = j.val if j else 0
        total = i_val + j_val + add
        new_node = ListNode(total % 10)
        add = 1 if total >= 10 else 0

        if prev:
            prev.next = new_node
        prev = new_node
        if not head:
            head = prev

        i = i.next if i else None
        j = j.next if j else None

    if add:
        prev.next = ListNode(1)
    return head