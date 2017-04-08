class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        Question:
            * Negative inputs?

        Edge case:
            * 0

        Bug:
            * 3

        Find a number r such that r ** 2 <= x and (r+1) ** 2 > x
        """

        def square(x):
            return x * x

        first, last = 0, x
        while first + 1 < last:
            mid = (first + last) / 2

            if square(mid) == x:
                return mid

            if square(mid) < x:
                first = mid
            else:
                last = mid

        # For x = 0
        if square(first) <= x and square(last) > x:
            return first
        return last
