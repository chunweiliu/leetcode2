"""Find the value that is the closest to the target in a BST

            6
        3       9
      1   5    8
       2 4    7

Time: O(n)
Space: O(1)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return root

        def closer(target, a, b):
            return a if abs(target - a) < abs(target - b) else b

        closest = root.val
        while root:
            closest = closer(target, closest, root.val)
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return closest
