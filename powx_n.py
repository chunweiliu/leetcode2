"""
Questions:
    - Assume we are not going to use built-in lib.
    - Assume we are not looking for a trivial solution.
    - Is n >= 0?
    - Is x integer?

Time: O(logn)
Space: O(1) (logn stack)
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n == 0:
            return 1

        p = self.myPow(x, n / 2)

        if n % 2 == 0:
            return p * p
        return p * p * x
