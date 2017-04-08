"""Link the next pointer for each node in the tree

    <<       1
           /  \
          2    3
         / \    \
        4   5    7

    =>       1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \    \
        4-> 5 -> 7 -> NULL
                
BFS (level order traversal without a queue)

Time: O(n)
Space: O(1)
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        node = root  # current upper level node
        dummy = tail = TreeLinkNode(0)  # current lower level node
        
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            
            tail.next = node.right
            if tail.next:
                tail = tail.next
            
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
                