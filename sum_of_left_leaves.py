# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Example:
            6
        12      7
              9

        return 12 + 9

        Binary tree: at most two children, a child can be either left or right.
        """
        if not root:
            return 0

        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        total += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return total
