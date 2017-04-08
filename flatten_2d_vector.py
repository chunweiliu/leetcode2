"""Flatten a 2D array (best practice: using iterator)

    [
      [1,2],
      [3],
      [4,5,6]
    ]

    => [1, 2, 3, 4, 5, 6]

    * Empty deque is not Falsy!!!
    * [[]]

Time: O(1)
Space: O(n)
"""
from collections import deque


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vectors = vec2d

        self.list_index = 0
        self.element_index = 0

    def next(self):
        """
        :rtype: int
        """
        # Advance the element_index
        if self.hasNext():
            value = self.vectors[self.list_index][self.element_index]
            self.element_index += 1
            return value

    def hasNext(self):
        """
        :rtype: bool
        """
        # Keep advance the list index until we found a non empty element list.
        # Otherwise, we have no next element.
        while self.list_index < len(self.vectors):
            if self.element_index < len(self.vectors[self.list_index]):
                return True

            self.list_index += 1
            self.element_index = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())