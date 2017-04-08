"""Reverse a 32 bit integer

Time: O(1)
Space: O(1)
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = 32

        ret = 0
        for i in range(bits):
            # from 0 to 31
            ret += (n % 2) << (bits - i - 1)
            n /= 2

        return ret
