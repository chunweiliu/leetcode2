"""A lowest common ancestor is a node that have p and q in different subtree.

Time: O(n)
Space: O(logn) for stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """        
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def search(root, p, q):
            if not root:
                return None

            if root == p or root == q:
                return root

            found_in_left = search(root.left, p, q)
            found_in_right = search(root.right, p, q)

            # Early stop
            if found_in_left and found_in_right:
                return root

            return found_in_left or found_in_right

        return search(root, p, q)


    def lowestCommonAncestorShort(self, root, p, q):
        if root in (None, p, q):
            return root

        left, right = (self.lowestCommonAncestor(child, p, q) 
                       for child in (root.left, root.right))

        return root if left and right else left or right

        