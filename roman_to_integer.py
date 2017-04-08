"""Roman to integer

    Place for digit is not matter for Roman number
    The order of digit is

    If a small Roman number appear in the left, it means substraction.
    IX => X - I = 10 - 1 = 9

    Start backward would be eailer

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        ROMANS = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        def roman(c):
            return ROMANS[c]

        ret = 0

        prev = 1
        for r in reversed(map(roman, s)):
            if r < prev:
                ret -= r
            else:
                ret += r
            prev = r

        return ret
        