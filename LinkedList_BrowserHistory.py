##https://leetcode.com/problems/design-browser-history/
##double linked list
class Node:
    def __init__(self,val=None,prev=None,next_v=None):
        self.val = val
        self.prev = prev
        self.next = next_v

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage,None,None)

    def visit(self, url: str) -> None:
        self.cur.next = Node(url,self.cur,None)
        self.cur = self.cur.next


    def back(self, steps: int) -> str:
        cur_node = self.cur
        while(steps>0 and cur_node.prev):
            cur_node = cur_node.prev
            steps -=1
        self.cur = cur_node
        return self.cur.val


    def forward(self, steps: int) -> str:
        cur_node = self.cur
        while(steps>0 and cur_node.next):
            cur_node = cur_node.next
            steps -=1
        self.cur = cur_node
        return self.cur.val

