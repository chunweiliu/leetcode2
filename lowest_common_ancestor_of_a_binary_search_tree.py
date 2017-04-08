"""Find the lowest common ancestor in a BST

    If both p and q smaller than root, go left
    If both p and q larger than root, go right
    Otherwise, return root

Time: O(n)
Space: O(1)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
