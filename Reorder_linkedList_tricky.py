#https://leetcode.com/problems/reorder-list/
"""


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time complexity O(N), space complexity O(1)

step 1: find middle point of linked list [1,2,{{3}},4,5] (two pointer method)
        [1,2,3,{{4}},5,6]
        
step 2: reverse nodes in the second half [1=>2=>3=>{{4}}<=5<=6] {{4}}=>null

step 3: combine two ordered linked list
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow_p = fast_p = head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        prev,cur = None,slow_p
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        p_1,p_2 = head,prev
        while p_2.next:
            _next_1 = p_1.next
            _next_2 = p_2.next
            p_1.next = p_2
            p_2.next = _next_1
            p_1 = _next_1
            p_2 = _next_2

        return head










