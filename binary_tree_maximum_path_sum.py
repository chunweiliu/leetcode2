# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        Each path in this tree is either
        1) starting from a root to a leaf, or
        2) accrossing a root from one subtree to another.

        We exam each node as a root in this tree.

        :type root: TreeNode
        :rtype: int

        Questions:
            * Does the node have negative value?
            - If not than just call max_path_value(root)

        Example: 
              1
            2   3
            => 6
        """
        def max_path_to_root(root):
            if not root:
                return 0

            l = max(0, max_path_to_root(root.left))
            r = max(0, max_path_to_root(root.right))

            # The value won't pass upon.
            #      root
            #    /      \
            # left      right
            self.max_path_value = max(self.max_path_value,
                                      l + root.val + r)
            
            # The value can be passed to its partent.
            # parent
            #       \
            #      root
            #    /
            # left
            return root.val + max(l, r)

        self.max_path_value = None
        max_path_value(root)
        return self.max_path_value
