"""Convert a number to Excel sheet column

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        BASE = 26
        
        s = ''
        while n > 0:
            # Map n from 0 to base - 1
            n -= 1
            
            s = chr(ord('A') + n % BASE) + s
            
            # Use division instead of minus
            n /= BASE
            
        return s


    def convertToTitle1(self, n):
        if n <= 0:
            return ''
        
        n -= 1
        return self.convertToTitle(n / 26) + chr(ord('A') + n % 26) 