"""Flip a binary tree

Retrieve the left most node, rotate the subtree from there, and go back to the upper one.


Questions:
    - Do you mean every sub tree has three nodes?
    - left -> root; root -> right; right -> left? (sub structure not maintain)

Bugs:
    - Didn't make the recursion in the beginning.
    - From top to down, rotate the subtree.
        - Should be buttom-up

Examples:
    from 
      1
    2   3
  4  5

    to
      4
    5   2
       3 1

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
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root

        left_most = self.upsideDownBinaryTree(root.left)

        #   from    to
        #    1      2
        #   2 3    3 1
        #  /\        /\
        # N  N      N  N
        left = root.left
        left.left, left.right = root.right, root
        root.left = root.right = None

        return left_most

    def upsideDownBinaryTree_bug(self, root):
        def rotate(root):
            
            if root.left and root.right:
                left, right = root.left, root.right

                left.left, left.right = right, root
                root.left = root.right = None
            return root

        if root.left:
            return rotate(root.left)
