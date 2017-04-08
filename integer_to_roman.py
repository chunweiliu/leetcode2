"""Transfer integer to roman

    1 => I
    4 => IV
    5 => V
    6 => VI

    Greddy stacking the largest number from the left to right

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX','V', 'IV', 'I']

        ret = ''
        for value, roman in zip(values, romans):
            ret += roman * (num / value)
            num %= value

        return ret
