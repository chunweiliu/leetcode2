"""Symatric tree

          root
     left      right
    (l) [r]   [l]  (r)
  (l) [r]  ...   [l] (r)

  Check left most with right most, and the second left with the second right


Time: O(n)
Space: O(log n)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            #           root
            #      left      right
            #     (l) [r]   [l]  (r)
            #   (l) [r]  ...   [l] (r)
            return (is_mirror(left.left, right.right) and 
                    is_mirror(left.right, right.left))
            
        if not root:
            return True
        return is_mirror(root.left, root.right)