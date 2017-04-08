"""Convert sorted array to binary search tree

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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build_tree(first, last):
            if first > last:
                return None
                
            mid = (first + last) / 2
            root = TreeNode(nums[mid])
            root.left = build_tree(first, mid - 1)
            root.right = build_tree(mid + 1, last)
            return root

        return build_tree(0, len(nums) - 1)