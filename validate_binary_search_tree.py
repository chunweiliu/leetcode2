# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r
        
    def __repr__(self):
        return str(self.val)
        
        
class Solution(object):
    def isValidBST(self, root):
        def inorder(node):
            if not node:
                return True

            print 'go left'
            if not inorder(node.left):
                return False

            if self.prev and self.prev.val >= node.val:
                return False

            # This has to be set as global variable.
            #   1 <- node (previous level)
            # 1 <- prev
            # When we go back to preivous level, we should remember the last visited
            # node (prev) is 1 and is equal to the current node (node). Since the
            # function call has been returned. Only global variable will be preserved.
            self.prev = node

            print 'go right'
            if not inorder(node.right):
                return False

            return True

        # The SELF is the key.
        self.prev = None
        return inorder(root)

    def isValidBSTFail(self, root):
        def inorder(node, prev):
            if not node:
                return True

            print 'go left'
            if not inorder(node.left, prev):
                return False

            if prev and prev.val >= node.val:
                return False

            # This won't change when backtracking up to the root
            # because the prev is modified in the next level.
            prev = node

            print 'go right'
            return inorder(node.right, prev)

        return inorder(root, None)
"""
    1
   / \
  1   x
 / \
x   x
"""
print Solution().isValidBSTFail(TreeNode('a', TreeNode('a')))
print '----------'
print Solution().isValidBST(TreeNode('a', TreeNode('a')))