class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """        
        # Only have one bit been set
        return n > 0 and n & (n - 1) == 0
