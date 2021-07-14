#https://leetcode.com/problems/longest-absolute-file-path/
class Node:
    def __init__(self,val=None,prev=None,next=None,layer=None):
        self.val = val
        self.prev = prev
        self.next = next if next else []
        self.layer = layer
"""
each file/dir is like a node in a n-ary tree
step 1: create the n-ary tree (keep track of next,prev,layers)
step 2: if layer of new_node is less than current_node, then let current_node to go back untill we find the parent of
this new node, and let this new node as current_node

step 3: after creating this n-ary tree, we use dfs to find the longest abolute path
"""
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")
        root_dir = []
        cur_node,root = None,None
        for i in lines:
            # print(i)
            count = 0
            j = 0
            while j < len(i):
                if i[j] == '\t':
                    count +=1
                    j +=1
                else:
                    break

            # print(f"current_count={count}")
            if count == 0:
                cur_node = Node(val=i,prev=None,layer=count)
                if "." not in cur_node.val:
                    root = cur_node
                root_dir.append(cur_node)


            elif count == 1:
                cur_node = Node(val=i[j:],prev=root,layer=count)
                root.next.append(cur_node)

            else:
                new_node = Node(val=i[j:],layer=count)
                if count > cur_node.layer: ##new_node is child of cur_node
                    new_node.prev = cur_node
                    cur_node.next.append(new_node)

                elif count <= cur_node.layer: ##new_node is at the same layer of cur_node
                    while(count<cur_node.layer):
                        cur_node = cur_node.prev
                    new_node.prev = cur_node.prev
                    cur_node.prev.next.append(new_node)

                cur_node = new_node


        def longest(node):
            if not node.next:
                return len(node.val) if "." in node.val else float(-inf)

            return len(node.val) + 1 + max(longest(i) for i in node.next)

        maximum =  max(longest(node) for node in root_dir)

        return maximum if maximum > 0 else 0
