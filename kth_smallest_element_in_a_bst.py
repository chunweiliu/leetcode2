"""Find kth smallest element in a BST

    Build a BST iterator

Time: O(n)
Spcae: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.move_to_left_most(root)

    def move_to_left_most(self, node):
        while node:
            self.stack.append(node)        
            node = node.left

    def has_next(self):
        if self.stack:
            return True
        return False

    def next(self):
        if self.has_next():
            node = self.stack.pop()
            if node.right:
                self.move_to_left_most(node.right)
            return node.val


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        iterator = BSTIterator(root)

        for i in range(k - 1):
            if iterator.has_next():
                iterator.next()
        return iterator.next()
