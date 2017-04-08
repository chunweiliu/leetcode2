"""Link the next pointer for each node in the tree

    <<       1
           /  \
          2    3
         / \    \
        4   5    7

          upper  1 -> None
                /  \
     lower ->  2 -> 3 -> None
              / \    \
             4-> 5 -> 7 -> None
     

                 1 -> None
                /  \
lower-> upper  2 -> 3 -> None
              / \    \
             4-> 5 -> 7 -> None

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
        upper = root             # current upper level node
        dummy = TreeLinkNode(0)  # just a dummy pointer that will point to next lower node
        lower = dummy
        
        while upper:
            lower.next = upper.left
            if lower.next:
                lower = lower.next
            
            lower.next = upper.right
            if lower.next:
                lower = lower.next
            
            upper = upper.next
            if not upper:
                lower = dummy       # reuse dummy head
                upper = dummy.next  # dummy always point to the first left node
                