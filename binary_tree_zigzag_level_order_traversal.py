"""Zigzag level order traversal on a binary tree

        3
       / \
      9  20
        /  \
       15   7

    [
      [3],
      [20,9],
      [15,7]
    ]

Time: O(n)
Space: O(n)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        flip = -1

        ret = []
        froniter = [root]
        while froniter:
            if flip == 1:
                ret.append([node.val for node in froniter[::-1]])
            else:
                ret.append([node.val for node in froniter])
            flip *= -1

            next = []
            for node in froniter:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            froniter = next

        return ret