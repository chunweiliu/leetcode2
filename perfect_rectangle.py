"""Find if the rectangles can form a single large rectange

    Three necessary and sufficent conditions:

    * The are of large rect is equal to sum of all small areas.
    * Only four corners appear once and only once.
    * Other connected points appear even number of time.

Time: O(n)
Space: O(n)
"""
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if not rectangles:
            return False

        min_x = sys.maxint
        min_y = sys.maxint
        max_x = -sys.maxint
        max_y = -sys.maxint
        corners = set()

        area = 0
        for rect in rectangles:
            bl = Point(rect[0], rect[1])  # bottom-left
            ur = Point(rect[2], rect[3])  # upper-right

            area += (ur.x - bl.x) * (ur.y - bl.y)

            min_x = min(min_x, bl.x)
            min_y = min(min_y, bl.y)
            max_x = max(max_x, ur.x)
            max_y = max(max_y, ur.y)

            br = Point(rect[0], rect[3])
            ul = Point(rect[2], rect[1])

            for p in (bl, ur, br, ul):
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)

        if len(corners) == 4 and \
           len(corners & set([Point(min_x, min_y), Point(min_x, max_y), Point(max_x, min_y), Point(max_x, max_y)])) == 4 and \
           area == (max_x - min_x) * (max_y - min_y):
            return True
        return False
