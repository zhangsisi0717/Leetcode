import math
"""
add an element to a binary search tree
"""
class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def addElement(node, element):
    if not node:
        return Node(element)

    if element >= node.val:
        node.right = addElement(node.right, element)

    else:
        node.left = addElement(node.left, element)


    return node

#call addElement(root, element) to add a new element to the BST

"""
find predecessor and successor of current node in a binary tree
"""

def successor(node):
    if not node.right:
        return None
    node = node.right
    while node.left:
        node = node.left
    return node


def predecessor(node):
    if not node.left:
        return None
    node = node.left
    while node.right:
        node = node.right
    return node
"""
delete a specific node from a binary search tree
"""
def deleteElement(node, element):
    if not node:
        return

    if element > node.val:
        node.right = deleteElement(node.right, element)

    elif element < node.val:
        node.left = deleteElement(node.left, element)

    else:
        if node.right:
            node.val = successor(node).val
            node.right = deleteElement(node.right, node.right.val)

        elif node.left:
            node.val = successor(node).val
            node.left = deleteElement(node.left, node.left.val)

        else:
            return

    return node









