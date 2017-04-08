"""Return the length of the longest consecutive sequence

    1
    \
     3
    / \
   2   4
        \
         5

    => 3, for a path 3->4->5

    BFS. Start a new search once the next node is not consecutive

    * the original length starts with 1, not 0.
    * consecutive means n and n + 1, not n and m such that m > n.

Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        length = 1
        queue = deque([(length, root)])

        while queue:
            l, node = queue.popleft()
            length = max(length, l)

            if node.left:
                if node.left.val == node.val + 1:
                    queue.append((l + 1, node.left))
                else:
                    queue.append((1, node.left))

            if node.right:
                if node.right.val == node.val + 1:
                    queue.append((l + 1, node.right))
                else:
                    queue.append((1, node.right))

        return length
        