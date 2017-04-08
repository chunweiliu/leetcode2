"""Return a list of values in vertical order of a tree

    column -1   0   1   2

                1
            2       3
                4       5

    => [[2], [1, 4], [3], [5]]

    - What if the node is on the same column?
        BFS:
          1) Upper; and then 2) left

        DFS:
          1) Left; and then 2) bottom

Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, rigth=None):
        self.val = x
        self.left = left
        self.right = rigth

from collections import defaultdict
from collections import deque

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        columns = defaultdict(list)
        
        queue = deque([(0, root)])

        while queue:
            i, node = queue.popleft()
            
            if node:
                columns[i].append(node.val)
                
                queue += (i - 1, node.left), (i + 1, node.right)
                
        return [columns[i] for i in sorted(columns.keys())]
