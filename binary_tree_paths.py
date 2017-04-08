"""Inorder triversal to print all the tree paths

Time: O(n)
Space: O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        
        def inorder(root, path):
            path.append(str(root.val))
            
            # Stop at each leave. Do not go to None.
            if not root.left and not root.right:
                paths.append('->'.join(path))
                
            # Make copy for the current attemp, otherwise the append
            # will modify an global current object.
            if root.left:
                inorder(root.left, path[:])
            
            if root.right:
                inorder(root.right, path[:])

        paths = []        
        path = []
        if root:      
            inorder(root, path)
        return paths