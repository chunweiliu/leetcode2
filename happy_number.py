"""Tell if a number's digit sum will be 1 after enough enumerations

Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_sum(n):
            ret = 0
            while n:
                ret += (n % 10) ** 2
                n /= 10
            return ret

        exist = set()
        while n not in exist:
            exist.add(n)
            n = digit_sum(n)

        if n == 1:
            return True
        return False
        