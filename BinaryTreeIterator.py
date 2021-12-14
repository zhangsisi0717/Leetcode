from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def _iter_helper(self):
        # 0
        if self.left:
            yield from self.left._iter_helper()
        # 1
        yield self.val
        # 2
        if self.right:
            yield from self.right._iter_helper()
        # 3

    # def _equivalent_to_iter_helper(self):
    #     res = []
    #     if self.left:
    #         res += self.left._equivalent_to_iter_helper()
    #
    #     res.append(self.val)
    #
    #     if self.right:
    #         yield from res += self.right._equivalent_to_iter_helper()
    #
    #     return res


    def __iter__(self):
        # return NodeIterator(self)
        return self._iter_helper()

class NodeIterator:
    def __init__(self, node: Node):
        self.stack = deque([{'node': node, 'status': 0}])


    def __next__(self):
        while self.stack:
            cur = self.stack[-1]

            if cur['status'] == 0: # just started
                cur['status'] += 1
                if cur['node'].left: # add left node to stack
                    self.stack.append({'node': cur['node'].left, 'status': 0})
                continue

            if cur['status'] == 1: # returned from first recursion point
                cur['status'] += 1
                return cur['node'].val

            if cur['status'] == 2: # just returned self's value
                cur['status'] += 1
                if cur['node'].right:
                    self.stack.append({'node': cur['node'].right, 'status': 0}) # add right node to stack
                continue

            if cur['status'] == 3: # returned from second recursion point
                self.stack.pop() # we're done with this
                continue

        if not self.stack:
            raise StopIteration


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.left = b
a.right = c
b.left = d

for i in a:
    print(i)
