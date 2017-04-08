# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
             4
           /   \
          2     7
         / \   / \
        1   3 6   9

             4
           /   \
          7     2
         / \   / \
        9   6 3   1
        """
        if not root:
            return root

        # Python swap:
        # a, b = b, a
        # Load b and a into a stack [b, a]
        # Swap the stack to get [a, b]
        # Pop the stack from the back and assign them to the variables on left.
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
