##https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from typing import List
"""
#seriablize: in-order traversal root -> left-> right
    1
  /   \
  2    3
       / \
       4  5
#1,2,None,None,3,4,None,None,5,None,None##

##deserialize binary tree
step 1: make string into list , l =data.split(",") => [1,2,None,None,3,4,None,None,5,None,None]
step 2: use recursion, 
if l[0] is None:
   then just return
else=> l[0] must be the root element
  then curRoot = TreeNode(l[0])
  then we pop root element from list, l.pop(0)
  
  curRoot.left = recursion(l)
  curRoot.right = recursion(l)
  return curRoot
  
NOTE: in the whole process, we keep popping out first element in l
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "None"

        l,r = "None","None"

        if root.left:
            l = self.serialize(root.left)

        if root.right:
            r = self.serialize(root.right)

        # print(str(root.val) + ","+ l+","+r)
        return str(root.val) + ","+ l+","+r



    def deserialize(self, data):
        l = data.split(",")
        # print(l)
        def recursion(l):
            if l[0] == "None":
                l.pop(0)
                return None

            curRoot = TreeNode(l[0])
            l.pop(0)
            curRoot.left = recursion(l)
            curRoot.right = recursion(l)
            return curRoot

        return recursion(l)
