class Node:
    def __init__(self,value=None,next=None,prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self,head=None):
        self.head = head
        self.cur_node=head

    def append(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            curNode = self.head
            while curNode.next:
                curNode = curNode.next

            newNode = Node(value)
            curNode.next = newNode
            newNode.prev = curNode

    def appendAll(self,values):
        for value in values:
            self.append(value)

    def __str__(self):
        re = ""
        curNode = self.head
        while curNode:
            re += str(curNode.value) + " "
            curNode = curNode.next
        return "[" + re[:-1] + "]"

    def __len__(self):
        length=0
        curNode = self.head
        while curNode:
            curNode = curNode.next
            length+=1

        return length

    def __iter__(self):
        self.cur_node = self.head
        return LinkedListIterator(head=self.head)

    def __next__(self):
        if not self.cur_node:
            raise StopIteration
        else:
            temp = self.cur_node
            self.cur_node = temp.next

    def __getitem__(self, key):
        idx=0
        cur_node = self.head
        while(idx<key):
            idx +=1
            cur_node = cur_node.next
        return cur_node.value

    def __setitem__(self, key, value):
        idx=0
        cur_node = self.head
        while(idx<key):
            idx +=1
            cur_node = cur_node.next
        cur_node.value = value

    def __contains__(self, value):
        cur_node = self.head
        while(cur_node):
            if cur_node.value == value:
                return True
            cur_node = cur_node.next
        return False


class LinkedListIterator:
    def __init__(self,head:Node):
        self.cur_node = head

    def __next__(self):
        if not self.cur_node:
            raise StopIteration
        else:
            temp = self.cur_node
            self.cur_node = temp.next
            return temp



ll = LinkedList()
ll.appendAll([1,2,3,4,5])

for i in ll:
    print(i)



heapq.heapify(l)
heapq.heappush(heap, item)
heapq.heappop(heap)


