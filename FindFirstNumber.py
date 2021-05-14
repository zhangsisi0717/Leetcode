###https://leetcode.com/problems/first-unique-number/##
###double-linked-lists and hashmap
from type_checking import *
from collections import deque
from collections import defaultdict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = None
        self.tail = None
        self.unique_queue = dict()
        self.all_num_set = set()
        for i in nums:
            self.add(i)
            print(f"self.all_num_set = {self.all_num_set}")
            print(f"self.unique_queue = {self.unique_queue}")

    def showFirstUnique(self) -> int:
        return self.head if self.head else -1


    def add(self, value: int) -> None:
        if value not in self.all_num_set: ##this value never showed up
            self.all_num_set.add(value)
            if not self.head and not self.tail: ##if this queue is empty. add value as head
                self.unique_queue={value:[None,None]}
                self.head = value
            elif self.head and not self.tail: ## if there is not self.tail
                self.tail = value
                self.unique_queue[self.tail] = [self.head,None]
                self.unique_queue[self.head][1] = value
            else:
                self.unique_queue[self.tail][1] = value
                self.unique_queue[value] = [self.tail,None]
                self.tail = value

        elif value in self.all_num_set and value in self.unique_queue:##remove
            pre,sur = self.unique_queue[value]
            if not pre and not sur: ##only one left
                self.head,self.tail = None,None
                self.unique_queue = dict()

            elif not pre and sur :
                self.head = sur
                self.unique_queue[sur][0] = None
            elif not sur and pre:
                self.tail = pre
                self.unique_queue[pre][1] = None
            else:
                self.unique_queue[pre][1] = sur
                self.unique_queue[sur][0] = pre

        print(f"add_value = {value}")
        print(f"self.unique_queue={self.unique_queue}")

a = FirstUnique(b)
a.showFirstUnique()
a.add(5)
a.showFirstUnique()
a.add(2)
a.showFirstUnique()
a.add(3)
a.showFirstUnique()
a.add(7)
a.showFirstUnique()

b= [27, 5, 27, 14, 7, 30, 26, 14, 13, 1, 3, 2, 9, 3, 30, 25, 23, 21, 7, 22]