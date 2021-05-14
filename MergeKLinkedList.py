from type_checking import *
import  heapq
#https://leetcode.com/problems/merge-k-sorted-lists/
"""
Explanination: 
use heap to implement merging K linked lists
[[1,4,5],[1,3,4],[2,6]]
heapify -> (1,1,2) 
then head = 1, cur_node = head
while(heap is not empty):
    cur_node = lists[0]
    if cur_node.next != None -> then replace lists[0] with cur_node.next 
    else:
        pop cur_node from the lists heap
    
    if lists heap is not empty:
        cur_node.next = lists[0]
time complexity: O(NlgK), N is the number of nodes in the final lists,and K is number of lists
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda s, o: s.val < o.val
ListNode.__le__ = lambda s, o: s.val <= o.val
ListNode.__eq__ = lambda s, o: s.val == o.val
ListNode.__gt__ = lambda s, o: s.val > o.val
ListNode.__ge__ = lambda s, o: s.val >= o.val

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [i for i in lists if i]
        if not lists:
            return None
        heapq.heapify(lists)
        head = lists[0]
        while(lists):
            cur_node = lists[0]
            if cur_node.next:
                heapq.heapreplace(lists, cur_node.next)
            else:
                heapq.heappop(lists)

            if lists:
                cur_node.next = lists[0]

        return head



######################################################################
#######################implement my own heap###############################################
######################################################################

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.lists = lists


    def heapify(self, cur):
        l = 2*cur + 1
        r = 2*cur + 2

        if l<= len(self.lists)-1 and self.lists[cur].val > self.lists[l].val: ##left child is the smallest, then swith
            minimal = l
        else:
            minimal = cur


        if r<= len(self.lists-1) and self.lists[r].val < self.lists[minimal].val: ##right child is the smallest
            minimal = r

        if minimal != cur:
            temp = self.lists[cur]
            self.lists[cur] = self.lists[minimal]
            self.lists[minimal] = temp
            self.heapify(minimal)


    def buildHeap(self):
        n = len(self.lists)
        for idx in range(int(n/2-1), -1,-1):
            self.heapify(idx)

    def pop(self)-> ListNode:
        val = self.lists[0]
        self.lists = self.lists[1:]
        self.buildHeap()
        return val

    def replace(self,node:ListNode) -> ListNode:
        self.lists[0] = node
        self.buildHeap()




















