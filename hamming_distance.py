"""Compute hamming distance (bit difference) using binary opperator

    << (1, 4)
    => 2

Time: O(logn)
Space: O(1)
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dist = 0

        # Find the different bits
        bit_diff = x ^ y

        # Count how many different bit
        while bit_diff:
            # Two ways to take off the right most bit
            # bit_diff -= bit_diff & (-bit_diff)
            bit_diff &= bit_diff - 1
            dist += 1

        return dist