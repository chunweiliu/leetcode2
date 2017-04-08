# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = []

        previous = None
        stack, current = [], root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek = stack[-1]
                if not peek.right or (peek.right == previous):
                    values.append(peek.val)
                    previous = stack.pop()
                else:
                    current = peek.right

        return values
