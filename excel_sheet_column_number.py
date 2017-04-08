class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int

        Example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 

        26 base conversion
        """
        number = 0
        for i, c in enumerate(list(s[::-1])):
            number += (ord(c) - ord('A') + 1) * 26 ** i
        return number
        