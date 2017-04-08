"""
Multiply two strings

      100
    x 100
    -----
    10000
    
    Beaware 0 x 0

Time: O(n^2)
Space: O(1)
"""
class Solution(object):
    def multiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Need to be reversed
        m = [0] * (len(a) + len(b))
        
        for i, aa in enumerate(reversed(a)):
            for j, bb in enumerate(reversed(b)):
                m[i + j] += int(aa) * int(bb)
            
                # Should be added whatever we have in the previous digit. 
                # It might come from different mutliplication.
                m[i + j + 1] += m[i + j] / 10
                
                m[i + j] %= 10
        
        return ''.join(map(str, m[::-1])).lstrip('0') or '0'
