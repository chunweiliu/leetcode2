# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        level, depth = [root], 1
        while level:

            next_level = []
            for node in level:
                if not node.left and not node.right:
                    return depth

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            depth += 1
            level = next_level