"""Design a class to find median for data stream

    - Binary search tree

          mediam
           / \
    smaller   larger

    * This implementation is TLE unless we make it a Red-Black Tree

        - __init__: O(1)
        - addNum: O(log n) (O(n) without balancing)
        - findMedian: O(1)

    - Min-Max heaps

      Max heap has the smaller half (which store negative values)
      Min heap has the larger half



Time: 
    - __init__: O(1)
    - addNum: O(log n)
    - findMedian: O(1)
Space: O(n)
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def size(self, node):
        return node.size if node else 0

    def add(self, num):
        self.root = self.add_to(num, self.root)

    def add_to(self, num, root):
        if not root:
            return TreeNode(num)

        if num > root.val:
            root.right = self.add_to(num, root.right)
        else:
            root.left = self.add_to(num, root.left)

        root.size = sum(map(self.size, [root.left, root.right])) + 1
        return root

    def rank(self, k, root=None):
        root = root or self.root

        size = self.size(root.left) + 1
        if k == size:
            return root.val

        return self.rank(k, root.left) if k < size else self.rank(k - size, root.right)


class MedianFinderTLE:
    def __init__(self):
        self.tree = BinarySearchTree()
        self.count = 0

    def addNum(self, num):
        self.tree.add(num)
        self.count += 1

    def findMedian(self):
        tree = self.tree
        count = self.count

        print tree.rank(1)
        
        if count % 2 == 1:
            return tree.rank(count / 2 + 1)
        return (tree.rank(count / 2) + tree.rank(count / 2 + 1)) / 2.0
        

from heapq import *


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        small, large = self.heaps

        # Make sense to push large first, since one is bigger than nothing.
        # Do push pop for updating the heap. Make sure they do keeps the larger
        # half and smaller half.
        if len(small) == len(large):
            heappush(large, -heappushpop(small, -num))
        else:
            heappush(small, -heappushpop(large, num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        small, large = self.heaps

        # odd number if length is unbalance
        if len(small) == len(large):
            return (large[0] - small[0]) / 2.0
        return large[0]

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
print mf.findMedian()