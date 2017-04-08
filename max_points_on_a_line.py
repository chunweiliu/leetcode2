"""Return max points on a line

    Count slope

    * Only one point
    * Duplicate points
    * Clear slope for each pivot

Time: O(n^2)
Space: O(n^2)
"""

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_points = 0

        for i, pivot in enumerate(points):
            # Renew the slope counter for each pivot
            slopes = defaultdict(int)
            
            # Only one point should still count
            points_at_pivot = 1
            for point in points[i + 1:]:
                dx = point.x - pivot.x
                dy = point.y - pivot.y

                # Duplicated points have no slope
                if dx == 0 and dy == 0:
                    points_at_pivot += 1
                else:
                    if dx == 0:
                        slope = 'vertical'
                    else:
                        slope = float(dy) / dx
                    slopes[slope] += 1

            max_for_pivot = points_at_pivot
            if slopes.values():
                max_for_pivot += max(value for value in slopes.values())
            
            max_points = max(max_points, max_for_pivot)

        return max_points