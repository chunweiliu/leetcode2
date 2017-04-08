# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Add value when view
        """
        values = []

        stack, current = [], root
        # [None] is True
        while stack or current:
            if current:
                values.append(current.val)

                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

        return values
        