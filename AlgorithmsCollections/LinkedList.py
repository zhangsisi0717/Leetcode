class Node:
    def __init__(self,value,restLinkedList):
        self.value = value
        self.next = restLinkedList


class RecursiveLinkedList:
    def __init__(self, head=None):
        self.head = head


    def add(self,value):
        if not self.head:
            self.head = Node(value,RecursiveLinkedList())
            return self.head

        else:
            newNode = Node(value,None)


