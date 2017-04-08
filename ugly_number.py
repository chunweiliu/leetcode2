class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool

        Wheather if the number only include prime factor 2, 3, 5 or 1.

        # Bugs:
        1. num = 0
        """
        if num == 0 or num < 0:
            return False

        prime_factors = [2, 3, 5]
        for prime_factor in prime_factors:
            while num % prime_factor == 0:
                num /= prime_factor

        return num == 1
        