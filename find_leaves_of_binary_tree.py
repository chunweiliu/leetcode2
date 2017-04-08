"""Collect a tree's nodes within the same height

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
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def height(root):
            if not root:
                return -1
            
            current_height = 1 + max(height(root.left), height(root.right))
            
            if current_height == len(leafs):
                leafs.append([])
            leafs[current_height].append(root.val)
            
            return current_height
            
        leafs = []
        height(root)
        
        return leafs
        