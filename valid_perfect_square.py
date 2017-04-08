"""Return True if a number is a perfect square, else False

    Binary search

Time: O(log n)
Space: O(1)
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lower = 1
        upper = num
        while lower + 1 < upper:
            mid = (lower + upper) / 2

            square = mid * mid
            if square == num:
                return True

            if square < num:
                lower = mid
            else:
                upper = mid

        if lower * lower == num:
            return True
        if upper * upper == num:
            return True
        return False

