##https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque
"""
a tree is 
    1
   / \
  2  3 
  /\ /\
 4 5 6 7

if need to tranverse layers in order such as : [[1],[2,3],[4,5,6,7]], need to use BFS
if need to tranverse in zigzag, just keep track of which layer it is ,if it is odd layer, then reverse the list
 
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result = []
        queue = deque([[root,0]])
        while(queue):
            node,layer = queue.popleft()
            if node.left:queue.append([node.left,layer+1])
            if node.right:queue.append([node.right,layer+1])

            if layer>=len(result):
                if layer % 2 == 0 and layer>0: result[layer-1].reverse()
                result.append([node.val])
            else:
                result[layer].append(node.val)

        if layer % 2 == 1: result[layer].reverse()
        return result
