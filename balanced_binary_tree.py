# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isBalanced(self, root):
        """
        Time: O(n), In order traversal (DFS)
        """
        def DFS_height(root):
            if not root:
                return 0

            left_height = DFS_height(root.left)
            if left_height == -1:
                return -1

            right_height = DFS_height(root.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return DFS_height(root) != -1

    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time: O(n^2)
        """
        if not root:
            return True

        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # Height is for a tree; Depth is for a tree node.
    # http://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height
    # Example: Height is computed from call stack.
    #        3
    #       / \
    #      2   1
    #     /     \
    #    1
    #   /
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
        
root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(1))
print Solution().isBalanced(root)